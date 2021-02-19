import urllib.request
from bs4 import BeautifulSoup
from library import cf
import json
from urllib import parse
from collections import OrderedDict
import pandas_datareader as data
import pandas as pd
from datetime import datetime
import pymysql

#실시간 지수 데이터 받아오기
basic_url = "https://finance.naver.com/sise/"

fp = urllib.request.urlopen(basic_url)

source = fp.read()

fp.close()

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("span",class_="num")


kospi_value = soup[0].string
kosdaq_value = soup[1].string

print(kospi_value)
print(kosdaq_value)




# conn = pymysql.connect(host='localhost', user='root', password=cf.db_passwd, charset='utf8')
# cursor = conn.cursor()
# sql = "CREATE DATABASE KOSDAQ"
#
# cursor.execute(sql)
#
# conn.commit()
# conn.close()



# 두 가지의 방식
# ^KS11(코스피) , KQ11(코스닥)

#맨 처음에만 시도, 지수 데이터를 sql에 저장하는데 사용
kosp = data.get_data_yahoo("^KS11")
kosp = kosp.reset_index()


kosq = data.get_data_yahoo("^KQ11")
kosq = kosq.reset_index()


#일별 db업데이트
start_date = datetime(2021,2,19)
end_date = datetime(2021,2,19)

df = data.get_data_yahoo("^KS11", start_date, end_date)