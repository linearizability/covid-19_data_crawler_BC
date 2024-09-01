# -*- coding = utf-8 -*-
# @Software: PyCharm
# @File CollectionUtils.py
# @Author : ZhangBoyuan
# @Time : 2024/6/10 18:14

def isEmpty(collection):
    if collection is None:
        return True
    if not isinstance(collection, list):
        return False
    if len(collection) <= 0:
        return True
    return False

def isNotEmpty(collection):
    return not isEmpty(collection)
