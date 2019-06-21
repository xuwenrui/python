#!/usr/bin/env python
# encoding: utf-8
"""
@author: frank
@file: singer_dtl_crawl.py
@time: 2019/5/15 11:29
@desc:
"""
from urllib import parse
import requests
import json
from qq_music.service.singer_service import SingerService
import random
from qq_music.db.redis_conn import Redis
import time
import xml.dom.minidom as xmldom

redis = Redis()
singer_service = SingerService()


class SingerDtlCrawl(object):

    @staticmethod
    def get_singer_dtl_key(key):
        return {
            "中文名": "name",
            "外文名": "name_en",
            "别名": "alias",
            "国籍": "country",
            "出生地": "birth_place",
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

    # 获取歌手简介
    @staticmethod
    def __get_singer_intro():
        headers = {"Referer": "https://c.y.qq.com/xhr_proxy_utf8.html",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}
        singer_mid = '002J4UUk29y8BY'
        url = "https://c.y.qq.com/splcloud/fcgi-bin/fcg_get_singer_desc.fcg?singermid=" + singer_mid \
              + "&utf8=1&outCharset=utf-8&format=xml&r=" + str(int(time.time() * 1000))

        res = requests.get(url, verify=False, headers=headers)
        res_content = res.content.decode('utf-8')
        print(res_content)
        SingerDtlCrawl.parse_singer_res_xml(res_content)

    @staticmethod
    def parse_singer_res_xml(res_content):
        root = xmldom.parseString(res_content)
        # 获得子标签
        items = root.getElementsByTagName("item")
        singer_dtl = []
        for i in range(len(items)):
            singer_dtl_key = SingerDtlCrawl.get_singer_dtl_key(items[i].getElementsByTagName("key")[0].firstChild.data)
            if len(singer_dtl_key) > 0:
                value = items[i].getElementsByTagName("value")[0].firstChild.data
                if singer_dtl_key == "" and len(value) == 0:
                    break
                singer_dtl.append(value)
            else:
                singer_dtl.append("")
        print(singer_dtl)

    # 获取歌手成就（专辑数，歌曲受，mv数量）
    def __get_singer_achievement(self):
        pass

    # 获取歌手关注数
    def _get_singer_follow_num(self):
        pass

    def crawl(self):
        # self.__get_singer_intro()


    @staticmethod
    def test():
        print(int(time.time() * 1000))


if __name__ == '__main__':
    s = SingerDtlCrawl()
    s.crawl()
    # s.test()
