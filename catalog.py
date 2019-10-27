# encoding: utf-8
"""
@version: 1.0
@author:
@file: db_api
@time: 2019-06-15 22:39
"""
import random
import requests
from bs4 import BeautifulSoup
from config import header


# 抓取目录
def catalog(url):
    _list = []
    req = requests.get(url, headers=header[random.randint(0, 4)])
    _temp_result = req.content.decode('gbk')
    bs = BeautifulSoup(_temp_result, "html.parser")

    all_list = bs.find('div', id='list-chapterAll')
    if all_list is None:
        return _list

    list_tag = all_list.find('dl', 'panel-chapterlist')
    if list_tag is None:
        return _list

    a_tags = list_tag.findAll('a')
    for k in a_tags:
        _dict = dict()
        _dict['name'] = k.get_text()
        _dict['link'] = url + k.attrs['href']
        _list.append(_dict)

    return _list


if __name__ == "__main__":
    _temp = catalog('http://www.biqukan.cc/book/47583/')
    for i in _temp:
        print(i)
