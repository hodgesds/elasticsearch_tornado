from elasticsearch_tornado import EsClient
import tornado.ioloop


def ex_cb(req):
    print req
    ioloop = tornado.ioloop.IOLoop.instance()
    ioloop.stop()


io_loop = tornado.ioloop.IOLoop.instance()

c = EsClient()
# make an info request (same as http://localhost:9200)
c.info(cb=ex_cb)

io_loop.start()
