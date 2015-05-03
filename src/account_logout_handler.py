__author__ = 'weizheng'
import tornado.web
from datetime import datetime

from account_manager import AccountManager
from account_info import AccountInfo
from consts import *
from response_message import ReponseMessage

class AccountLogoutHandler(tornado.web.RequestHandler):
    def initialize(self, database_engine):
        self.account_manager = AccountManager(database_engine)

    def post(self):
        #TODO: catch MissingArgumentError Exception
        email = self.get_argument("email")
        gender = True
        auth_token = self.get_argument("auth_token")
        register_time = datetime.now()
        password = self.get_argument("password")

        response_msg = ReponseMessage()
        if self.account_manager.is_email_registered(email):
            response_msg.set_error_code(ERROR_CODE_REGISTER_ACCOUNT_EXIST)
        else:
            account_info = AccountInfo(email=email, gender=gender, auth_token=auth_token, password=password, register_time=register_time)
            self.account_manager.add_account(account_info)

        self.write(response_msg)

