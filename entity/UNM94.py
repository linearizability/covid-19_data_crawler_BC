# -*- coding = utf-8 -*-
# @Software: PyCharm
# @File UNM94.py
# @Author : ZhangBoyuan
# @Time : 2024/6/17 18:53

from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class UNM94(Base):
    __tablename__ = 'unm94'
    ID = Column(Integer, primary_key=True, autoincrement=False, nullable=False)
    COUNTRY_NAME = Column(String(255))

    def __init__(self, COUNTRY_NAME):
        self.COUNTRY_NAME = COUNTRY_NAME

    def __init__(self, ID, COUNTRY_NAME):
        self.ID = ID
        self.COUNTRY_NAME = COUNTRY_NAME

engine = create_engine("sqlite:///../static/covid-19.db")

DBSession = sessionmaker(bind=engine)
