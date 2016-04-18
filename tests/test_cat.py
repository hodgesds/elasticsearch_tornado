import tornado.ioloop
from   tornado.testing import AsyncTestCase
from   elasticsearch_tornado import MeowClient
try:
    # python 2.6
    from unittest2 import TestCase, SkipTest
except ImportError:
    from unittest import TestCase, SkipTest


class MeowClientTest(AsyncTestCase):

    def handle_cb(self, req, **kwargs):
        if kwargs.get('codes'):
            cl = [200, 201] + kwargs.get('codes')
            self.assertTrue(req.code in cl)
        else:
            self.assertTrue(req.code in (200, 201, ))
        self.stop()

    def test_aliases(self):
        mc = MeowClient(io_loop=self.io_loop)
        mc.aliases_cat(callback=self.handle_cb)
        self.wait()

    def test_allocation(self):
        mc = MeowClient(io_loop=self.io_loop)
        mc.allocation_cat(callback=self.handle_cb)
        self.wait()

    def test_count(self):
        mc = MeowClient(io_loop=self.io_loop)
        mc.count_cat(callback=self.handle_cb)
        self.wait()

    def test_health(self):
        mc = MeowClient(io_loop=self.io_loop)
        mc.health_cat(callback=self.handle_cb)
        self.wait()

    def test_help(self):
        mc = MeowClient(io_loop=self.io_loop)
        mc.help_cat(callback=self.handle_cb)
        self.wait()

    def test_indices(self):
        mc = MeowClient(io_loop=self.io_loop)
        mc.indices_cat(callback=self.handle_cb)
        self.wait()

    def test_master(self):
        mc = MeowClient(io_loop=self.io_loop)
        mc.master_cat(callback=self.handle_cb)
        self.wait()

    def test_nodes(self):
        mc = MeowClient(io_loop=self.io_loop)
        mc.nodes_cat(callback=self.handle_cb)
        self.wait()

    def test_recovery(self):
        mc = MeowClient(io_loop=self.io_loop)
        mc.recovery_cat(callback=self.handle_cb)
        self.wait()

    def test_shards(self):
        mc = MeowClient(io_loop=self.io_loop)
        mc.shards_cat(callback=self.handle_cb)
        self.wait()

    @SkipTest
    def test_segments(self):
        mc = MeowClient(io_loop=self.io_loop)
        mc.segments_cat(callback=self.handle_cb)
        self.wait()

    def test_pending_tasks(self):
        mc = MeowClient(io_loop=self.io_loop)
        mc.pending_tasks_cat(callback=self.handle_cb)
        self.wait()

    def test_thread_pool(self):
        mc = MeowClient(io_loop=self.io_loop)
        mc.thread_pool_cat(callback=self.handle_cb)
        self.wait()

    def test_fielddata(self):
        mc = MeowClient(io_loop=self.io_loop)
        mc.fielddata_cat(callback=self.handle_cb)
        self.wait()

    def test_plugins(self):
        mc = MeowClient(io_loop=self.io_loop)
        mc.plugins_cat(callback=self.handle_cb)
        self.wait()
