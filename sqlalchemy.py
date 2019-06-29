import sqlalchemy
import os
import sys
from sqlalchemy import Column, String, create_engine,Integer,Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

CONF_SQL_URL = "postgresql://postgres:postgres@127.0.0.1:5432/tester"

engine = create_engine(CONF_SQL_URL)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

class Test_Serial(Base):
     __tablename__ = 'test_serial'
     id = Column(Integer,Sequence('test_serial_id_seq'), primary_key=True)
     count = Column(Integer)

def insert_count(count=0):

    objs = []
    for i in range(count):
        t = Test_Serial()
        t.count = i
        objs.append(t)
    if objs:
        print 'insert count:',count
        session.bulk_save_objects(objs)
        session.commit()

def insert_loop(loop=1):
    for i in range(loop):
        print 'insert loop:', i
        insert_count(100000)


def main():
    insert_loop(10000)
    session.close()

if __name__=='__main__':
    main()
