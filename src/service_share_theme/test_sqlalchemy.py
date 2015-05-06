__author__ = 'weizheng'

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.orm import sessionmaker, relationship, backref

from consts import *

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                                self.name, self.fullname, self.password)

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    email_address = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", backref=backref('addresses', order_by = id))

    def __repr__(self):
        return "<Address(email_address = '%s')>" % self.email_address

username = DATABASE_USER_NAME
password = DATABASE_PASSWORD
host = DATABASE_HOST_NAME
dbname = "test_sqlalchemy"

db_url = "mysql://%s:%s@%s/%s?charset=utf8" % (username, password, host, dbname)
engine = create_engine(db_url, pool_recycle = 3600, echo = True)

# create table
Base.metadata.create_all(engine)

# setup session
Session = sessionmaker(bind = engine)
session = Session()

# add single user
ed_user = User(name = "ed", fullname = "Ed Jones", password = 'edspassword')
session.add(ed_user)

# batch add users
session.add_all([
        User(name='wendy', fullname='Wendy Williams', password='foobar'),
        User(name='mary', fullname='Mary Contrary', password='xxg527'),
        User(name='fred', fullname='Fred Flinstone', password='blah')])

session.commit()