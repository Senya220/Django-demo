from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, scoped_session



#create database

engine = create_engine('mysql+pymysql://root:password@localhost:3306/test?charset=utf8mb4')
#session used to insert data -->bind to engine
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init():
    Base.metadata.create_all(engine)

def drop():
    Base.metadata.drop_all(engine)

#create table Product
class Product(Base):
    __tablename__ = 'app_product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))

if __name__ == '__main__':
    init()