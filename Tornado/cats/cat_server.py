import random

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cats = [
            {"image": "images/1.jpg", "name": "Шаурма"},
            {"image": "images/2.jpg", "name": "Пуля"},
            {"image": "images/3.jpeg", "name": "Кама"},
            {"image": "images/4.jpg", "name": "Ежжи"},
            {"image": "images/5.jpg", "name": "Барсик"},
        ]
        catOfTheDay = random.choice(cats)
        self.render("page.html", cat=catOfTheDay)


settings = [
    (r"/", MainHandler),
    (r'/images/(.*)', tornado.web.StaticFileHandler, {'path': 'images'})
]
app = tornado.web.Application(settings)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()
