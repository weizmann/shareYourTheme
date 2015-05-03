from theme_info import ThemeInfo
from base_model import BaseModel
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