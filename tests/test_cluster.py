import tornado.ioloop
from functools import partial
from elasticsearch_tornado import ClusterClient
try:
    # python 2.6
    from unittest2 import TestCase, SkipTest
except ImportError:
    from unittest import TestCase, SkipTest


class ClusterClientTest(TestCase):

    def test_health(self):
        c = ClusterClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.health(index='test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_pending_tasks(self):
        c = ClusterClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.pending_tasks(cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_state(self):
        c = ClusterClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.state(cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_stats(self):
        c = ClusterClient()
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

    def test_reroute(self):
        c = ClusterClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.reroute(cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_get_settings(self):
        c = ClusterClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.get_settings(cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_put_settings(self):
        c = ClusterClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.put_settings('{}', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()
