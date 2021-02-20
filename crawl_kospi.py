from library import cf
import pymysql
from sqlalchemy import create_engine
pymysql.install_as_MySQLdb()
import MySQLdb
import urllib.request
from bs4 import BeautifulSoup
import json
from urllib import parse
from collections import OrderedDict
import pandas_datareader as data
import pandas as pd
from datetime import datetime
import time


#날자 데이터 전처리, timestamp  => str
def trans_string(t):
    Date = []
    for x in t:
        x = str(x)
        x = x.replace(" ", "")
        x = x.replace("00:00:00", "")
        x = x.replace("-", "")
        Date.append(x)
    return Date

#당일 날자 조회
d = datetime.today()

start_date = datetime(d.year,d.month,d.day)
end_date = datetime(d.year,d.month,d.day)

# 두 가지의 방식
# ^KS11(코스피) , KQ11(코스닥)

##########################################코스피######################################
#처음 데이터를 받아올떄만 사용
# kosp = data.get_data_yahoo("^KS11")
# kosp = kosp.reset_index()
# Date = trans_string(kosp["Date"])
# kosp["Date"] = Date
# engine = create_engine("mysql+mysqldb://root:"+cf.db_passwd+"@localhost/kospi", encoding='utf-8')
# conn = engine.connect()
#
# kosp.to_sql(name='crawl_kospi', con=conn, if_exists='append',index=False)


#코스피 일별 db업데이트
df = data.get_data_yahoo("^KS11", start_date, end_date)
kospi_df = df.reset_index()

engine = create_engine("mysql+mysqldb://root:"+cf.db_passwd+"@localhost/kospi", encoding='utf-8')
conn = engine.connect()

kospi_df.to_sql(name='crawl_kospi', con=conn, if_exists='append',index=False)


##################################코스닥##################################
# kosq = data.get_data_yahoo("^KQ11")
# kosq = kosq.reset_index()
#
# Date = trans_string(kosq["Date"])
# kosq["Date"] = Date
#
# engine = create_engine("mysql+mysqldb://root:"+cf.db_passwd+"@localhost/kosdaq", encoding='utf-8')
# conn = engine.connect()
#
# kosp.to_sql(name='crawl_kosdaq', con=conn, if_exists='append',index=False)


#코스닥 일별 db업데이트
df = data.get_data_yahoo("^KQ11", start_date, end_date)
kosdaq_df = df.reset_index()

engine = create_engine("mysql+mysqldb://root:"+cf.db_passwd+"@localhost/kosdaq", encoding='utf-8')
conn = engine.connect()

kospi_df.to_sql(name='crawl_kosdaq', con=conn, if_exists='append',index=False)