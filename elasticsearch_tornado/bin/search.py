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
        action   = 'append',
        default  = None,
    )
    search_subparser.add_argument(
        '--type', '-t',
        action   = 'append',
        dest     = 'doc_type',
        default  = None,
        help     = 'Doc type',
    )
    search_subparser.add_argument(
        '--analyzer', '-a',
        default  = None,
        help     = 'Analyzer',
    )
    search_subparser.add_argument(
        '--body', '-b',
        default  = None,
        help     = 'Query DSL request body',
    )
    search_subparser.add_argument(
        '--default-opterator', '-o',
        dest     = 'operator',
        default  = None,
    )
    search_subparser.add_argument(
        '--exclude', '-e',
        action   = 'append',
        default  = None,
        help     = 'fields to exclude',
    )
    search_subparser.add_argument(
        '--explain', '-x',
        default  = False,
        action   = 'store_true',
        help     = 'explain query',
    )
    search_subparser.add_argument(
        '--fields', '-f',
        action   = 'append',
        default  = None,
    )
    search_subparser.add_argument(
        '--from',
        dest     = 'start',
        default  = 0,
        type     = int,
        help     = 'Starting offset',
    )
    search_subparser.add_argument(
        '--size', '-s',
        default  = 10,
        type     = int,
        help     = 'Page size',
    )
    search_subparser.add_argument(
        '--query', '-q',
        default  = None,
    )


# search
@gen.coroutine
def search_coro(args):
    c = EsClient(host=args.host, port=args.port)

    doc_type = ','.join(args.doc_type) if args.doc_type else None
    exclude  = ','.join(args.exclude) if args.exclude else None
    explain  = '_explain' if args.explain else None
    fields   = ','.join(args.fields) if args.fields else None
    index    = ','.join(args.index) if args.index else None

    s = yield gen.Task(
        c.search,
        **{
            'params': {
                'default_operator': args.operator,
                'doc_type':        args.doc_type,
                'explain':         explain,
                'from':            args.start,
                'index':           args.index,
                'q':               args.query,
                'size':            args.size,
                '_source_exclude': args.exclude,
                '_source_include': fields,
            }
        }
    )
    print(s.body.rstrip('\n'))


def search(args):
    m = partial(search_coro, args)
    ioloop.IOLoop.current().run_sync(m)
