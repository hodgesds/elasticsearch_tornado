import tornado.ioloop
from   tornado.testing import AsyncTestCase
from   elasticsearch_tornado import NodesClient
try:
    # python 2.6
    from unittest2 import TestCase, SkipTest
except ImportError:
    from unittest import TestCase, SkipTest


class NodesClientTest(AsyncTestCase):

    def handle_cb(self, req, **kwargs):
        if kwargs.get('codes'):
            cl = [200, 201] + kwargs.get('codes')
            self.assertTrue(req.code in cl)
        else:
            self.assertTrue(req.code in (200, 201, ))
        self.stop()

    def test_info(self):
        c = NodesClient()
        c.info(callback=self.handle_cb)
        self.wait()

    def test_stats(self):
        c = NodesClient()
        c.node_stats(callback=self.handle_cb)
        self.wait()

    def test_hot_threads(self):
        c = NodesClient()
        c.node_hot_threads(callback=self.handle_cb)
        self.wait()
