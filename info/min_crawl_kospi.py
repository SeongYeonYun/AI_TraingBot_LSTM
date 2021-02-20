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

#일별 db업데이트
start_date = datetime(2021,2,19)
end_date = datetime(2021,2,19)

df = data.get_data_yahoo("^KS11", start_date, end_date)
df = df["Date"].str_replace("-","")
print(df)

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