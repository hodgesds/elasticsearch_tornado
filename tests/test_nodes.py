import tornado.ioloop
from functools import partial
from elasticsearch_tornado import NodesClient
try:
    # python 2.6
    from unittest2 import TestCase, SkipTest
except ImportError:
    from unittest import TestCase, SkipTest


class NodesClientTest(TestCase):

    def test_info(self):
        c = NodesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.info(cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_stats(self):
        c = NodesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.stats(cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_hot_threads(self):
        c = NodesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.hot_threads(cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()
