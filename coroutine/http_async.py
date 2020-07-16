import asyncio
from asyncio import Queue
from tornado import httpclient
import time
import requests
import concurrent.futures

"""
learnging async by using blocking http-get function
"""


async def main():
    loop = asyncio.get_event_loop()
    start = time.time()
    fetures = list()
    for _ in range(100):
        fetures.append(loop.run_in_executor(
            None, requests.get, "http://www.google.com/"))
    responses = list()
    for f in fetures:
        resp = await f
        responses.append(len(resp.text))
    print(len(responses))
    print("finish,async time use {0}f".format(time.time()-start))


asyncio.run(main())

start = time.time()
for each in range(100):
    requests.get("http://www.google.com/")
print("finish,sync time use {0}f".format(time.time()-start))
