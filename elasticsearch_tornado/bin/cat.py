from __future__            import print_function
from elasticsearch_tornado import EsClient
from functools             import partial
from tornado               import gen
from tornado               import ioloop
import os


def et_cmd(subparsers):
    cat_parser = subparsers.add_parser('cat')
    cat_subparser = cat_parser.add_subparsers()

    # sub sub parsers
    aliases_subparser(cat_subparser)
    allocation_subparser(cat_subparser)
    count_subparser(cat_subparser)
    health_subparser(cat_subparser)
    indices_subparser(cat_subparser)
    master_subparser(cat_subparser)
    nodes_subparser(cat_subparser)
    recovery_subparser(cat_subparser)
    shards_subparser(cat_subparser)
    segments_subparser(cat_subparser)
    pending_subparser(cat_subparser)
    thread_subparser(cat_subparser)
    field_subparser(cat_subparser)
    plugins_subparser(cat_subparser)


def aliases_subparser(subparsers):
    aliases_subparser = subparsers.add_parser('aliases')
    aliases_subparser.set_defaults(func=aliases)
    aliases_subparser.add_argument(
        '-n', '--name',
        default = None,
    )


def allocation_subparser(subparsers):
    allocation_subparser = subparsers.add_parser('allocation')
    allocation_subparser.set_defaults(func=allocation)
    allocation_subparser.add_argument(
        '-i', '--node-id',
        dest    = 'node_id',
        default = None,
        help    = 'Node Id',
    )


def count_subparser(subparsers):
    count_subparser = subparsers.add_parser('count')
    count_subparser.set_defaults(func=count)
    count_subparser.add_argument(
        '-i', '--index',
        default = None,
    )


def health_subparser(subparsers):
    health_subparser = subparsers.add_parser('health')
    health_subparser.set_defaults(func=health)


def indices_subparser(subparsers):
    indices_subparser = subparsers.add_parser('indices')
    indices_subparser.set_defaults(func=indices)
    indices_subparser.add_argument(
        '-i', '--index',
        default = None,
    )


def master_subparser(subparsers):
    master_subparser = subparsers.add_parser('master')
    master_subparser.set_defaults(func=master)


def nodes_subparser(subparsers):
    nodes_subparser = subparsers.add_parser('nodes')
    nodes_subparser.set_defaults(func=nodes)


def recovery_subparser(subparsers):
    recovery_subparser = subparsers.add_parser('recovery')
    recovery_subparser.set_defaults(func=recovery)
    recovery_subparser.add_argument(
        '-i', '--index',
        default = None,
    )


def shards_subparser(subparsers):
    shards_subparser = subparsers.add_parser('shards')
    shards_subparser.set_defaults(func=shards)
    shards_subparser.add_argument(
        '-i', '--index',
        default = None,
    )


def segments_subparser(subparsers):
    segments_subparser = subparsers.add_parser('segments')
    segments_subparser.set_defaults(func=segments)
    segments_subparser.add_argument(
        '-i', '--index',
        default = None,
    )


def pending_subparser(subparsers):
    pending_subparser = subparsers.add_parser('pending')
    pending_subparser.set_defaults(func=pending)


def thread_subparser(subparsers):
    thread_subparser = subparsers.add_parser('thread')
    thread_subparser.set_defaults(func=thread)


def field_subparser(subparsers):
    field_subparser = subparsers.add_parser('field')
    field_subparser.set_defaults(func=field)
    field_subparser.add_argument(
        '-f', '--field',
        default = None,
    )


def plugins_subparser(subparsers):
    plugins_subparser = subparsers.add_parser('plugins')
    plugins_subparser.set_defaults(func=plugins)


# aliases
@gen.coroutine
def aliases_coro(args):
    c = EsClient(host=args.host, port=args.port)
    s = yield gen.Task(c.aliases_cat, **{
        'name':   args.name,
        'params': {
            'v':True
            }
        })
    print(s.body.rstrip('\n'))


def aliases(args):
    m = partial(aliases_coro, args)
    ioloop.IOLoop.current().run_sync(m)


# allocation
@gen.coroutine
def allocation_coro(args):
    c = EsClient(host=args.host, port=args.port)
    s = yield gen.Task(c.allocation_cat, **{
        'node_id': args.node_id,
        'params':  {
            'v':True
            }
        })
    print(s.body.rstrip('\n'))


def allocation(args):
    m = partial(allocation_coro, args)
    ioloop.IOLoop.current().run_sync(m)


# count
@gen.coroutine
def count_coro(args):
    c = EsClient(host=args.host, port=args.port)
    s = yield gen.Task(c.count_cat, **{
        'index':  args.index,
        'params': {
            'v':True
            }
        })
    print(s.body.rstrip('\n'))


def count(args):
    m = partial(count_coro, args)
    ioloop.IOLoop.current().run_sync(m)


# health
@gen.coroutine
def health_coro(args):
    c = EsClient(host=args.host, port=args.port)
    s = yield gen.Task(c.health_cat, **{
        'params': {
            'v':True
            }
        })
    print(s.body.rstrip('\n'))


def health(args):
    m = partial(health_coro, args)
    ioloop.IOLoop.current().run_sync(m)


# indicies
@gen.coroutine
def indices_coro(args):
    c = EsClient(host=args.host, port=args.port)
    s = yield gen.Task(c.indices_cat, **{
        'index':  args.index,
        'params': {
            'v':True
            }
        })
    print(s.body.rstrip('\n'))


def indices(args):
    m = partial(indices_coro, args)
    ioloop.IOLoop.current().run_sync(m)


# master
@gen.coroutine
def master_coro(args):
    c = EsClient(host=args.host, port=args.port)
    s = yield gen.Task(c.master_cat, **{
        'params': {
            'v':True
            }
        })
    print(s.body.rstrip('\n'))


def master(args):
    m = partial(master_coro, args)
    ioloop.IOLoop.current().run_sync(m)


# nodes
@gen.coroutine
def nodes_coro(args):
    c = EsClient(host=args.host, port=args.port)
    s = yield gen.Task(c.nodes_cat, **{
        'params': {
            'v':True
            }
        })
    print(s.body.rstrip('\n'))


def nodes(args):
    m = partial(nodes_coro, args)
    ioloop.IOLoop.current().run_sync(m)


# recovery
@gen.coroutine
def recovery_coro(args):
    c = EsClient(host=args.host, port=args.port)
    s = yield gen.Task(c.recovery_cat, **{
        'index':  args.index,
        'params': {
            'v':True
            }
        })
    print(s.body.rstrip('\n'))


def recovery(args):
    m = partial(recovery_coro, args)
    ioloop.IOLoop.current().run_sync(m)


# shards
@gen.coroutine
def shards_coro(args):
    c = EsClient(host=args.host, port=args.port)
    s = yield gen.Task(c.shards_cat, **{
        'index':  args.index,
        'params': {
            'v':True
            }
        })
    print(s.body.rstrip('\n'))


def shards(args):
    m = partial(shards_coro, args)
    ioloop.IOLoop.current().run_sync(m)


# segments
@gen.coroutine
def segments_coro(args):
    c = EsClient(host=args.host, port=args.port)
    s = yield gen.Task(c.segments_cat, **{
        'index':  args.index,
        'fields': args.field,
        'params': {
            'v':True
            }
        })
    print(s.body.rstrip('\n'))


def segments(args):
    m = partial(segments_coro, args)
    ioloop.IOLoop.current().run_sync(m)


# pending
@gen.coroutine
def pending_coro(args):
    c = EsClient(host=args.host, port=args.port)
    s = yield gen.Task(c.pending_tasks_cat)
    print(s.body.rstrip('\n'))


def pending(args):
    m = partial(pending_coro, args)
    ioloop.IOLoop.current().run_sync(m)


# thread
@gen.coroutine
def thread_coro(args):
    c = EsClient(host=args.host, port=args.port)
    s = yield gen.Task(c.thread_pool_cat, **{
        'fields': args.field,
        'params': {
            'v':True
            }
        })
    print(s.body.rstrip('\n'))


def thread(args):
    m = partial(thread_coro, args)
    ioloop.IOLoop.current().run_sync(m)


# field
@gen.coroutine
def field_coro(args):
    c = EsClient(host=args.host, port=args.port)
    s = yield gen.Task(c.fielddata_cat, **{
        'fields': args.field,
        'params': {
            'v':True
            }
        })
    print(s.body.rstrip('\n'))


def field(args):
    m = partial(field_coro, args)
    ioloop.IOLoop.current().run_sync(m)


# plugins
@gen.coroutine
def plugins_coro(args):
    c = EsClient(host=args.host, port=args.port)
    s = yield gen.Task(c.plugins_cat, **{
        'params': {
            'v':True
            }
        })
    print(s.body.rstrip('\n'))


def plugins(args):
    m = partial(plugins_coro, args)
    ioloop.IOLoop.current().run_sync(m)
