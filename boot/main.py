# -*- coding = utf-8 -*-
# 工程启动类
# @Software: PyCharm
# @File main.py
# @Author : ZhangBoyuan
# @Time : 2024/1/6 下午11:10
import json
import sqlite3

import requests

from constant.url_path import UrlPath


def get_covid19_data_dict():
    response = requests.get(url=UrlPath.INDEX_URL)
    response.encoding = "utf-8"
    dataJson = json.loads(response.text);
    return dataJson['value']


if __name__ == '__main__':
    covid19DataDict = get_covid19_data_dict()

    conn = sqlite3.connect("../static/covid-19.db")
    cur = conn.cursor()

    for i in covid19DataDict:
        sql = """insert into covid_19_data values ('%s', '%s', '%s');""" % (
        i.get('DIM_TIME'), i.get('DIM_GEO_CODE_M49'), str(i.get('VALUE_NUMERIC')))

        cur.execute(sql)
        conn.commit()

    cur.close()
    conn.close()
