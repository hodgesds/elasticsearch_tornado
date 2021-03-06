import unittest
import tornado.ioloop
from   functools import partial
from   tornado.testing import AsyncTestCase
from   tornado.stack_context import ExceptionStackContext
from   elasticsearch_tornado import BaseClient
try:
    # python 2.6
    from unittest2 import TestCase, SkipTest
except ImportError:
    from unittest import TestCase, SkipTest


def handle_exc(*args):
    print('Exception occured')
    return True


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

    def handle_cb(self, req, **kwargs):
        if kwargs.get('codes'):
            cl = [200, 201] + kwargs.get('codes')
            self.assertTrue(req.code in cl)
        else:
            self.assertTrue(req.code in (200, 201, ))
        self.stop()

    def test_ping(self):
        c = BaseClient()
        c.ping(callback=self.handle_cb)
        self.wait()

    def test_info(self):
        c = BaseClient()
        c.info(callback=self.handle_cb)
        self.wait()

    def test_index_doc(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 403, 404]}
        )
        c.index_doc('test', 'test', '{"test":"123"}', doc_id='test123',
                callback=h_cb)
        self.wait()

    def test_doc_exists(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 403, 404]}
        )
        c.doc_exists('test', 'test123', callback=h_cb)
        self.wait()

    def test_get_doc(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 403, 404]}
        )
        c.get_doc('test', 'test123', callback=h_cb)
        self.wait()

    def test_get_source(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 403, 404]}
        )
        c.get_source('test', 'test123', callback=h_cb)
        self.wait()

    def test_mget(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404, 500]}
        )
        body = '''
        {
          "docs" : [
          {
          "_index" : "test",
          "_type" : "type",
          "_id" : "1"
          },
          {
          "_index" : "test",
          "_type" : "type",
          "_id" : "2"
          }
        ]
        }
        '''
        c.mget(body, index='test', doc_type='test', callback=h_cb)
        self.wait()

    def test_update_doc(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404, 403,]}
        )
        body = """
        {
            "script" : "ctx._source.counter += count",
            "params" : {
                "count" : 4
            }
        }

        """
        c.update_doc('test', 'test', 'test123', body=body, callback=h_cb)
        self.wait()

    def test_search(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404, 403,]}
        )
        c.search(index='test', doc_type='test', callback=h_cb)
        self.wait()

    def test_search_shards(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404, 403,]}
        )
        c.search_shards(index='test', doc_type='test', callback=h_cb)
        self.wait()

    def test_search_template(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404, 403,]}
        )
        c.search_template(index='test', doc_type='test', callback=h_cb)
        self.wait()

    def test_explain(self):
        c = BaseClient()
        body = """
        {
            "query" : {
                "term" : { "message" : "search" }
            }
        }

        """
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 401, 403, 404]}
        )
        c.explain('test', 'test', 'test123', body=body, callback=h_cb)
        self.wait()

    def test_scroll(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 403, 404]}
        )
        c.scroll('test', callback=h_cb)
        self.wait()

    def test_clear_scroll(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 403, 404]}
        )
        c.clear_scroll('aaaaa', callback=h_cb)
        self.wait()

    def test_delete_doc(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 403, 404]}
        )
        c.delete_doc(
            'test',
            'test',
            'test123',
            callback=h_cb
        )
        self.wait()

    def test_doc_count(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[403, 404]}
        )
        c.doc_count(
            body     = '',
            index    = 'test',
            doc_type = 'test',
            callback=h_cb
        )
        self.wait()

    def test_bulk(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404]}
        )
        body = """
        { "index" : { "_index" : "test", "_type" : "type1", "_id" : "1" } }
        { "field1" : "value1" }

        """
        c.bulk(
            body,
            index    = 'test',
            doc_type = 'test',
            callback=h_cb
        )
        self.wait()

    def test_msearch(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404]}
        )
        c.msearch(
            None,
            index='test',
            doc_type='test',
            callback=h_cb
        )
        self.wait()

    def test_delete_by_query(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 403, 404]}
        )
        p = {}
        p['source'] = '{ "query": { "match_all": {} } }\n'
        c.delete_by_query(
            'test',
            body='{ "query": { "match_all": {} } }\n',
            doc_type='test',
            params=p,
            callback=h_cb
        )
        self.wait()

    def test_suggest(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 403, 404]}
        )
        body = """
        {
            "my-suggestion" : {
                "text" : "the amsterdma meetpu",
                "term" : {
                    "field" : "body"
                }
            }
        }

        """
        c.suggest(
            body,
            index    = 'test',
            callback = h_cb
        )
        self.wait()

    def test_percolate(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 403, 404]}
        )
        c.percolate(
            'test',
            'test',
            body=None,
            callback=h_cb
        )
        self.wait()

    def test_mpercolate(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 403, 404]}
        )
        c.mpercolate(
            None,
            index='test',
            doc_type='test',
            callback=h_cb
        )
        self.wait()

    def test_count_percolate(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[403, 404]}
        )
        c.count_percolate(
            'test',
            'test',
            callback=h_cb
        )
        self.wait()

    def test_mlt(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404]}
        )
        c.mlt(
            'index',
            'index',
            'bulk1',
            callback=h_cb,
        )
        self.wait()

    def test_termvector(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[500, 404]}
        )
        body = """
        {
            "fields" : ["text", "some_field_without_term_vectors"],
                "offsets" : true,
                "positions" : true,
                "term_statistics" : true,
                "field_statistics" : true
        }

        """
        c.termvector(
            'index',
            'test',
            'test123',
            body=body,
            callback=h_cb,
        )
        self.wait()

    def test_mtermvector(self):
        c = BaseClient()
        body = """
        {
            "docs": [
                {
                    "_index": "testidx",
                    "_type": "test",
                    "_id": "2",
                    "term_statistics": true
                },
                {
                   "_index": "testidx",
                   "_type": "test",
                   "_id": "1",
                   "fields": [
                       "text"
                   ]
                }
            ]
        }

        """
        c.mtermvectors(
            index = 'index',
            doc_type = 'index',
            body = body,
            callback=self.handle_cb,
        )
        self.wait()

    def test_benchmark(self):
        c = BaseClient()
        body = '''{
            "name": "my_benchmark",
            "competitors": [ {
                "name": "my_competitor",
                "requests": [ {
                    "query": {
                        "match": { "_all": "a*" }
                    }
                } ]
             } ]
        }

        '''
        c.benchmark(
            body     = body,
            index    = 'index',
            doc_type = 'index',
            callback = self.handle_cb,
        )
        self.wait()

    @SkipTest
    def test_abort_benchmark(self):
        c = BaseClient()
        c.abort_benchmark(
            name = 'test',
            callback = self.handle_cb,
        )
        self.wait()

    @SkipTest
    def test_list_benchmarks(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404]}
        )
        c.list_benchmarks(
            index = 'test',
            callback=h_cb,
        )
        self.wait()

    def test_put_script(self):
        c = BaseClient()
        body = """
        {
            "query": {
                "function_score": {
                    "query": {
                        "match": {
                             "body": "foo"
                        }
                     },
                    "functions": [
                    {
                        "script_score": {
                            "script": "calculate-score",
                            "params": {
                                "my_modifier": 8
                            }
                        }
                    }
                    ]
                }
            }
        }

        """
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404]}
        )
        c.put_script(
            'native',
            'testscript123',
            body,
            callback = h_cb,
        )
        self.wait()

    def test_get_script(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[404]}
        )
        c.get_script(
            'native',
            'testscript123',
            callback = h_cb,
        )
        self.wait()

    def test_delete_script(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[404]}
        )
        c.delete_script(
            'native',
            'testscript123',
            callback = h_cb,
        )
        self.wait()

    def test_put_template(self):
        c = BaseClient()
        c.put_template(
            'temp123',
            '{"template":"test123"}',
            callback = self.handle_cb,
        )
        self.wait()

    def test_get_template(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[404]}
        )
        c.get_template(
            'temp123',
            callback = h_cb,
        )
        self.wait()

    def test_delete_template(self):
        c = BaseClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[404]}
        )
        c.delete_template(
            temp_id='temp123',
            callback = h_cb,
        )
        self.wait()
