from account_info import AccountInfo
from base_model import BaseModel
from consts import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from datetime import datetime

class AccountManager(object):
    def __init__(self, engine):
        BaseModel.metadata.create_all(engine)
        self.session = sessionmaker(bind=engine, autocommit=True)()

    def get_account_info_by_email(self, email):
        return self.session.query(AccountInfo).filter_by(email = AccountInfo.email).first()

    def is_account_exist(self, account_id):
        query = self.session.query(AccountInfo).filter_by(AccountInfo.account_id == account_id)
        return len(query.all()) != 0

    def is_email_registered(self, email):
        query = self.session.query(AccountInfo).filter(AccountInfo.email == email)
        return len(query.all()) != 0

    def is_password_valid(self, email, password):
        account_info = self.get_account_info_by_email(email)
        return (account_info is not None) and (account_info.password == password)

    def add_account(self, account_info):
        if self.get_account_info_by_email(email=account_info.email):
            return

        with self.session.begin():
            self.session.add(account_info)

    def delete_account_by_email(self, email):
        account_info = self.session.query(AccountInfo).filter(AccountInfo.email == email)
        if account_info:
            account_info.delete()

    def get_account_upload_operations(self, account_id):
        pass

    def get_account_download_operations(self, account_id):
        pass

    def update_record(self):
        self.session.commit()

def __test_all():
    username = DATABASE_USER_NAME
    password = DATABASE_PASSWORD
    host = DATABASE_HOST_NAME
    dbname = DATABASE_DB_NAME
    db_url = "mysql://%s:%s@%s/%s?charset=utf8" % (username, password, host, dbname)
    engine = create_engine(db_url, pool_recycle = 3600, echo = False)
    account_manager = AccountManager(engine)

    # test user 'zhengwei0828@gmail.com' is existing in database
    zhengwei0828_gmail = "zhengwei0828@gmail.com"
    print ("----- test [account] zhengwei0828@gmail.com is existing in database -----")
    print (account_manager.get_account_info_by_email(zhengwei0828_gmail))
    print ("----- test [email] zhengwei0828@gmail.com is existing in database -----")
    print (account_manager.is_email_registered(zhengwei0828_gmail))

    print ("----- add zhengwei0828@gmail.com to database -----")
    zhengwei0828_account = AccountInfo(email = zhengwei0828_gmail, password = 'zhengwei',
                                       gender = True, auth_token = None, register_time = datetime.now())
    account_manager.add_account(zhengwei0828_account)

    print ("----- test [account] zhengwei0828@gmail.com is existing in database -----")
    print (account_manager.get_account_info_by_email(zhengwei0828_gmail))

    print ("----- test [delete account] zhengwei0828@gmail.com in database -----")
    #account_manager.delete_account_by_email(zhengwei0828_gmail)
    #account_manager.delete_account_by_email(zhengwei0828_gmail)

    print ("----- test [account] zhengwei0828@gmail.com is existing in database -----")
    print (account_manager.get_account_info_by_email(zhengwei0828_gmail))

if __name__ == '__main__':
    __test_all()