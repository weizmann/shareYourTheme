import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		greetings = self.get_argument("greeting", "Hello")
		self.write(greetings + ", friendly user!!")

	def write_error(self, status_code, **kwargs):
		self.write("dear user, you cause a %d error." % status_code)

if __name__ == "__main__":
	tornado.options.parse_command_line()
	app = tornado.web.Application(
		handlers = [
			(r"/", IndexHandler),
	])

	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
