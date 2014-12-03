from os import environ, system, popen
from os.path import dirname, join, pardir, abspath, exists
import time


def start_es():
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
    time.sleep(6)

start_es()
