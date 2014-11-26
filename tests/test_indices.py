from elasticsearch_tornado import BaseClient
try:
    # python 2.6
    from unittest2 import TestCase, SkipTest
except ImportError:
    from unittest import TestCase, SkipTest


class BaseClientTest(TestCase):
    def test_mk_req(self):
        c = BaseClient()
        # making a req for async http client should work
        self.assertEquals(c.base_url, c.mk_req('').url)
        self.assertEquals('GET', c.mk_req('').method)
        # test making urls
        url = c.mk_url(*['a','b','c'], **{'key':'value'})
        print(url) 
        self.assertEquals('/a/b/c?key=value', url)
