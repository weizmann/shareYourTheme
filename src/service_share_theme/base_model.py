__author__ = 'weizheng'

from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()
class BaseModel(BaseModel):
    __abstract__ = True
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }
