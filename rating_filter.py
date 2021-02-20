import pymysql
from library import cf
import sys
import logging
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

conn = pymysql.connect(host=cf.db_ip,
                       port=int(cf.db_port),
                       user=cf.db_id,
                       password=cf.db_passwd,
                       db='jackbot1_imi1',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

cur = conn.cursor()


