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

    def test_create(self):
        c = SnapshotClient()
        c.create('test', 'test', cb=self.handle_cb)
        self.wait()

    def test_delete(self):
        c = SnapshotClient()
        c.delete('test', 'test', cb=self.handle_cb)
        self.wait()

    def test_get(self):
        c = SnapshotClient()
        c.get('test', 'test', cb=self.handle_cb)
        self.wait()

    def test_delete_repository(self):
        c = SnapshotClient()
        c.delete_repository('test', cb=self.handle_cb)
        self.wait()

    def test_get_repository(self):
        c = SnapshotClient()
        c.get_repository(cb=self.handle_cb)
        self.wait()

    def test_create_repository(self):
        c = SnapshotClient()
        c.create_repository('test', '{}', cb=self.handle_cb)
        self.wait()

    def test_restore(self):
        c = SnapshotClient()
        c.restore('test', 'test', cb=self.handle_cb)
        self.wait()

    def test_status(self):
        c = SnapshotClient()
        c.status(cb=self.handle_cb)
        self.wait()

    def test_verify_repository(self):
        c = SnapshotClient()
        c.verify_repository('test', cb=self.handle_cb)
        self.wait()

