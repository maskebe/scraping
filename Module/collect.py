#Author : Mamadou Seybane KEBE
#Student at Dakar Institute of Technology
# 2022.06.03
################################################################

from multiprocessing.dummy import Value
from importlib_metadata import files
from nbformat import write
import requests
import json
import pandas as pd
import mysql.connector
import xlsxwriter
from mysql.connector import Error

link = ''

#function to fetch http params and header
def httpFetcher(url : str, methode : str, params = None, headers = None):
    #alias the active session as session faster than the old way
    with requests.Session() as session:
        #get the response
        res = session.get(url, params = params, headers = headers)
        return res

#function to format the response
def formatResponse(res, format : str):
    if format == 'json':
        return res.json()
    return res.text()

#function to create a file to stock the content from the API
def collectData(filename : str, filetype: str, filepath : str, res):
    filetype = filetype.lower()
    data = json.dumps(res, indent = 4)
    df = pd.DataFrame(eval(data))
    #print(data)
    if filetype == 'csv':
        #file = open(filepath + '\\' + filename, "w")
        #file.write(data)
        #file.close()
        df.to_csv(filepath + '\\' + filename)
    elif filetype == 'xlsx':        
        df.to_excel(filepath + '\\' + filename, index=False)
    elif filetype == 'mysql' or filetype == 'postgres' or filetype == 'oracle':
        #print(filename)
        return filename
    else:
        print(f"{filetype} is not supported by this package.")
#function to get filename from params
def getFilename(params : dict, filetype : str):
   if filetype == 'csv' or filetype == 'xlsx' or filetype == 'txt':
       for key in params:
           filename = params.get(key) + '.' + filetype
           return filename
   elif filetype == 'mysql' or filetype == 'postgres' or filetype == 'oracle':
       for key in params:
           filename = params.get(key)
          # print(filename)
           return filename
   else:
        print(f"{filetype} is not supported by this package.")
        

def connectToMysql(hostname : str, database : str, username : str, password :str):
    try:
        connection = mysql.connector.connect(host=hostname,
                                         database=database,
                                         user=username,
                                         password=password)
        return connection
    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))
   
if __name__ == '__main__':
    url = 'https://api.datamuse.com/words'
   # params, headers = {'rel_rhy':'forgetful', 'sl':'jirraf'}, {}
    params, headers, filetype = {'ml':'breakfast'}, {}, 'mysql'

    res = httpFetcher(url, 'get', params=params, headers = headers)
    res_format = formatResponse(res, "json")
    #print(res_format)
   # print(getFilename(params, 'csv'))
    #getFilename(params)
    collectData(getFilename(params, filetype), filetype, 'files', res_format)
    #print(connectToMysql('localhost', 'testapi', 'testapi', 'testapi123'))
   # saveToDatabase('search_key', params=params)