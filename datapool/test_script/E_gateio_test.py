# -*- coding: utf-8 -*-
"""
Created on 2018/1/14 18:14

@author: JERRY
"""

from datapool.E_gateio.E_gateio_rest.E_gateio_api import GateIO
import pymysql as ps
from sqlalchemy import create_engine
from utilPool.generalUtil import myThread

ps.install_as_MySQLdb()

proxy = {'http_proxy_host':'221.234.195.132',
         'http_proxy_port':'808'}

tableName = 'gateio'
conn = create_engine( 'mysql://Jerry:Eli19890908@localhost/datapool?charset=utf8',echo = False)

threadList = []
test = GateIO(proxy)
param = 'btc_usdt'

threadList.append(myThread(name='depth', target=test.callback,args=(test.orderBook,param)))

for i in threadList:
    i.start()
