from __future__            import print_function
from elasticsearch_tornado import EsClient
from functools             import partial
from tornado               import gen
from tornado               import ioloop
import sys


def et_cmd(subparsers):
    index_subparser = subparsers.add_parser('index')
    index_subparser.set_defaults(func=index)
    index_subparser.add_argument(
        '--file', '-f',
        default  = '-',
        help     = 'file: default STDIN',
    )


# index
@gen.coroutine
def index_coro(args):
    if args.file == '-':
        data_file = sys.stdin
    else:
        data_file = open(args.file, 'r')

    c = EsClient(host=args.host, port=args.port)
    data = '%s\n' % ''.join(data_file.readlines())
    s = yield gen.Task(c.bulk, data)
    print(s.body.rstrip('\n'))


def index(args):
    m = partial(index_coro, args)
    ioloop.IOLoop.current().run_sync(m)
