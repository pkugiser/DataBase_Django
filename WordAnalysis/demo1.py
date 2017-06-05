#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.qcloudapi import QcloudApi

module = 'wenzhi'
action = 'TextSentiment' # TextKeywords
config = {
    'Region': 'bj',
    'SecretId': "AKIDUnqdARAEjy4vXsylvqUszpPjmY3JuK6c",
    'SecretKey': "NTIq89tMaXDckeJirkMiohKhndDWaPyI",
    'method': 'post'
}
params = {
    'content': '我恨你',
    #'SignatureMethod':'HmacSHA256',#指定所要用的签名算法，可选HmacSHA256或HmacSHA1，默认为HmacSHA1
}
try:
    service = QcloudApi(module, config)
    print(service.generateUrl(action, params))
    print(service.call(action, params))
    #service.setRequestMethod('get')
    #print service.call('DescribeCdnEntities', {})
except Exception as e:
    print ('exception:', e)
