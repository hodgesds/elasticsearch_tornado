from   functools import partial
import tornado.ioloop
from   tornado.testing import AsyncTestCase
from   tornado.stack_context import ExceptionStackContext
from   elasticsearch_tornado import SnapshotClient
try:
    # python 2.6
    from unittest2 import TestCase, SkipTest
except ImportError:
    from unittest import TestCase, SkipTest


def handle_exc(*args):
    print('Exception occured')
    return True

class SnapshotClientTest(AsyncTestCase):

    def handle_cb(self, req, **kwargs):
        if kwargs.get('codes'):
            cl = [200, 201] + kwargs.get('codes')
            self.assertTrue(req.code in cl)
        else:
            self.assertTrue(req.code in (200, 201, ))
        self.stop()

    def test_create_snapshot(self):
        c = SnapshotClient()
        body = """
        {
            "type": "fs",
            "settings": {
                "location": "/tmp/test",
                "compress": true
            }
        }

        """
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404]}
        )
        c.create_snapshot('test', 'test', body, callback=h_cb)
        self.wait()

    def test_delete_snapshot(self):
        c = SnapshotClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404]}
        )
        c.delete_snapshot('test', 'test', callback=h_cb)
        self.wait()

    def test_get(self):
        c = SnapshotClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404]}
        )
        c.get_snapshot('test', 'test', callback=h_cb)
        self.wait()

    def test_delete_repository(self):
        c = SnapshotClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404]}
        )
        c.delete_repository('test', callback=h_cb)
        self.wait()

    def test_get_repository(self):
        c = SnapshotClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404]}
        )
        c.get_repository(callback=h_cb)
        self.wait()

    def test_create_repository(self):
        c = SnapshotClient()
        body = """
        {
            "type": "fs",
            "settings": {
                "location": "/tmp/test",
            }
        }

        """
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404]}
        )
        c.create_repository('test', body, callback=h_cb)
        self.wait()

    def test_restore_snapshot(self):
        c = SnapshotClient()
        body = """
        '{
           "indices": "index_1,index_2",
           "ignore_unavailable": "true",
           "include_global_state": false,
           "rename_pattern": "index_(.+)",
           "rename_replacement": "restored_index_$1"
        }

        """
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404]}
        )
        c.restore_snapshot('test', 'test', body, callback=h_cb)
        self.wait()

    def test_snapshot_status(self):
        c = SnapshotClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404]}
        )
        c.snapshot_status(callback=h_cb)
        self.wait()

    def test_verify_repository(self):
        c = SnapshotClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404]}
        )
        c.verify_repository('test', callback=h_cb)
        self.wait()

