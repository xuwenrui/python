#!/usr/bin/env python
# encoding: utf-8
"""
@author: frank
@file: redis.py
@time: 2019/4/17 17:40
@desc:
"""
import redis


class Redis(object):

    @staticmethod
    def __get_conn(__pool):
        return redis.Redis(connection_pool=__pool)

    def __init__(self):
        self.__conn = self.__get_conn(redis.ConnectionPool(host='127.0.0.1', port=6379))

    def set(self, key, value):
        return self.__conn.set(key, value)

    def get(self, key):
        return self.__conn.get(key)


