import tornado.ioloop
from   functools import partial
from   tornado.testing import AsyncTestCase
from   elasticsearch_tornado import IndicesClient
try:
    # python 2.6
    from unittest2 import TestCase, SkipTest
except ImportError:
    from unittest import TestCase, SkipTest


class IndicesClientTest(AsyncTestCase):

    def handle_cb(self, req, **kwargs):
        if kwargs.get('codes'):
            cl = [200, 201] + kwargs.get('codes')
            self.assertTrue(req.code in cl)
        else:
            self.assertTrue(req.code in (200, 201, ))
        self.stop()

    def test_analyze(self):
        c = IndicesClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404]}
        )
        c.analyze(index='test', cb=h_cb)
        self.wait()

    def test_refresh(self):
        c = IndicesClient()
        c.refresh(index='test', cb=self.handle_cb)
        self.wait()

    def test_flush(self):
        c = IndicesClient()
        c.flush(index='test', cb=self.handle_cb)
        self.wait()

    def test_create(self):
        c = IndicesClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404]}
        )
        body = """
        {
            "settings" : {
                "index" : {
                    "number_of_shards" : 3,
                    "number_of_replicas" : 2
                }
            }
        }

        """
        c.create('test', body, cb=self.handle_cb)
        self.wait()

    def test_get(self):
        c = IndicesClient()
        c.get('test', cb=self.handle_cb)
        self.wait()

    def test_open(self):
        c = IndicesClient()
        c.open('test', cb=self.handle_cb)
        self.wait()

    def test_close(self):
        c = IndicesClient()
        c.close('test', cb=self.handle_cb)
        self.wait()

    def test_delete(self):
        c = IndicesClient()
        c.delete('test', cb=self.handle_cb)
        self.wait()

    def test_exists(self):
        c = IndicesClient()
        c.exists('test', cb=self.handle_cb)
        self.wait()

    def test_exists_type(self):
        c = IndicesClient()
        c.exists_type('test', 'type', cb=self.handle_cb)
        self.wait()

    def test_put_mapping(self):
        c = IndicesClient()
        body = """
        {
            "tweet" : {
                "properties" : {
                    "message" : {"type" : "string", "store" : true }
                }
            }
        }

        """
        c.put_mapping('test', body, cb=self.handle_cb)
        self.wait()

    def test_get_mapping(self):
        c = IndicesClient()
        c.get_mapping(index='test', cb=self.handle_cb)
        self.wait()

    def test_get_field_mapping(self):
        c = IndicesClient()
        c.get_field_mapping('test', index='test', cb=self.handle_cb)
        self.wait()

    def test_delete_mapping(self):
        c = IndicesClient()
        c.delete_mapping('test', 'test', cb=self.handle_cb)
        self.wait()

    def test_put_alias(self):
        c = IndicesClient()
        body = """
        {
            "actions" : [
                { "add" : { "index" : "test1", "alias" : "alias1" } }
            ]
        }

        """
        c.put_alias('test', 'test', body, cb=self.handle_cb)
        self.wait()

    def test_exists_alias(self):
        c = IndicesClient()
        c.exists_alias('test', index='test', cb=self.handle_cb)
        self.wait()

    def test_get_alias(self):
        c = IndicesClient()
        c.get_alias(index='test', cb=self.handle_cb)
        self.wait()

    def test_get_aliases(self):
        c = IndicesClient()
        c.get_aliases(index='test', cb=self.handle_cb)
        self.wait()

    def test_update_aliases(self):
        c = IndicesClient()
        body = """
        {
            "actions" : [
                { "add" : { "index" : "test1", "alias" : "alias1" } },
                { "add" : { "index" : "test2", "alias" : "alias1" } }
            ]
        }

        """
        c.update_aliases(body, cb=self.handle_cb)
        self.wait()

    def test_delete_alias(self):
        c = IndicesClient()
        c.delete_alias('test', 'test', cb=self.handle_cb)
        self.wait()

    def test_put_template(self):
        c = IndicesClient()
        body = """
        {
            "template" : "te*",
            "settings" : {
                "number_of_shards" : 1
            },
            "mappings" : {
                "type1" : {
                    "_source" : { "enabled" : false }
                }
            }
        }

        """
        c.put_template('test', '{}', cb=self.handle_cb)
        self.wait()

    def test_exists_template(self):
        c = IndicesClient()
        c.exists_template('test', cb=self.handle_cb)
        self.wait()

    def test_get_template(self):
        c = IndicesClient()
        c.get_template(name='test', cb=self.handle_cb)
        self.wait()

    def test_delete_template(self):
        c = IndicesClient()
        c.delete_template('test', cb=self.handle_cb)
        self.wait()

    def test_get_settings(self):
        c = IndicesClient()
        c.get_settings(cb=self.handle_cb)
        self.wait()

    def test_put_settings(self):
        c = IndicesClient()
        body = """
        {
            "index" : {
                "number_of_replicas" : 1
            }
        }

        """
        c.put_settings(body, cb=self.handle_cb)
        self.wait()

    def test_put_warmer(self):
        c = IndicesClient()
        body = """
        {
            "query" : {
                "match_all" : {}
            },
            "aggs" : {
                "aggs_1" : {
                    "terms" : {
                        "field" : "field"
                    }
                }
            }
        }

        """
        c.put_warmer("test", body, cb=self.handle_cb)
        self.wait()

    def test_get_warmer(self):
        c = IndicesClient()
        c.get_warmer(cb=self.handle_cb)
        self.wait()

    def test_delete_warmer(self):
        c = IndicesClient()
        c.delete_warmer('test', 'test', cb=self.handle_cb)
        self.wait()

    def test_status(self):
        c = IndicesClient()
        c.status(cb=self.handle_cb)
        self.wait()

    def test_stats(self):
        c = IndicesClient()
        c.stats(cb=self.handle_cb)
        self.wait()

    def test_segments(self):
        c = IndicesClient()
        c.segments(cb=self.handle_cb)
        self.wait()

    def test_optimize(self):
        c = IndicesClient()
        c.optimize(cb=self.handle_cb)
        self.wait()

    def test_validate_query(self):
        c = IndicesClient()
        c.validate_query(cb=self.handle_cb)
        self.wait()

    def test_clear_cache(self):
        c = IndicesClient()
        c.clear_cache(cb=self.handle_cb)
        self.wait()

    def test_recovery(self):
        c = IndicesClient()
        c.recovery(cb=self.handle_cb)
        self.wait()

    def test_snapshot_index(self):
        c = IndicesClient()
        c.snapshot_index(cb=self.handle_cb)
        self.wait()

