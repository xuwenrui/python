#!/usr/bin/env python
# encoding: utf-8
"""
@author: frank
@file: singer_spider.py
@time: 2019/4/21 17:02
@desc:
"""
from qq_music.service.singer_service import SingerService

singer_service = SingerService()


class SingerCrawlTest(object):
    def singer_craw(self):
      pass


if __name__ == '__main__':
    sc = SingerCrawlTest()
    sc.singer_craw()
