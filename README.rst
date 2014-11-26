Python Elasticsearch Client
===========================

Tornado http client for Elasticsearch. Its goal is to provide common
ground for all Elasticsearch-related code in tornado and provide a
similar api to the official elasticsearch python.
Compatibility
-------------

The library is compatible with Elasticsearch 1.x



Example use
-----------

Simple use-case::

    >>> fromm elasticsearch_tornado import EsClient
    >>> import tornado.ioloop

    >>> def ex_cb(req):
    >>>     print req
    >>>     ioloop = tornado.ioloop.IOLoop.instance()
    >>>     ioloop.stop()

    >>> io_loop = tornado.ioloop.IOLoop.instance()

    >>> c = EsClient()
    # make an info request (same as http://localhost:9200)
    >>> c.info(cb=ex_cb)
    >>> io_loop.start()



Features
--------

The client's features include:

 * translating basic Python data types to and from json (datetimes are not
   decoded for performance reasons)
 * configurable automatic discovery of cluster nodes
 * persistent connections
 * load balancing (with pluggable selection strategy) across all available nodes
 * failed connection penalization (time based - failed connections won't be
   retried until a timeout is reached)
 * thread safety
 * pluggable architecture


License
-------

Copyright 2013 Daniel Hodges

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Build status
------------

.. image:: https://travis-ci.org/hodgesds/elasticsearch_tornado.svg?branch=master
    :target: https://travis-ci.org/hodgesds/elasticsearch_tornado
