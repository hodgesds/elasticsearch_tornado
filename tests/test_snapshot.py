import tornado.ioloop
from functools import partial
from elasticsearch_tornado import SnapshotClient
try:
    # python 2.6
    from unittest2 import TestCase, SkipTest
except ImportError:
    from unittest import TestCase, SkipTest


class SnapshotClientTest(TestCase):

    def test_create(self):
        c = SnapshotClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.create('test', 'test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_delete(self):
        c = SnapshotClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.delete('test', 'test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_get(self):
        c = SnapshotClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.get('test', 'test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_delete_repository(self):
        c = SnapshotClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.delete_repository('test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_get_repository(self):
        c = SnapshotClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.get_repository(cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_create_repository(self):
        c = SnapshotClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.create_repository('test', '{}', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_restore(self):
        c = SnapshotClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.restore('test', 'test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_status(self):
        c = SnapshotClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.status(cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_verify_repository(self):
        c = SnapshotClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.verify_repository('test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

