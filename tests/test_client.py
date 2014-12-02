import tornado.ioloop
from   tornado.testing import AsyncTestCase
from   elasticsearch_tornado import BaseClient
try:
    # python 2.6
    from unittest2 import TestCase, SkipTest
except ImportError:
    from unittest import TestCase, SkipTest


class BaseClientTest(AsyncTestCase):

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

    def handle_cb(self, req):
        print req
        self.assertEqual(200, req.code)
        self.stop()

    def test_ping(self):
        c = BaseClient()
        c.ping(cb=self.handle_cb)
        self.wait()

    def test_info(self):
        c = BaseClient()
        c.info(cb=self.handle_cb)
        self.wait()

    def test_index(self):
        c = BaseClient()
        c.index('test', 'test', '{"test":"123"}', doc_id='test123', cb=self.handle_cb)
        self.wait()

    def test_exists(self):
        c = BaseClient()
        c.exists('test', 'test123', cb=self.handle_cb)
        self.wait()

    def test_get(self):
        c = BaseClient()
        c.get('test', 'test123', cb=self.handle_cb)
        self.wait()

    def test_get_source(self):
        c = BaseClient()
        c.get_source('test', 'test123', cb=self.handle_cb)
        self.wait()

    def test_mget(self):
        c = BaseClient()
        c.mget('{"_id":"test123"}', index='test', doc_type='test', cb=self.handle_cb)
        self.wait()

    def test_update(self):
        c = BaseClient()
        c.update('test', 'test', 'test123', body='{"script":"ctx._source.tags += tag", "params":{"tag":"blue"}}', cb=self.handle_cb)
        self.wait()

    def test_search(self):
        c = BaseClient()
        c.search(index='test', doc_type='test', cb=self.handle_cb)
        self.wait()

    def test_search_shards(self):
        c = BaseClient()
        c.search_shards(index='test', doc_type='test', cb=self.handle_cb)
        self.wait()

    def test_search_template(self):
        c = BaseClient()
        c.search_template(index='test', doc_type='test', cb=self.handle_cb)
        self.wait()

    def test_explain(self):
        c = BaseClient()
        c.explain('test', 'test', 'test123', cb=self.handle_cb)
        self.wait()

    def test_scroll(self):
        c = BaseClient()
        c.scroll('testscroll', cb=self.handle_cb)
        self.wait()

    def test_clear_scroll(self):
        c = BaseClient()
        c.clear_scroll('testscroll', cb=self.handle_cb)
        self.wait()

    def test_delete(self):
        c = BaseClient()
        c.delete('test', 'test', 'test123', cb=self.handle_cb)
        self.wait()

    def test_count(self):
        c = BaseClient()
        c.count(index='test', doc_type='test', cb=self.handle_cb)
        self.wait()

    def test_bulk(self):
        c = BaseClient()
        c.bulk(
                '{"bulk":"bulk1","id_":"bulk1"}', index='test', doc_type='test',
                cb=self.handle_cb
        )
        self.wait()

    def test_msearch(self):
        c = BaseClient()
        c.msearch(
                '{"bulk":"bulk1","id_":"bulk1"}', index='test', doc_type='test',
                cb=self.handle_cb
        )
        self.wait()

    def test_delete_by_query(self):
        c = BaseClient()
        c.delete_by_query(
                'test',
                body='{"bulk":"bulk1","id_":"bulk1"}', doc_type='test',
                cb=self.handle_cb
        )
        self.wait()

    def test_suggest(self):
        c = BaseClient()
        c.suggest(
                '{"bulk":"bulk1","id_":"bulk1"}', index='test',
                cb=self.handle_cb
        )
        self.wait()

    def test_percolate(self):
        c = BaseClient()
        c.percolate(
                'test',
                'test',
                body='{"bulk":"bulk1","id_":"bulk1"}',
                cb=self.handle_cb
        )
        self.wait()

    def test_mpercolate(self):
        c = BaseClient()
        c.mpercolate(
                '{"bulk":"bulk1","id_":"bulk1"}',
                index='test',
                doc_type='test',
                cb=self.handle_cb
        )
        self.wait()

    def test_count_percolate(self):
        c = BaseClient()
        c.count_percolate(
                'test',
                'test',
                cb=self.handle_cb
        )
        self.wait()

    def test_mlt(self):
        c = BaseClient()
        c.mlt(
                'index',
                'index',
                'bulk1',
                cb=self.handle_cb,
                **{"request_timeout":3}
        )
        self.wait()

    def test_termvector(self):
        c = BaseClient()
        c.termvector(
                'index',
                'index',
                'bulk1',
                cb=self.handle_cb,
                **{"request_timeout":3}
        )
        self.wait()

    def test_mtermvector(self):
        c = BaseClient()
        c.mtermvectors(
                index = 'index',
                doc_type = 'index',
                cb=self.handle_cb,
                **{"request_timeout":3}
        )
        self.wait()

    def test_benchmark(self):
        c = BaseClient()
        c.benchmark(
                index = 'index',
                doc_type = 'index',
                cb=self.handle_cb,
                **{"request_timeout":3}
        )
        self.wait()

    def test_abort_benchmark(self):
        c = BaseClient()
        c.abort_benchmark(
                name='test',
                cb=self.handle_cb,
        )
        self.wait()

    def test_list_benchmarks(self):
        c = BaseClient()
        c.list_benchmarks(
                index = 'test',
                cb=self.handle_cb,
                **{"request_timeout":3}
        )
        self.wait()

    def test_put_script(self):
        c = BaseClient()
        c.put_script(
                'python',
                'testscript123',
                "1+1",
                cb=self.handle_cb,
                **{"request_timeout":3}
        )
        self.wait()

    def test_get_script(self):
        c = BaseClient()
        c.get_script(
                'python',
                'testscript123',
                cb=self.handle_cb,
                **{"request_timeout":3}
        )
        self.wait()

    def test_delete_script(self):
        c = BaseClient()
        c.delete_script(
                'python',
                'testscript123',
                cb=self.handle_cb,
                **{"request_timeout":3}
        )
        self.wait()

    def test_put_template(self):
        c = BaseClient()
        c.put_template(
                'temp123',
                '{"template":"test123"}',
                cb=self.handle_cb,
                **{"request_timeout":3}
        )
        self.wait()

    def test_get_template(self):
        c = BaseClient()
        c.get_template(
                'temp123',
                cb=self.handle_cb,
                **{"request_timeout":3}
        )
        self.wait()

    def test_delete_template(self):
        c = BaseClient()
        c.delete_template(
                temp_id='temp123',
                cb=self.handle_cb,
                **{"request_timeout":3}
        )
        self.wait()
