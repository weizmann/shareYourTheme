__author__ = 'weizheng'

from sqlalchemy import create_engine, Column, ForeignKey
from sqlalchemy.dialects.mysql import VARCHAR, BIGINT, BOOLEAN, DATETIME
from sqlalchemy.orm import relationship, backref

from base_model import BaseModel

class ThemeInfo(BaseModel):
    __tablename__ = 'theme_info'

    theme_id = Column(BIGINT(unsigned=True), primary_key=True, autoincrement=True)

    # foreign key and backref variable
    provider_account_id = Column(BIGINT(unsigned=True), ForeignKey('account_info.account_id'))
    provider_account = relationship('AccountInfo', backref('theme_info', order_by=theme_id))

    theme_tag = Column(VARCHAR(128))
    upload_time = Column(DATETIME, index=True)
    download_count = Column(BIGINT(unsigned=True))
    last_download_time = Column(DATETIME, index=True)


    def __init__(self, provider_account_id, theme_tag, upload_time, download_count, last_download_time):
        self.provider_account_id = provider_account_id
        self.theme_tag = theme_tag
        self.upload_time = upload_time
        self.download_count = download_count
        self.last_download_time = last_download_time