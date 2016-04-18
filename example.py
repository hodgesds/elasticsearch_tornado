from __future__            import print_function
from elasticsearch_tornado import EsClient, serialize
from functools             import partial
from tornado               import ioloop, gen
import json


c = EsClient()


@gen.coroutine
def index(doc):
    p = partial(
       c.index_doc,
       'test_index',
       'test_doctype',
       serialize(doc),
    )
    res = yield gen.Task(p)
    raise gen.Return(res)


@gen.coroutine
def get(doc_id):
    p = partial(
       c.get_doc,
       'test_index',
        doc_id,
    )
    res = yield gen.Task(p)
    raise gen.Return(res)


@gen.coroutine
def main_coro():
    res = yield index({"user": "foo", "age": 100})
    doc_id = json.loads(res.body).get('_id', '')
    res = yield get(doc_id)
    print(res.body)


ioloop.IOLoop.instance().run_sync(main_coro)
