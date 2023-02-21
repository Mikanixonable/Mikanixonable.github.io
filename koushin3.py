import os.path
import datetime
import json
import glob
import math
import bs4
from html.parser import HTMLParser
import codecs

#htmlファイル名全取得
files = glob.glob("*.html")

#ファイルの情報の取得、リスト化
dates=[]
for i in range(len(files)):
    path = files[i]
    #UnixTimeStamp取得
    ctime = math.floor(os.path.getctime(path))
    mtime = math.floor(os.path.getmtime(path))

    #UnixTimeStampの日付化
    cdate = datetime.datetime.fromtimestamp(ctime).date()
    mdate = datetime.datetime.fromtimestamp(mtime).date()

    #タイトルの取得、タイトルがなければファイル名を入れる
    soup = bs4.BeautifulSoup(open(path, mode= "r",encoding="utf-8"), 'html.parser')
    try: 
        title = str(soup.title.string)
    except AttributeError:
        title = "untitled"

    try: 
        content = soup.meta.get("content")
        
    except AttributeError:
        content = ""
    
    hrefs = []
    try: 
        links = soup.find_all("a")
        for link in links:
            hrefs.append(link.get("href"))
        
    except AttributeError:
        links = ""
    print(len(hrefs))
    print(type(hrefs))

    print(hrefs)


    date_dic = {
    "name":"_"+str(files[i]).replace(".",""),
    "title":title,
    "content":content,
    "ctime":str(ctime),
    "mtime":str(mtime),
    "cdate":str(cdate),
    "mdate":str(mdate),
    }
    dates.append(date_dic)


json1 = codecs.open('./meta.json', "w", "utf-8")
json.dump(dates, json1, indent = 2, ensure_ascii=False)

json1.close()
