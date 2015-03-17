import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Hello world!!")

class StoryHandler(tornado.web.RequestHandler):
	def get(self, story_id):
		self.write("Your requestd the story " + story_id)

class MyFormHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('<html><body><form action="/myform" method="post">'
				'<input type="text" name="message">'
				'<input type="submit" value="Submit">'
				'</form></body></html>')

	def post(self):
		self.set_header("Content-Type", "text/plain")
		self.write("You wrote " + self.get_argument("message"))

application = tornado.web.Application([
	(r"/", MyFormHandler),		
	(r"/myform", MyFormHandler),
	("r/story/([0-9]+)", StoryHandler),
	(r"/static/tornado-0.2.tar.gz", tornado.web.RedirectHandler,
	 dict(url = "https://github.com/downloads/facebook/tornado/tornado-0.2.tar.gz")),
])

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
