#-*- coding: UTF-8 -*-
import urllib
import urlparse
from taobao import taobao
from jd import jd
from const import const

results = {}

def get_html(url):
    try:
        page = urllib.urlopen(url)
        html = page.read()
        result = urlparse.urlparse(url)
        HOST = result.scheme + "://" + result.netloc
        return html
    except:
        return ""

def do_write_file():
    print results
    f = open('./result.txt', 'w')
    for (site, item) in results.items():
        f.write(str(site) + "\t")
        if item.has_key('min'):
            f.write(str(item['min']) + "\t")
        if item.has_key('min_url'):
            f.write(str(item['min_url']) + "\t")
        if item.has_key('max'):
            f.write(str(item['max']) + "\t")
        if item.has_key('max_url'):
            f.write(str(item['max_url']) + "\t")
        f.write("\n")
    f.close()
    print len(results)

if __name__ == '__main__':
    keyword = "回力帆布鞋"
    mTaobao = taobao()
    taobaoResult = {}
    taobaoResult['max'] = mTaobao.parse_price(get_html(mTaobao.get_max_price_url(keyword)))
    taobaoResult['max_url'] = mTaobao.parse_url(get_html(mTaobao.get_max_price_url(keyword)))
    taobaoResult['min'] = mTaobao.parse_price(get_html(mTaobao.get_min_price_url(keyword)))
    taobaoResult['min_url'] = mTaobao.parse_url(get_html(mTaobao.get_min_price_url(keyword)))
    print taobaoResult
    results['taobao'] = taobaoResult

    mJD = jd()
    jDResult = {}
    jDResult['max'] = mJD.parse_price(get_html(mJD.get_max_price_url(keyword)))
    jDResult['max_url'] = mJD.parse_url(get_html(mJD.get_max_price_url(keyword)))
    jDResult['min'] = mJD.parse_price(get_html(mJD.get_min_price_url(keyword)))
    jDResult['min_url'] = mJD.parse_url(get_html(mJD.get_min_price_url(keyword)))
    print jDResult
    results['jd'] = jDResult
    do_write_file()