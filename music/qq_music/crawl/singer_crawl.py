#!/usr/bin/env python
# encoding: utf-8
"""
@author: frank
@file: singer_spider.py
@time: 2019/4/21 17:02
@desc:
"""
from urllib import parse
import requests
import json
from qq_music.service.singer_service import SingerService
import random
from qq_music.db.redis_conn import Redis
import time

redis = Redis()
singer_service = SingerService()


class SingerCrawl(object):
    # 获取response
    @staticmethod
    def __sites_resource(cur_page):
        url = SingerCrawl.__build_url(cur_page)
        print(url)
        req = requests.get(url, verify=False)
        return json.loads(req.content.decode('utf-8'))

    # 构建url
    @staticmethod
    def __build_url(cur_page):
        getUCGI = "getUCGI" + str(random.random()).replace("0.", "")
        sin = (cur_page - 1) * 80
        base_url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=' + getUCGI + '&g_tk=5381&loginUin=0' \
                   + '&hostUin=0&format=json&inCharset=utf8' \
                   + '&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data='
        data = '{"comm":{"ct":24,"cv":10000},"singerList":{"module":"Music.SingerListServer","method":' \
               '"get_singer_list","param":' \
               + '{"area":-100,"sex":-100,"genre":-100,"index":-100,"sin":' + str(sin) + ',"cur_page":' + str(
            cur_page) + '}}}'
        return base_url + parse.quote(bytes(data.encode('utf-8')))

    # is_finish 0 否 1.是
    def __parse_response(self, cur_page, is_finish):
        # 将id存入redis
        SingerCrawl.__load_mid_to_redis()
        success_count = 0
        fail_count = 0
        # 获取json数据
        # singer_json = local_resource()
        singer_json = self.__sites_resource(cur_page)
        singer_list = singer_json['singerList']['data']['singerlist']
        singer_arr = []
        try:
            for singer in singer_list:
                if redis.get(singer["singer_id"]) is None:
                    singer_arr.append(singer)
                    success_count += 1
                else:
                    fail_count += 1
            if len(singer_arr) > 100:
                singer_service.insert_bat(singer_arr)
            elif is_finish == 1:
                singer_service.insert_bat(singer_arr)
            print("正在抓取第", cur_page, "页数据,====成功:", success_count, "\t失败：", fail_count, "当前总行数：", redis.get("total"))
        finally:
            singer_service.insert_bat(singer_arr)

    def crawl(self):
        page = 300
        is_finish = 0
        for i in range(page):
            print("执行第", i, "页面")
            if i < 120:
                continue
            if i == page:
                is_finish = 1
            self.__parse_response(i, is_finish)
            time.sleep(5)

    @staticmethod
    def __load_mid_to_redis():
        singer_service.select_all()
        singers = singer_service.select_all()
        if singers:
            redis.set("total", len(singers))
            for singer in singers:
                redis.set(singer["singer_id"], singer["singer_name"].decode("utf-8"))


if __name__ == '__main__':
    sc = SingerCrawl()
    # sc.__load_mid_to_redis()
    sc.crawl()

