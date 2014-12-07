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

    def test_create(self):
        c = SnapshotClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404, 599]}
        )
        c.create('test', 'test', cb=h_cb)
        self.wait()

    def test_delete(self):
        c = SnapshotClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404, 599]}
        )
        c.delete('test', 'test', cb=h_cb)
        self.wait()

    def test_get(self):
        c = SnapshotClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404, 599]}
        )
        c.get('test', 'test', cb=h_cb)
        self.wait()

    def test_delete_repository(self):
        c = SnapshotClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404, 599]}
        )
        c.delete_repository('test', cb=h_cb)
        self.wait()

    def test_get_repository(self):
        c = SnapshotClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404, 599]}
        )
        c.get_repository(cb=h_cb)
        self.wait()

    def test_create_repository(self):
        c = SnapshotClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404, 599]}
        )
        c.create_repository('test', '{}', cb=h_cb)
        self.wait()

    def test_restore(self):
        c = SnapshotClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404, 599]}
        )
        c.restore('test', 'test', cb=h_cb)
        self.wait()

    def test_status(self):
        c = SnapshotClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404, 599]}
        )
        c.status(cb=h_cb)
        self.wait()

    def test_verify_repository(self):
        c = SnapshotClient()
        h_cb = partial(
            self.handle_cb,
            **{'codes':[400, 404, 599]}
        )
        c.verify_repository('test', cb=h_cb)
        self.wait()

