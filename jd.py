#-*- coding: UTF-8 -*-

import re
import urlparse


class jd:

    URL = "http://search.jd.com/Search?keyword=%E9%9A%8F%E8%BD%A6%E5%90%AC&enc=utf-8&wq=%E9%9A%8F%E8%BD%A6%E5%90%AC&pvid=v2s3gbni.rfs01o"

    def parse_price(self, html):
        price_list = re.findall(r"data-price=\"[\s\S]*?\",", html)
        price = price_list[0].split("=")
        price = re.findall(r"\"[\s\S]*\"", price[1])
        price = price[0].split("\"")
        return price[1]

    def parse_url(self, html):
        url_list = re.findall(r"\/\/item.jd.com\/[\s\S]*?.html", html)
        new_url_list = []
        for url in url_list:
            if not (url in new_url_list):
                new_url_list.append(url)
        if not new_url_list[0].startswith("http"):
            new_url_list[0] = "http:" + new_url_list[0]
        return new_url_list[0]
        # url = url_list[0].split(":")
        # url = re.findall(r"\"[\s\S]*\"", url[1])
        # url = url[0].split("\"")
        # if not url[1].startswith("http"):
        #     url[1] = "http:" + url[1]
        # url = url[1].decode("raw_unicode_escape")
        # return url


    def get_max_price_url(self, keyword):
        result = urlparse.urlparse(self.URL)
        query = result.query + "&psort=1"
        queries = urlparse.parse_qs(query)
        if queries.has_key("keyword"):
            list = []
            list.append(keyword)
            queries['keyword'] = list
        if queries.has_key("wq"):
            list = []
            list.append(keyword)
            queries['wq'] = list
        query = ""
        for (key, value) in queries.items():
            query = query + key + "=" + value[0] + "&"
        query = query[0:len(query) - 1]
        url = result.scheme +"://" + result.netloc+ result.path + "?" + query
        print url
        return url

    def get_min_price_url(self, keyword):
        result = urlparse.urlparse(self.URL)
        query = result.query + "&psort=2"
        queries = urlparse.parse_qs(query)
        print queries
        if queries.has_key("keyword"):
            list = []
            list.append(keyword)
            queries['keyword'] = list
        if queries.has_key("wq"):
            list = []
            list.append(keyword)
            queries['wq'] = list
        query = ""
        for (key, value) in queries.items():
            query = query + key + "=" + value[0] + "&"
        query = query[0:len(query) - 1]
        url = result.scheme + "://" + result.netloc + result.path + "?" + query
        print url
        return url