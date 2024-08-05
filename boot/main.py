# -*- coding = utf-8 -*-
# 工程启动类
# @Software: PyCharm
# @File main.py
# @Author : ZhangBoyuan
# @Time : 2024/1/6 下午11:10
import json

import requests
from bs4 import BeautifulSoup

from constant.url_path import UrlPath
from entity.Covid19Data import DBSession, Covid19Data
from utils.CollectionUtils import isNotEmpty


def get_covid19_data_dict():
    response = requests.get(url=UrlPath.INDEX_URL)
    response.encoding = "utf-8"
    dataJson = json.loads(response.text)
    return dataJson['value']


def get_unm94_dict():
    soup = BeautifulSoup(requests.get(url=UrlPath.UN_M49_URL).text, 'html.parser')

    for div in soup.find_all('div', class_="Area table_roll table_item"):
        for tr in div.find_all('tr', class_="tr_bg"):
            print(tr.get_text())


def sync_covid19_data():
    covid19DataDict = get_covid19_data_dict()

    newCovid19DataList = []

    for i in covid19DataDict:
        newCovid19Data = Covid19Data(i.get('DIM_TIME'), i.get('DIM_GEO_CODE_M49'), str(i.get('VALUE_NUMERIC')))
        newCovid19DataList.append(newCovid19Data)

    if isNotEmpty(newCovid19DataList):
        session = DBSession()
        session.add_all(newCovid19DataList)
        session.commit()
        session.close()


if __name__ == '__main__':
    covid19DataDict = get_unm94_dict()
