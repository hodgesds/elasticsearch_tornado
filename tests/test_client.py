import tornado.ioloop
from elasticsearch_tornado import BaseClient
try:
    # python 2.6
    from unittest2 import TestCase, SkipTest
except ImportError:
    from unittest import TestCase, SkipTest


class BaseClientTest(TestCase):
    def test_mk_req(self):
        c = BaseClient()
        # making a req for async http client should work
        self.assertEquals(c.base_url, c.mk_req('').url)
        self.assertEquals('GET', c.mk_req('').method)

    def test_mk_url(self):
        c = BaseClient()
        # test making urls
        url = c.mk_url(*['a','b','c'], **{'key':'value'})
        self.assertEquals('/a/b/c?key=value', url)

    def test_ping(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.ping(cb=test_cb)
        io_loop.start()

    def test_info(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.info(cb=test_cb)
        io_loop.start()
