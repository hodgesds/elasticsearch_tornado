import tornado.ioloop
from   tornado.testing import AsyncTestCase
from   elasticsearch_tornado import IndicesClient
try:
    # python 2.6
    from unittest2 import TestCase, SkipTest
except ImportError:
    from unittest import TestCase, SkipTest


class IndicesClientTest(TestCase):

    def handle_cb(self, req):
        self.assertEqual(200, req.code)
        self.stop()

    def test_analyze(self):
        c = IndicesClient()
        c.analyze(index='test', cb=self.handle_cb)
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
        c.create('test', cb=self.handle_cb)
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
        c.put_mapping('test', '{}', cb=self.handle_cb)
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
        c.put_alias('test', 'test', cb=self.handle_cb)
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
        c.update_aliases('{}', cb=self.handle_cb)
        self.wait()

    def test_delete_alias(self):
        c = IndicesClient()
        c.delete_alias('test', 'test', cb=self.handle_cb)
        self.wait()

    def test_put_template(self):
        c = IndicesClient()
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
        c.put_settings("", cb=self.handle_cb)
        self.wait()

    def test_put_warmer(self):
        c = IndicesClient()
        c.put_warmer("test", "", cb=self.handle_cb)
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

