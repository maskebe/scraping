import mysql.connector
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import collect as cl

#conn = pymysql.connect(host='127.0.0.1', user='testapi', passwd='testapi123', db='mysql', charset='utf8')
conn = mysql.connector.connect(host='127.0.0.1', user='testapi', passwd='testapi123', db='mysql', charset='utf8')
cur = conn.cursor()
query = ("USE testapi")
cur.execute(query)
nowdate = datetime.datetime.now()

def storeKey(searchKey: str):
    searchKey = list(searchKey)
    query = ("INSERT INTO search_key (search_key) VALUES (\"%s\")")
    cur.execute(query, (searchKey))
    cur.connection.commit()

def insertRowIfNotExists(searchKey: str):
    searchKey = list(searchKey)
    query = ("SELECT * FROM search_key where search_key = \"%s\"")
    cur.execute(query, (searchKey))
    records = cur.fetchone()
    print(records)
    #print(f"search_key : {searchKey}")
    
   # if record == searchKey:
   #     print("This keyword already exists!")
   # else:
#    storeKey(searchKey)

#cur.close()
#conn.close()
    
url = 'https://api.datamuse.com/words'
   # params, headers = {'rel_rhy':'forgetful', 'sl':'jirraf'}, {}
params, headers, filetype = {'sl':'jirraf'}, {}, 'mysql'

res = cl.httpFetcher(url, 'get', params=params, headers = headers)
res_format = cl.formatResponse(res, "json")

#storeKey(cl.collectData(cl.getFilename(params, filetype), filetype, 'files', res_format))
insertRowIfNotExists(cl.collectData(cl.getFilename(params, filetype), filetype, 'files', res_format))
#cur.execute("SELECT * FROM search_key")
#print(cur.fetchone())
print(cur.fetchall())
cur.close()
conn.close()