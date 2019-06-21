#!/usr/bin/env python
# encoding: utf-8
"""
@author: frank
@file: singer_service.py
@time: 2019/4/21 15:53
@desc:
"""
from qq_music.db.mysql_conn import Mysql

mysql = Mysql()


class SingerService(object):

    @staticmethod
    def select_all():
        sql = "select * from qq_singer"
        return mysql.getAll(sql)

    def insert_bat(self, singer_list):
        sql = "insert into qq_singer (country,singer_id,singer_mid,singer_name,singer_pic," \
              "song_num,album_num,mv_num,follow_num) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        params = self.__build_insert_params(singer_list)
        count = mysql.insertMany(sql, params)
        # 释放资源
        mysql.end()
        return count

    @staticmethod
    def __build_insert_params(singer_list):
        params = []
        if len(singer_list):
            for singer in singer_list:
                new_singer = []
                if 'country' not in singer.keys() or len(singer['country']) == 0:
                    new_singer.append("其他")
                else:
                    new_singer.append(singer['country'])

                if 'singer_id' not in singer.keys():
                    new_singer.append(0)
                else:
                    new_singer.append(singer['singer_id'])

                if 'singer_mid' not in singer.keys() or len(singer['singer_mid']) == 0:
                    new_singer.append("")
                else:
                    new_singer.append(singer['singer_mid'])

                if 'singer_name' not in singer.keys() or len(singer['singer_name']) == 0:
                    new_singer.append("")
                else:
                    new_singer.append(singer['singer_name'])

                if 'singer_pic' not in singer.keys() or len(singer['singer_pic']) == 0:
                    new_singer.append("")
                else:
                    new_singer.append(singer['singer_pic'])

                if 'song_num' not in singer.keys():
                    new_singer.append(0)
                else:
                    new_singer.append(singer['song_num'])

                if 'album_num' not in singer.keys():
                    new_singer.append(0)
                else:
                    new_singer.append(singer['album_num'])

                if 'mv_num' not in singer.keys():
                    new_singer.append(0)
                else:
                    new_singer.append(singer['mv_num'])

                if 'follow_num' not in singer.keys():
                    new_singer.append(0)
                else:
                    new_singer.append(singer['follow_num'])

                params.append(new_singer)
        return params
