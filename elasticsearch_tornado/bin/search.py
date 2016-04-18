from __future__            import print_function
from elasticsearch_tornado import EsClient
from functools             import partial
from tornado               import gen
from tornado               import ioloop
import sys


def et_cmd(subparsers):
    search_subparser = subparsers.add_parser('search')
    search_subparser.set_defaults(func=search)
    search_subparser.add_argument(
        '--index', '-i',
        default  = None,
    )
    search_subparser.add_argument(
        '--type', '-t',
        dest     = 'doc_type',
        default  = None,
        help     = 'Doc type',
    )


# search
@gen.coroutine
def search_coro(args):
    c = EsClient(host=args.host, port=args.port)
    s = yield gen.Task(
        c.search,
        **{
            'index': args.index,
            'doc_type': args.doc_type,
        }
    )
    print(s.body.rstrip('\n'))


def search(args):
    m = partial(search_coro, args)
    ioloop.IOLoop.current().run_sync(m)
