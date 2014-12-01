import tornado.ioloop
from functools import partial
from elasticsearch_tornado import IndicesClient
try:
    # python 2.6
    from unittest2 import TestCase, SkipTest
except ImportError:
    from unittest import TestCase, SkipTest


class IndicesClientTest(TestCase):

    def test_analyze(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.analyze(index='test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_refresh(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.refresh(index='test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_flush(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.flush(index='test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_create(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.create('test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_get(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.get('test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_open(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.open('test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_close(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.close('test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_delete(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.delete('test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_exists(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.exists('test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_exists_type(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.exists_type('test', 'type', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_put_mapping(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.put_mapping('test', '{}', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_get_mapping(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.get_mapping(index='test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_get_field_mapping(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.get_field_mapping('test', index='test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_delete_mapping(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.delete_mapping('test', 'test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_put_alias(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.put_alias('test', 'test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_exists_alias(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.exists_alias('test', index='test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_get_alias(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.get_alias(index='test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_get_aliases(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.get_aliases(index='test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_update_aliases(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.update_aliases('{}', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_delete_alias(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.delete_alias('test', 'test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_put_template(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.put_template('test', '{}', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_exists_template(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.exists_template('test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_get_template(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.get_template(name='test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_delete_template(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.delete_template('test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_get_settings(self):
        c = IndicesClient()
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
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.put_settings("", cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_put_warmer(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.put_warmer("test", "", cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_get_warmer(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.get_warmer(cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_delete_warmer(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.delete_warmer('test', 'test', cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_status(self):
        c = IndicesClient()
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

    def test_stats(self):
        c = IndicesClient()
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

    def test_segments(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.segments(cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_optimize(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.optimize(cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_validate_query(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.validate_query(cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_clear_cache(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.clear_cache(cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_recovery(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.recovery(cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_snapshot_index(self):
        c = IndicesClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.snapshot_index(cb=test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

