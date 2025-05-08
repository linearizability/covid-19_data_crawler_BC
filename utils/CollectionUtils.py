# -*- coding = utf-8 -*-
# @Software: PyCharm
# @File CollectionUtils.py
# @Author : ZhangBoyuan
# @Time : 2024/6/10 18:14

def is_empty(collection):
    if collection is None:
        return True
    if not isinstance(collection, list):
        return False
    if len(collection) <= 0:
        return True
    return False


def is_not_empty(collection):
    return not is_empty(collection)
