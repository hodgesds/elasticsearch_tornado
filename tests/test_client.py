import tornado.ioloop
from functools import partial
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
        c.ping(cb = test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_info(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.info(cb = test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_index(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.index('test', 'test', '{"test":"123"}', doc_id='test123', cb = test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_exists(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.exists('test', 'test123', cb = test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_get(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.get('test', 'test123', cb = test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_get_source(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.get_source('test', 'test123', cb = test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_mget(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.mget('{"_id":"test123"}', index='test', doc_type='test', cb = test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_update(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.update('test', 'test', 'test123', body='{"update":"field"}', cb = test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_search(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.search(index='test', doc_type='test', cb = test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_search_shards(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.search_shards(index='test', doc_type='test', cb = test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_search_template(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.search_template(index='test', doc_type='test', cb = test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_explain(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.explain('test', 'test', 'test123', cb = test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_scroll(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.scroll('testscroll', cb = test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_clear_scroll(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.clear_scroll('testscroll', cb = test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_delete(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.delete('test', 'test', 'test123', cb = test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_count(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.count(index='test', doc_type='test', cb = test_cb)
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_bulk(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.bulk(
                '{"bulk":"bulk1","id_":"bulk1"}', index='test', doc_type='test',
                cb = test_cb
        )
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_msearch(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.msearch(
                '{"bulk":"bulk1","id_":"bulk1"}', index='test', doc_type='test',
                cb = test_cb
        )
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_delete_by_query(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.delete_by_query(
                'test',
                body='{"bulk":"bulk1","id_":"bulk1"}', doc_type='test',
                cb = test_cb
        )
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_suggest(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.suggest(
                '{"bulk":"bulk1","id_":"bulk1"}', index='test',
                cb = test_cb
        )
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_percolate(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.percolate(
                'test',
                'test',
                body='{"bulk":"bulk1","id_":"bulk1"}',
                cb = test_cb
        )
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_mpercolate(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.mpercolate(
                '{"bulk":"bulk1","id_":"bulk1"}',
                index='test',
                doc_type='test',
                cb = test_cb
        )
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_count_percolate(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.count_percolate(
                'test',
                'test',
                cb = test_cb
        )
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_mlt(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.mlt(
                'index',
                'index',
                'bulk1',
                cb = test_cb,
                **{"request_timeout":3}
        )
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_termvector(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.termvector(
                'index',
                'index',
                'bulk1',
                cb = test_cb,
                **{"request_timeout":3}
        )
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_mtermvector(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.mtermvectors(
                index = 'index',
                doc_type = 'index',
                cb = test_cb,
                **{"request_timeout":3}
        )
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_benchmark(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.benchmark(
                index = 'index',
                doc_type = 'index',
                cb = test_cb,
                **{"request_timeout":3}
        )
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_abort_benchmark(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.abort_benchmark(
                cb = test_cb,
                **{"request_timeout":3}
        )
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_list_benchmarks(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.list_benchmarks(
                index = 'test',
                cb = test_cb,
                **{"request_timeout":3}
        )
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_put_script(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.put_script(
                'python',
                'testscript123',
                "1+1",
                cb = test_cb,
                **{"request_timeout":3}
        )
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_get_script(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            if hasattr(req, 'code'):
                self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.get_script(
                'python',
                'testscript123',
                cb = test_cb,
                **{"request_timeout":3}
        )
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_delete_script(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.delete_script(
                'python',
                'testscript123',
                cb = test_cb,
                **{"request_timeout":3}
        )
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_put_template(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.put_template(
                'temp123',
                '{"template":"test123"}',
                cb = test_cb,
                **{"request_timeout":3}
        )
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_get_template(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            if hasattr(req, 'code'):
                self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.get_template(
                'temp123',
                cb = test_cb,
                **{"request_timeout":3}
        )
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()

    def test_delete_template(self):
        c = BaseClient()
        io_loop = tornado.ioloop.IOLoop.current()
        def test_cb(req):
            self.assertEqual(200, req.code)
            ioloop = tornado.ioloop.IOLoop.current()
            ioloop.stop()
        c.delete_template(
                temp_id='temp123',
                cb = test_cb,
                **{"request_timeout":3}
        )
        def test_timeout(ioloop):
            if not ioloop._stopped:
                ioloop.stop()
                raise error("Test timeout")
        tpartial = partial(test_timeout, io_loop)
        io_loop.add_timeout(io_loop.time()+1.5, tpartial)
        io_loop.start()
