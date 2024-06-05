# -*- coding = utf-8 -*-
# 工程启动类
# @Software: PyCharm
# @File main.py
# @Author : ZhangBoyuan
# @Time : 2024/1/6 下午11:10
import json

import requests

from constant.url_path import UrlPath
from entity.Covid19Data import DBSession, Covid19Data


def get_covid19_data_dict():
    response = requests.get(url=UrlPath.INDEX_URL)
    response.encoding = "utf-8"
    dataJson = json.loads(response.text);
    return dataJson['value']

if __name__ == '__main__':
    covid19DataDict = get_covid19_data_dict()

    newCovid19DataList = []

    for i in covid19DataDict:
        newCovid19Data = Covid19Data(i.get('DIM_TIME'), i.get('DIM_GEO_CODE_M49'), str(i.get('VALUE_NUMERIC')))
        newCovid19DataList.append(newCovid19Data)

    if newCovid19DataList is not None and len(newCovid19DataList) > 0:
        session = DBSession()
        session.add_all(newCovid19DataList)
        session.commit()
        session.close()
