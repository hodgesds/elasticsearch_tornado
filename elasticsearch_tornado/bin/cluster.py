from __future__            import print_function
from elasticsearch_tornado import EsClient
from functools             import partial
from tornado               import gen
from tornado               import ioloop
import os


def et_cmd(subparsers):
    cluster_parser = subparsers.add_parser('cluster')
    cluster_subparser = cluster_parser.add_subparsers()

    # sub sub parsers
    health_subparser(cluster_subparser)
    state_subparser(cluster_subparser)
    stats_subparser(cluster_subparser)


def health_subparser(subparsers):
    health_subparser = subparsers.add_parser('health')
    health_subparser.set_defaults(func=health)
    health_subparser.add_argument(
        '-i', '--index',
        default = None,
        help    = 'Index health',
    )


def state_subparser(subparsers):
    state_subparser = subparsers.add_parser('state')
    state_subparser.set_defaults(func=state)
    state_subparser.add_argument(
        '-i', '--index',
        default = None,
        help    = 'Index',
    )
    state_subparser.add_argument(
        '-m', '--metric',
        default = None,
        help    = 'Index',
        choices = [ '_all', 'blocks', 'index_templates',
            'metadata', 'nodes', 'routing_table', 'master_node',
            'version' ]
    )


def stats_subparser(subparsers):
    stats_subparser = subparsers.add_parser('stats')
    stats_subparser.set_defaults(func=stats)
    stats_subparser.add_argument(
        '-i', '--node-id',
        default = None,
        help    = 'Node Id',
    )


# health
@gen.coroutine
def health_coro(args):
    c = EsClient(host=args.host, port=args.port)
    s = yield gen.Task(c.health)
    print(s.body.rstrip('\n'))


def health(args):
    m = partial(health_coro, args)
    ioloop.IOLoop.current().run_sync(m)

# state
@gen.coroutine
def state_coro(args):
    c = EsClient(host=args.host, port=args.port)
    s = yield gen.Task(c.state, **{'metric': args.metric, 'index':
        args.index})
    print(s.body.rstrip('\n'))


def state(args):
    m = partial(state_coro, args)
    ioloop.IOLoop.current().run_sync(m)


# stats
@gen.coroutine
def stats_coro(args):
    c = EsClient(host=args.host, port=args.port)
    s = yield gen.Task(c.stats, **{'node_id': args.node_id})
    print(s.body.rstrip('\n'))


def stats(args):
    m = partial(stats_coro, args)
    ioloop.IOLoop.current().run_sync(m)
