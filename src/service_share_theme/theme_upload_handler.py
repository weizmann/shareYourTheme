__author__ = 'weizheng'

import tornado.web

from theme_manager import ThemeManager
from account_manager import AccountManager
from response_message import ReponseMessage
import os

REQUEST_ARGUMENT_ACCOUNT_ID     = "account_id"
REQUEST_ARGUMENT_AUTH_TOKEN     = "auth_token"
REQUEST_ARGUMENT_THEME_CONTENT  = "theme_content"

class ThemeUploadHandler(tornado.web.RequestHandler):
    def __init__(self):
        self.theme_manager = None
        self.account_manager = None

    def initialize(self, database_engine):
        self.theme_manager = ThemeManager(database_engine)
        self.account_manager = AccountManager(database_engine)

    # post arguments:
    # localhost:port/upload?account_id=***&&auth_token=***
    # theme_info is added in self.request.files["theme_content"]
    def post(self):
        account_id = self.get_argument(REQUEST_ARGUMENT_ACCOUNT_ID)
        auth_token = self.get_argument(REQUEST_ARGUMENT_AUTH_TOKEN)

        file_metas = self.request.files["theme_content"]
        upload_path = "./"
        for meta in file_metas:
            file_name = meta['file_name']
            file_path = os.path.join(upload_path, file_name)
            with open(file_path, 'wb') as up:
                up.write(meta['body'])
                up.write(meta['body'])
        #self.theme_manager.record_theme()
        response_msg = ReponseMessage()
        self.write(response_msg)