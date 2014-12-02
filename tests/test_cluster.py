import tornado.ioloop
from   tornado.testing import AsyncTestCase
from   elasticsearch_tornado import ClusterClient
try:
    # python 2.6
    from unittest2 import TestCase, SkipTest
except ImportError:
    from unittest import TestCase, SkipTest


class ClusterClientTest(AsyncTestCase):

    def handle_cb(self, req):
        self.assertEqual(200, req.code)
        self.stop()

    def test_health(self):
        c = ClusterClient()
        c.health(cb=self.handle_cb)
        self.wait()

    def test_pending_tasks(self):
        c = ClusterClient()
        c.pending_tasks(cb=self.handle_cb)
        self.wait()

    def test_state(self):
        c = ClusterClient()
        c.state(cb=self.handle_cb)
        self.wait()

    def test_stats(self):
        c = ClusterClient()
        c.stats(cb=self.handle_cb)
        self.wait()

    def test_reroute(self):
        c = ClusterClient()
        c.reroute(
            body = '{}\n',
            cb=self.handle_cb
        )
        self.wait()

    def test_get_settings(self):
        c = ClusterClient()
        c.get_settings(cb=self.handle_cb)
        self.wait()

    def test_put_settings(self):
        c = ClusterClient()
        c.put_settings('{}\n', cb=self.handle_cb)
        self.wait()
