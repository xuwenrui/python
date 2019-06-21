#!/usr/bin/env python
# encoding: utf-8
"""
@author: frank
@file: singer_dtl_service.py
@time: 2019/5/15 11:10
@desc: 歌手详情
"""

from qq_music.db.mysql_conn import Mysql

mysql = Mysql()


class SingerDtlService(object):
    @staticmethod
    def select_all():
        sql = "select * from qq_singer_dtl"
        return mysql.getAll(sql)

    @staticmethod
    def insert_bat(singer_dtl_list):
        sql = "insert into qq_singer_dtl (singer_mid,name,name_en,country,birth_place,main_work,birth_day," \
              "song_num,album_num,mv_num,follow_num,singer_id,create_time" \
              ") values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        count = mysql.insertMany(sql, singer_dtl_list)
        # 释放资源
        mysql.end()
        return count
