# -*- coding:utf-8 -*- 
# 2017/3/24
import time
import requests
import threading

success_count = 0
total_count = 100
q = threading.Lock()


def get_function(uri='http://10.8.15.110'):
    req = requests.get(uri)
    global success_count
    q.acquire()
    if req.status_code == 200:
        success_count += 1
    q.release()

requests_list = []
for each in range(total_count):
    requests_list.append(threading.Thread(target=get_function))

t1 = time.time()
for each in requests_list:
    each.start()

for each in requests_list:
    each.join()
t2 = time.time()
print t2-t1
print "status code is 200 (count):", success_count
print "total request count :", total_count
print "test result:", success_count/(t2-t1)*60, 'r/m'
