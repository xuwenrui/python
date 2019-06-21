#!/usr/bin/env python
# encoding: utf-8
"""
@author: frank
@file: http_parse.py
@time: 2019/5/15 14:35
@desc:
"""
import xml.dom.minidom as xmldom
from xml.etree import ElementTree
import os


def parse_http_req():
    result = {}
    with open('http.txt', 'r') as file_to_read:
        while True:
            line = file_to_read.readline()  # 整行读取数据
            if not line:
                break
            key = line.split(':')[0]
            value = line.split(':')[1].strip().replace("\n", "")
            result[key] = value
    print(result)

def parse_xml_str():
    xml_str='<?xml version="1.0" encoding="utf-8"?><result><code>0</code></result>'
    # domobj=ElementTree.fromstring(xml_str)
    root = xmldom.parseString(xml_str)
    print("domobj",root)

def parse_res_xml():
    xmlfilepath = os.path.abspath("res.xml")
    print("xml文件路径：", xmlfilepath)

    # 得到文档对象
    domobj = xmldom.parse(xmlfilepath)
    print("xmldom.parse:", type(domobj))
    # 得到元素对象
    root = domobj.documentElement
    # 获得子标签
    items = root.getElementsByTagName("item")
    singer_dtl = []
    for i in range(len(items)):
        # value = items[i].getElementsByTagName("value")[0].firstChild.data
        # if len(value) < 100:
        #     print(items[i].getElementsByTagName("key")[0].firstChild.data,
        #           items[i].getElementsByTagName("value")[0].firstChild.data)
        # print("subElementObj1[i]:", subElementObj[i].childNodes[0].childNodes[0].data)
        singer_dtl_key = get_singer_dtl_key(items[i].getElementsByTagName("key")[0].firstChild.data)
        if len(singer_dtl_key) > 0:
            singer_dtl.append(items[i].getElementsByTagName("value")[0].firstChild.data)
        else:
            singer_dtl.append("")
    print(singer_dtl)

def get_singer_dtl_key(key):
    return {
        "中文名": "name",
        "外文名": "name_en",
        "别名": "alias",
        "国籍": "country",
        "出生地":"birth_place",
        "职业": "occupation",
        "星座": "constellation",
        "民族": "nation",
        "出生日期": "birth_day",
        "代表作品": "main_work",
        "毕业院校": "school",
        "经纪公司": "company",
        "身高": "height",
        "体重": "weight",
        "粉丝": "fans"
    }.get(key, "")


if __name__ == '__main__':
    # parse_http_req()
    # parse_res_xml()
    parse_xml_str()
