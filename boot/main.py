# -*- coding = utf-8 -*-
# 工程启动类
# @Software: PyCharm
# @File main.py
# @Author : ZhangBoyuan
# @Time : 2024/1/6 下午11:10
import json

import requests
import re
from bs4 import BeautifulSoup

from constant.url_path import UrlPath
from entity.Covid19Data import DBSession, Covid19Data
from entity.UNM49 import UNM49
from utils.CollectionUtils import is_not_empty


def get_covid19_data_dict():
    response = requests.get(url=UrlPath.INDEX_URL)
    response.encoding = "utf-8"
    dataJson = json.loads(response.text)

    return dataJson['value']


def get_unm49_dict():
    result = []
    soup = BeautifulSoup(requests.get(url=UrlPath.UN_M49_URL).text, 'html.parser')
    for div in soup.find_all('div', class_="Area table_roll table_item"):
        for tr in div.find_all('tr', class_="tr_bg"):
            chinese_chars = re.findall(r'[\u4e00-\u9fff]+', tr.text)
            digits = re.findall(r'\d+', tr.text)
            result.append(UNM49(digits, chinese_chars))

    return result


def sync_unm49_data():
    unm49List = get_unm49_dict()
    if is_not_empty(unm49List):
        session = DBSession()
        session.add_all(unm49List)
        session.commit()
        session.close()

def sync_covid19_data():
    covid19DataDict = get_covid19_data_dict()

    newCovid19DataList = []
    for i in covid19DataDict:
        newCovid19Data = Covid19Data(i.get('DIM_TIME'), i.get('DIM_GEO_CODE_M49'), str(i.get('VALUE_NUMERIC')))
        newCovid19DataList.append(newCovid19Data)

    if is_not_empty(newCovid19DataList):
        session = DBSession()
        session.add_all(newCovid19DataList)
        session.commit()
        session.close()


if __name__ == '__main__':
    sync_covid19_data()