from theme_info import ThemeInfo
from base_model import BaseModel
from account_manager import AccountManager
from consts import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from datetime import datetime

class ThemeManager(object):
    def __init__(self, engine):
        BaseModel.metadata.create_all(engine)
        self.session = sessionmaker(bind=engine, autocommit=True)()

    def handle_uploaded_theme(self, theme_info):
        pass

    def get_theme_info_by_theme_id(self, theme_id):
        pass

    def get_upload_themes_by_account(self, account_id):
        pass

    def get_theme_account_provider(self, theme_info):
        pass

    def record_theme(self, theme_info):
        with self.session.begin():
            self.session.add(theme_info)

def __test_all():
    username = DATABASE_USER_NAME
    password = DATABASE_PASSWORD
    host = DATABASE_HOST_NAME
    dbname = DATABASE_DB_NAME
    db_url = "mysql://%s:%s@%s/%s?charset=utf8" % (username, password, host, dbname)
    engine = create_engine(db_url, pool_recycle = 3600, echo = False)
    theme_manager = ThemeManager(engine)
    account_manager = AccountManager(engine)

    email_zhengwei0828 = 'zhengwei0828@gmail.com'
    account_zhengwei0828 = account_manager.get_account_info_by_email(email_zhengwei0828)

    print (account_zhengwei0828)
    theme_zhengwei0828 = ThemeInfo(provider_account_id = account_zhengwei0828[0].account_id,
                               theme_tag='Shanghai',
                               upload_time=datetime.now(),
                               download_count=0,
                               last_download_time=datetime.now())
    theme_manager.record_theme(theme_zhengwei0828)

if __name__ == '__main__':
    __test_all()
    pass

