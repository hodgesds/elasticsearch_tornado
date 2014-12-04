#!/usr/bin/env python
from __future__ import print_function
import sys
import tempfile
import time
from   os import environ, system, popen
from   os.path import dirname, join, pardir, abspath, exists
import subprocess

import nose


def run_all(argv=None):
    sys.exitfunc = lambda: sys.stderr.write('Shutting down....\n')

    # fetch elasticsearch 
    # always insert coverage when running tests
    if argv is None:
        argv = [
            'nosetests', '--with-xunit',
            '--with-xcoverage', '--cover-package=elasticsearch_tornado',
            '--cover-erase', '--logging-filter=elasticsearch',
            '--logging-level=DEBUG', '--verbose',
        ]

    nose.run_exit(
        argv=argv,
        defaultTest=abspath(dirname(__file__))
    )

if __name__ == '__main__':
    run_all(sys.argv)

