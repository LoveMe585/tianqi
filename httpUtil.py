# -*- coding:utf-8 -*-
# author = wulu 
# date = 2018/11/7

import requests


class HttpUtil:

    headler = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive',
               }

    def doGet(self, url):
        if url is None:
            print("url is None")
            return

        response = requests.get(url, self.headler)

        return response.text.encode('utf-8')



    def doPost(self, url, param):
        if url is None:
            print('url is None')
            return
        response = requests.post(url, param, self.headler)

        return response.text.encode('utf-8')





