from cpu import CpuTemp
import numpy as np
import time
import os
from urllib import request, parse

np.random.seed(1234)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def post(target, value=None):
    url = os.environ.get('TARGET_URL') or 'http://instrumented-app-go:8080'
    data = bytes(str(value), 'UTF-8')
    req =  request.Request(url+'/'+target, data=data, method="POST")
    request.urlopen(req)

cpu = CpuTemp()
while True:
   print(cpu.value)
   post('cpu', cpu.value)
   cpu.update()
   if (np.random.ranf() < sigmoid(((cpu.value - 120) / 120))/10):
       print("sda err")
       post('hd', 'sda')
   if (np.random.ranf() < sigmoid(((cpu.value - 120) / 120))/10):
       print("sdb err")
       post('hd', 'sdb')
   time.sleep(1)
