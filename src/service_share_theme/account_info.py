
from sqlalchemy import create_engine, Column, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import VARCHAR, BIGINT, BOOLEAN, DATETIME

from base_model import BaseModel

class AccountInfo(BaseModel):
    __tablename__ = 'account_info'
    account_id = Column(BIGINT(unsigned=True), primary_key=True, autoincrement=True)
    email = Column(VARCHAR(128))
    password = Column(VARCHAR(128))
    gender = Column(BOOLEAN)
    auth_token = Column(VARCHAR(128))
    register_time = Column(DATETIME, index=True)
    last_login_time = Column(DATETIME, index=True)

    def __str__(self):
        return "<AccountInfo email = %s, password = %s, auth_token = %s, register_time = %s>" \
            %(self.email, self.password, self.auth_token, self.register_time)

    def __init__(self, email = None, password = None, gender = None, auth_token = None, register_time = None):
        self.email = email
        self.password = password
        self.gender = gender
        self.auth_token = auth_token
        self.register_time = register_time