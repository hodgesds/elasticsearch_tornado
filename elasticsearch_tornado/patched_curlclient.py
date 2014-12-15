from tornado.curl_httpclient import CurlAsyncHTTPClient


class PatchedCurlClient(CurlAsyncHTTPClient):
    def _curl_setup_request(self, curl, request, buffer, headers):
        curl.setopt(pycurl.URL, native_str(request.url))

        # libcurl's magic "Expect: 100-continue" behavior causes delays
        # with servers that don't support it (which include, among others,
        # Google's OpenID endpoint).  Additionally, this behavior has
        # a bug in conjunction with the curl_multi_socket_action API
        # (https://sourceforge.net/tracker/?func=detail&atid=100976&aid=3039744&group_id=976),
        # which increases the delays.  It's more trouble than it's worth,
        # so just turn off the feature (yes, setting Expect: to an empty
        # value is the official way to disable this)
        if "Expect" not in request.headers:
            request.headers["Expect"] = ""

        # libcurl adds Pragma: no-cache by default; disable that too
        if "Pragma" not in request.headers:
            request.headers["Pragma"] = ""

        curl.setopt(pycurl.HTTPHEADER,
                    ["%s: %s" % (native_str(k), native_str(v))
                     for k, v in request.headers.get_all()])

        curl.setopt(pycurl.HEADERFUNCTION,
                    functools.partial(self._curl_header_callback,
                        headers, request.header_callback))
        if request.streaming_callback:
            write_function = lambda chunk: self.io_loop.add_callback(
                request.streaming_callback, chunk)
        else:
            write_function = buffer.write
        if bytes is str:  # py2
            curl.setopt(pycurl.WRITEFUNCTION, write_function)
        else:  # py3
            # Upstream pycurl doesn't support py3, but ubuntu 12.10 includes
            # a fork/port.  That version has a bug in which it passes unicode
            # strings instead of bytes to the WRITEFUNCTION.  This means that
            # if you use a WRITEFUNCTION (which tornado always does), you cannot
            # download arbitrary binary data.  This needs to be fixed in the
            # ported pycurl package, but in the meantime this lambda will
            # make it work for downloading (utf8) text.
            curl.setopt(pycurl.WRITEFUNCTION, lambda s: write_function(utf8(s)))
        curl.setopt(pycurl.FOLLOWLOCATION, request.follow_redirects)
        curl.setopt(pycurl.MAXREDIRS, request.max_redirects)
        curl.setopt(pycurl.CONNECTTIMEOUT_MS, int(1000 * request.connect_timeout))
        curl.setopt(pycurl.TIMEOUT_MS, int(1000 * request.request_timeout))
        if request.user_agent:
            curl.setopt(pycurl.USERAGENT, native_str(request.user_agent))
        else:
            curl.setopt(pycurl.USERAGENT, "Mozilla/5.0 (compatible; pycurl)")
        if request.network_interface:
            curl.setopt(pycurl.INTERFACE, request.network_interface)
        if request.decompress_response:
            curl.setopt(pycurl.ENCODING, "gzip,deflate")
        else:
            curl.setopt(pycurl.ENCODING, "none")
        if request.proxy_host and request.proxy_port:
            curl.setopt(pycurl.PROXY, request.proxy_host)
            curl.setopt(pycurl.PROXYPORT, request.proxy_port)
            if request.proxy_username:
                credentials = '%s:%s' % (request.proxy_username,
                                         request.proxy_password)
                curl.setopt(pycurl.PROXYUSERPWD, credentials)
        else:
            curl.setopt(pycurl.PROXY, '')
            curl.unsetopt(pycurl.PROXYUSERPWD)
        if request.validate_cert:
            curl.setopt(pycurl.SSL_VERIFYPEER, 1)
            curl.setopt(pycurl.SSL_VERIFYHOST, 2)
        else:
            curl.setopt(pycurl.SSL_VERIFYPEER, 0)
            curl.setopt(pycurl.SSL_VERIFYHOST, 0)
        if request.ca_certs is not None:
            curl.setopt(pycurl.CAINFO, request.ca_certs)
        else:
            # There is no way to restore pycurl.CAINFO to its default value
            # (Using unsetopt makes it reject all certificates).
            # I don't see any way to read the default value from python so it
            # can be restored later.  We'll have to just leave CAINFO untouched
            # if no ca_certs file was specified, and require that if any
            # request uses a custom ca_certs file, they all must.
            pass

        if request.allow_ipv6 is False:
            # Curl behaves reasonably when DNS resolution gives an ipv6 address
            # that we can't reach, so allow ipv6 unless the user asks to disable.
            curl.setopt(pycurl.IPRESOLVE, pycurl.IPRESOLVE_V4)
        else:
            curl.setopt(pycurl.IPRESOLVE, pycurl.IPRESOLVE_WHATEVER)

        # Set the request method through curl's irritating interface which makes
        # up names for almost every single method
        curl_options = {
            "GET": pycurl.HTTPGET,
            "POST": pycurl.POST,
            "PUT": pycurl.UPLOAD,
            "HEAD": pycurl.NOBODY,
        }
        custom_methods = set(["DELETE", "OPTIONS", "PATCH"])
        for o in curl_options.values():
            curl.setopt(o, False)
        if request.method in curl_options:
            curl.unsetopt(pycurl.CUSTOMREQUEST)
            curl.setopt(curl_options[request.method], True)
        elif request.allow_nonstandard_methods or request.method in custom_methods:
            curl.setopt(pycurl.CUSTOMREQUEST, request.method)
        else:
            raise KeyError('unknown method ' + request.method)

        #####################################################################
        # XXX: PATCHED
        #####################################################################
        #
        # Handle curl's cryptic options for every individual HTTP method
        #if request.method == "GET":
        #    if request.body is not None:
        #        raise ValueError('Body must be None for GET request')
        #####################################################################
        if request.method in ("POST", "PUT") or request.body:
            if request.body is None:
                raise ValueError(
                    'Body must not be None for "%s" request'
                    % request.method)

            request_buffer = BytesIO(utf8(request.body))
            def ioctl(cmd):
                if cmd == curl.IOCMD_RESTARTREAD:
                    request_buffer.seek(0)
            curl.setopt(pycurl.READFUNCTION, request_buffer.read)
            curl.setopt(pycurl.IOCTLFUNCTION, ioctl)
            if request.method == "POST":
                curl.setopt(pycurl.POSTFIELDSIZE, len(request.body))
            else:
                curl.setopt(pycurl.UPLOAD, True)
                curl.setopt(pycurl.INFILESIZE, len(request.body))

        if request.auth_username is not None:
            userpwd = "%s:%s" % (request.auth_username, request.auth_password or '')

            if request.auth_mode is None or request.auth_mode == "basic":
                curl.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_BASIC)
            elif request.auth_mode == "digest":
                curl.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_DIGEST)
            else:
                raise ValueError("Unsupported auth_mode %s" % request.auth_mode)

            curl.setopt(pycurl.USERPWD, native_str(userpwd))
            gen_log.debug("%s %s (username: %r)", request.method, request.url,
                          request.auth_username)
        else:
            curl.unsetopt(pycurl.USERPWD)
            gen_log.debug("%s %s", request.method, request.url)

        if request.client_cert is not None:
            curl.setopt(pycurl.SSLCERT, request.client_cert)

        if request.client_key is not None:
            curl.setopt(pycurl.SSLKEY, request.client_key)

        if threading.activeCount() > 1:
            # libcurl/pycurl is not thread-safe by default.  When multiple threads
            # are used, signals should be disabled.  This has the side effect
            # of disabling DNS timeouts in some environments (when libcurl is
            # not linked against ares), so we don't do it when there is only one
            # thread.  Applications that use many short-lived threads may need
            # to set NOSIGNAL manually in a prepare_curl_callback since
            # there may not be any other threads running at the time we call
            # threading.activeCount.
            curl.setopt(pycurl.NOSIGNAL, 1)
        if request.prepare_curl_callback is not None:
            request.prepare_curl_callback(curl)

