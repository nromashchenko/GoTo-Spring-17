import os
import uuid

from bson import ObjectId
from pymongo import MongoClient

import tornado.ioloop
import tornado.web

client = MongoClient("CONNECTION STRING")
db = client["catreviews"]

def upload_photo(fileinfo):
    fname = fileinfo['filename']
    extn = os.path.splitext(fname)[1]
    cname = str(uuid.uuid4()) + extn
    fh = open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'images') + "/" + cname, 'wb')
    fh.write(fileinfo['body'])
    return 'images/' + cname

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cats = list(db['cats'].find())
        self.render("pages/list.html", cats=cats)

class AddHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("pages/add.html")

    def post(self):
        name = self.get_argument("name", "")
        text = self.get_argument("text", "")
        email = self.get_argument("email", "")
        sex = self.get_argument("sex", "")
        type = self.get_argument("type", "")
        path = upload_photo(self.request.files['photo'][0])
        comments = []

        cat = {
            "name": name,
            "email": email,
            "sex": sex,
            "photo": path,
            "text": text,
            "type": type,
            "comments": comments
        }

        db["cats"].insert_one(cat)

        self.redirect("/")

class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        id = self.get_argument("id")
        cat = db['cats'].find_one({'_id': ObjectId(id)})
        self.render("pages/about.html", cat=cat)
    def post(self):
        id = self.get_argument("id")
        cat = db['cats'].find_one({'_id': ObjectId(id)})

        name = self.get_argument("name", "")
        text = self.get_argument("text", "")

        comment = {
            "name": name,
            "text": text
        }

        cat["comments"].append(comment)
        db['cats'].update({'_id': ObjectId(id)}, cat)

        self.redirect("/about?id="+id)



settings = [
    (r"/", MainHandler),
    (r"/add",AddHandler),
    (r"/about",AboutHandler),
    (r'/images/(.*)', tornado.web.StaticFileHandler, {'path': os.path.join(os.path.dirname(os.path.realpath(__file__)),'images')})
]
app = tornado.web.Application(settings)
app.listen(1338)
tornado.ioloop.IOLoop.current().start()