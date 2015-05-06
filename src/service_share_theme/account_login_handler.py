__author__ = 'weizheng'

import tornado.web
from datetime import datetime

from account_manager import AccountManager
from account_info import AccountInfo
from consts import *
from response_message import ReponseMessage

class AccountLoginHandler(tornado.web.RequestHandler):
    def initialize(self, database_engine):
        self.account_manager = AccountManager(database_engine)

    def post(self):
        #TODO: catch MissingArgumentError Exception
        email = self.get_argument("email")
        auth_token = self.get_argument("auth_token", None)
        password = self.get_argument("password")

        response_msg = ReponseMessage()
        if not self.account_manager.is_email_registered(email):
            response_msg.set_error_code(ERROR_CODE_LOGIN_NAME_NOT_EXIST)
        elif not self.account_manager.is_password_valid(email, password):
            response_msg.set_error_code(ERROR_CODE_LOGIN_PWD_INVALID)
        else:
            account_info = self.account_manager.get_account_info_by_email(email)
            account_info.last_login_time = datetime.now()
            self.account_manager.update_record()

        self.write(response_msg)

