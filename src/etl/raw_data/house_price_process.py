#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "xiaoyong.Liang"
import sys, json
from base import House_price_base
# print(sys.path)
from pyquery import PyQuery as pq
class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


# with open('04480984-2b07-11e8-8155-e09467d4fa03.json', 'r') as f:
#     data = json.load(f, object_hook=JSONObject)
    # data = json.loads(f.readlines(), object_hook=JSONObject)
# print(data.data_type)


class New_house_process(object):
    def __init__(self, item):
        # super().__init__(item)
        self.item = item
        self.obj = None
        
        if item:
            self.obj = self.load()
    
    def load(self):
        with open(self.item, 'r') as f:
            return json.load(f, object_hook=JSONObject)
    
    
    def process(self):
        print(self.obj.data_type)
        
obj = New_house_process('04480984-2b07-11e8-8155-e09467d4fa03.json')
obj.process()