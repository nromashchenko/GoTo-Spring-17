import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class PageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("roctbb.html")

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("name", "world")
        self.write("Hello, {0}!".format(name))


settings = [
    (r"/", MainHandler),
    (r"/page",PageHandler),
    (r"/hello",HelloHandler),
]
app = tornado.web.Application(settings)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()