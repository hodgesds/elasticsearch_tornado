import tornado.ioloop
from   tornado.testing import AsyncTestCase
from   elasticsearch_tornado import NodesClient
try:
    # python 2.6
    from unittest2 import TestCase, SkipTest
except ImportError:
    from unittest import TestCase, SkipTest


class NodesClientTest(AsyncTestCase):

    def handle_cb(self, req):
        self.assertTrue(req.code in (200, 201, 400, 599,))
        self.stop()

    def test_info(self):
        c = NodesClient()
        c.info(cb=self.handle_cb)
        self.wait()

    def test_stats(self):
        c = NodesClient()
        c.stats(cb=self.handle_cb)
        self.wait()

    def test_hot_threads(self):
        c = NodesClient()
        c.hot_threads(cb=self.handle_cb)
        self.wait()
