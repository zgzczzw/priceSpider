#-*- coding: UTF-8 -*-

import re
import urlparse


class taobao:

    URL = "https://s.taobao.com/search?q=%E9%9A%8F%E8%BD%A6%E5%90%AC&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20160422"

    def parse_price(self, html):
        price_list = re.findall(r"\"view_price\":\"[\s\S]*?\",", html)
        price = price_list[0].split(":")
        price = re.findall(r"\"[\s\S]*\"", price[1])
        price = price[0].split("\"")
        return float(price[1])


    def parse_url(self, html):
        url_list = re.findall(r"\"detail_url\":\"[\s\S]*?\",", html)
        url = url_list[0].split(":")
        url = re.findall(r"\"[\s\S]*\"", url[1])
        url = url[0].split("\"")
        if not url[1].startswith("http"):
            url[1] = "http:" + url[1]
        url = url[1].decode("raw_unicode_escape").encode("utf-8")
        return url

    def get_max_price_url(self, keyword):
        result = urlparse.urlparse(self.URL)
        query = result.query + "&sort=price-desc"
        queries = urlparse.parse_qs(query)
        if queries.has_key("q"):
            list=[]
            list.append(keyword)
            queries['q'] = list
        query = ""
        for (key, value) in queries.items():
            query = query + key+"="+value[0]+"&"
        query = query[0:len(query)-1]
        url = result.scheme + "://" + result.netloc+ result.path + "?" + query
        return url

    def get_min_price_url(self, keyword):
        result = urlparse.urlparse(self.URL)
        query = result.query + "&sort=price-asc"
        queries = urlparse.parse_qs(query)
        if queries.has_key("q"):
            list = []
            list.append(keyword)
            queries['q'] = list
        query = ""
        for (key, value) in queries.items():
            query = query + key + "=" + value[0] + "&"
        query = query[0:len(query) - 1]
        url = result.scheme + "://" + result.netloc + result.path + "?" + query
        return url

