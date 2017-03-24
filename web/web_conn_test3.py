# -*- coding:utf-8 -*- 
# 2017/3/24
# -*- coding:utf-8 -*-
# 2017/3/24
import time
import urllib2
import json
import random
import requests
import threading

authkey = ""
success_count = 0
total_count = 20
q = threading.Lock()


def addRand(url):
    if str(url.find('?')) != '-1':
        # 当?存在时
        url = url + '&rand=' + str(random.uniform(1, 100))
    else:
        # 当?号不存在时
        url = url + '?rand=' + str(random.uniform(1, 100)) + '&'
    return url


def get_function(uri='http://10.8.15.110'):
    api = ""
    api = addRand(api)
    request = urllib2.Request(
        api,
        '',
        {'Content-Type': 'application/json', "NS-NTI-KEY": authkey}
    )
    try:
        response = urllib2.urlopen(request)
        result = json.loads(response.read())
        global success_count
        q.acquire()
        if response.getcode() == 200:
            success_count += 1
        q.release()
    except Exception, e:
        pass


requests_list = []
for each in range(total_count):
    requests_list.append(threading.Thread(target=get_function))

t1 = time.time()
for each in requests_list:
    each.start()

for each in requests_list:
    each.join()
t2 = time.time()
print t2 - t1
print "status code is 200 (count):", success_count
print "total request count :", total_count
print "test result:", success_count / (t2 - t1) * 60, 'r/m'
