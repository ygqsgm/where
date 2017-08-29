#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import sys


def run():
    ip = {"ip": str(sys.argv[1])}
    response = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip', params=ip).json()
    if response['code']:
        print "查询失败:  " + response['data'].encode('utf-8')
    else:
        data = {k: unicode(v).encode("utf-8") for k,v in response['data'].iteritems()}
        print "查询IP: " + data['ip']
        if data['country'] != "中国":
            print "国家: " + data['country']
        else:
            print "区域: " + data['area']
            print "省份: " + data['region'] + "  城市: " + data['city'] + " 区: " + data['county']
            print "运营商: " + data['isp']

if __name__ == '__main__':
    run()
