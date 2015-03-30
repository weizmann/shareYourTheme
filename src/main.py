import tornado.ioloop
import tornado.web

application = tornado.web.Application([
	(r"/upload/", UploadThemeHandler),
	(r"/queryShakeCompanion/", QueryShakeCompanionHandler),
	(r"/downloadTheme/", DownloadThemeHandler),
])

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
