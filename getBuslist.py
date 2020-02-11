import requests
from pyquery import PyQuery as pq
import queue
import time
import json
accessQueue = queue.Queue()
baseURL = "https://guangzhou.8684.cn/list"
for i in range(1,10):
  url =  baseURL + str(i)
  accessQueue.put(url)
for i in range(ord('A'),ord('Z') + 1):
  url = baseURL + chr(i)
  accessQueue.put(url)
buslist = []
while not accessQueue.empty():
  url = accessQueue.get()
  resp = requests.get(url)
  resp.close()
  if resp.status_code == 200:
    pqhtml = pq(resp.text)
  for line in pqhtml(".cc-content .list.clearfix a").items('a'):
    buslist.append(line.text())
  time.sleep(1)
  if len(buslist) > 0:
    fJson = open("bus" + url.split('/')[3] + ".json","w")
    fJson.write(json.dumps(buslist))
    fJson.close()
  print("Loading Bus Line from " + url + " Loaded "+ str(len(buslist)))
  buslist.clear()

