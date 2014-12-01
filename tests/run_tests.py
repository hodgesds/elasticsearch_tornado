#!/usr/bin/env python
from __future__ import print_function
import sys
import tempfile
from   os import environ, system, popen
from   os.path import dirname, join, pardir, abspath, exists
import subprocess

import nose


def fetch_es_repo():
    # fetch new commits to be sure...
    td = abspath(join(dirname(__file__), 'test_elasticsearch'))
    system('rm -rf %s' % td)
    system('mkdir -p %s' % td)
    #subprocess.check_call('cd %s && git clone https://github.com/elasticsearch/elasticsearch.git' % td, shell=True)
    system('cd %s; wget http://s3-eu-west-1.amazonaws.com/build-eu.elasticsearch.org/origin/master/nightly/JDK7/elasticsearch-latest-SNAPSHOT.tar.gz; tar xvf elasticsearch*' % td)
    #subprocess.check_call('cd %s; wget http://s3-eu-west-1.amazonaws.com/build-eu.elasticsearch.org/origin/master/nightly/JDK7/elasticsearch-latest-SNAPSHOT.tar.gz | tar xz --directory=%s/tmp --strip-components=1' % (td, td,))
    #subprocess.check_call('cd %s && git clone https://github.com/elasticsearch/elasticsearch.git' % td, shell=True)
    f = [x for x in popen("ls %s" % td).readlines() if '.gz' not in x][0]
    el_dir = f.replace('\n','')
    system('sh %s/%s/bin/elasticsearch &' % (td, el_dir,))
    return td


def run_all(argv=None):
    sys.exitfunc = lambda: sys.stderr.write('Shutting down....\n')

    # fetch elasticsearch 
    td = fetch_es_repo()
    print('running tests')
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

