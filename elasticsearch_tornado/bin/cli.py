from pkgutil import iter_modules
import argparse
import importlib
import os
import sys


def find_subcommands(subparsers):
    for _, mod_name, is_pkg in iter_modules([os.path.dirname(__file__)]):
        if not is_pkg and mod_name not in [sys.modules, 'cli']:
            mod_fullname = 'elasticsearch_tornado.bin.{}'.format(mod_name)
            module = importlib.import_module(mod_fullname)
            if hasattr(module, 'et_cmd'):
                module.et_cmd(subparsers)


def main():
    parser = argparse.ArgumentParser(
        prog = "et",
        description = "ET: Command line utilities for Elasticsearch",
    )

    parser.add_argument(
        '--host',
        default = os.environ.get('ET_HOST','localhost'),
        help    = 'Elasticsearch server: ET_HOST',
    )

    parser.add_argument(
        '-p', '--port',
        default = os.environ.get('ET_PORT', 9200),
        type    = int,
        help    = 'Elasticsearch server: ET_PORT',
    )

    subparsers = parser.add_subparsers()

    find_subcommands(subparsers)

    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
