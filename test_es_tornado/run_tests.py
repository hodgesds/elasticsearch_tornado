#!/usr/bin/env python
from __future__ import print_function

import sys
from os import environ
from os.path import dirname, join, pardir, abspath, exists
import subprocess

import nose


def fetch_es_repo():
    # fetch new commits to be sure...
    print('Fetching elasticsearch repo...')
    subprocess.check_call('cd %s && git fetch https://github.com/elasticsearch/elasticsearch.git' % repo_path, shell=True)
    # reset to the version fron info()
    subprocess.check_call('cd %s && git reset --hard %s' % (repo_path, sha), shell=True)


def run_all(argv=None):
    sys.exitfunc = lambda: sys.stderr.write('Shutting down....\n')

    # fetch elasticsearch 
    fetch_es_repo()

    # always insert coverage when running tests
    if argv is None:
        argv = [
            'nosetests', '--with-xunit',
            '--with-xcoverage', '--cover-package=elasticsearch', '--cover-erase',
            '--logging-filter=elasticsearch', '--logging-level=DEBUG',
            '--verbose',
        ]

    nose.run_exit(
        argv=argv,
        defaultTest=abspath(dirname(__file__))
    )

if __name__ == '__main__':
    run_all(sys.argv)

