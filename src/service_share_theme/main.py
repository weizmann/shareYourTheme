import tornado.ioloop
import tornado.web

from account_register_handler import AccountRegisterHandler
from account_login_handler import AccountLoginHandler
from account_logout_handler import AccountLogoutHandler

from theme_upload_handler import  ThemeUploadHandler
from query_share_companion_handler import QueryShakeCompanionHandler
from theme_download_handler import DownloadThemeHandler

from sqlalchemy import create_engine

def get_database_engine():
    username = "wei.zheng"
    password = "zhengwei"
    host = "localhost"
    dbname = "share_your_theme"
    db_url = "mysql://%s:%s@%s/%s?charset=utf8" % (username, password, host, dbname)
    engine = create_engine(db_url, pool_recycle = 3600, echo = False)
    return engine

database_engine = get_database_engine()

application = tornado.web.Application([
	(r"/register", AccountRegisterHandler, dict(database_engine=database_engine)),
    (r"/login", AccountLoginHandler, dict(database_engine=database_engine)),
    (r'/logout', AccountLogoutHandler, dict(database_engine=database_engine)),

	#(r"/upload/", UploadThemeHandler),
	#(r"/queryShakeCompanion/", QueryShakeCompanionHandler),
	#(r"/downloadTheme/", DownloadThemeHandler),
])

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
