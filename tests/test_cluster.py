import tornado.ioloop
from   functools import partial
from   tornado.testing import AsyncTestCase
from   elasticsearch_tornado import ClusterClient
try:
    # python 2.6
    from unittest2 import TestCase, SkipTest
except ImportError:
    from unittest import TestCase, SkipTest


class ClusterClientTest(AsyncTestCase):

    def handle_cb(self, req, **kwargs):
        if kwargs.get('codes'):
            cl = [200, 201] + kwargs.get('codes')
            self.assertTrue(req.code in cl)
        else:
            self.assertTrue(req.code in (200, 201, ))
        self.stop()

    def test_health(self):
        c = ClusterClient()
        c.cluster_health(callback=self.handle_cb)
        self.wait()

    def test_pending_tasks(self):
        c = ClusterClient()
        c.cluster_pending_tasks(callback=self.handle_cb)
        self.wait()

    def test_state(self):
        c = ClusterClient()
        c.cluster_state(callback=self.handle_cb)
        self.wait()

    def test_stats(self):
        c = ClusterClient()
        c.cluster_stats(callback=self.handle_cb)
        self.wait()

    def test_reroute(self):
        c = ClusterClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404]}
        )
        body = """
        {
            "commands" : [ {
                "move" :
                    {
                        "index" : "test", "shard" : 0,
                        "from_node" : "node1", "to_node" : "node2"
                    }
                },
                {
                    "allocate" : {
                        "index" : "test", "shard" : 1, "node" : "node3"
                    }
                }
                ]
        }

        """
        c.cluster_reroute(body, callback=h_cb)
        self.wait()

    def test_get_settings(self):
        c = ClusterClient()
        c.cluster_get_settings(callback=self.handle_cb)
        self.wait()

    def test_put_settings(self):
        c = ClusterClient()
        body = """
        {
            "persistent" : {
                "discovery.zen.minimum_master_nodes" : 1
            }
        }

        """
        c.cluster_put_settings(body, callback=self.handle_cb)
        self.wait()
