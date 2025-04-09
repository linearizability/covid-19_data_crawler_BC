# -*- coding = utf-8 -*-
# @Software: PyCharm
# @File Covid19Data.py
# @Author : ZhangBoyuan
# @Time : 2024/5/4 下午6:56

from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Covid19Data(Base):
    __tablename__ = 'covid_19_data'
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    DIM_TIME = Column(String(255))
    DIM_GEO_CODE_M49 = Column(String(255))
    VALUE_NUMERIC = Column(String(255))

    def __init__(self, DIM_TIME, DIM_GEO_CODE_M49, VALUE_NUMERIC):
        self.DIM_TIME = DIM_TIME
        self.DIM_GEO_CODE_M49 = DIM_GEO_CODE_M49
        self.VALUE_NUMERIC = VALUE_NUMERIC

engine = create_engine("sqlite:///../static/covid-19.db")

DBSession = sessionmaker(bind=engine)
