import torndb
import tornado.ioloop
import tornado.web
import tornado.gen
import tornado.httpclient

database = torndb.Connection('localhost', 'share_theme', user='root', password='')

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		print(database.execute('show tables'))
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

class GetFullPageAsyncHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		http_client = tornado.httpclient.AsyncHTTPClient()
		http_response = yield http_client.fetch("http://www.drdobbs.com/web-development")
		response = http_response.body.decode().replace("Most Recent Premium Content", "Most Recent Content")
		self.write(response)
		self.set_header("Content-Type", "text/html")


application = tornado.web.Application([
	(r"/", MainHandler),		
	(r"/myform", MyFormHandler),
	(r"/story/([0-9]+)", StoryHandler),
	(r"/getFullPage", GetFullPageAsyncHandler),
	(r"/static/tornado-0.2.tar.gz", tornado.web.RedirectHandler,
	 dict(url = "https://github.com/downloads/facebook/tornado/tornado-0.2.tar.gz")),
])

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
