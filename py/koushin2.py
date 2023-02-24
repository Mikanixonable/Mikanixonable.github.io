import os.path
import datetime
import json
import glob
import math
import bs4
import codecs
import random
import math
import time
import numpy as np

backgroundColor="#ddd"
color1 = "#3bb"
color2 = "#623"

def colorMixer(c1,c2,k):
    a = [int(c1[1],16),int(c1[2],16),int(c1[3],16)];
    b = [int(c2[1],16),int(c2[2],16),int(c2[3],16)];
    c = [a[0]*(1-k)+b[0]*k,a[1]*(1-k)+b[1]*k,a[2]*(1-k)+b[2]*k];
    c3 = "#"+hex(math.floor(c[0]))[2:]+hex(math.floor(c[1]))[2:]+hex(math.floor(c[2]))[2:];
    return c3

#htmlファイル名全取得
files = glob.glob("*.html")
print(files)

#ファイルの情報の取得、リスト化
dates=[]
# graphs={
#     "nodes" : [],
#     "edges" : []
# }
nodes = []
links = []

size = []
for file in files:
    soup = bs4.BeautifulSoup(open(file, mode= "r",encoding="utf-8"), 'html.parser')
    size.append(len(str(soup)))


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


    lapse = int(time.time())-mtime #経過秒数
    lapse = lapse/1000000
    grad = 1-math.exp(-lapse*(1/2));
    dotcolor = colorMixer(color1,color2,grad)


    #グラフ描画用、頂点####################################
    node_dic = {
    "id":"_"+str(files[i]).replace(".",""),
    # "label":"<"+str(files[i].replace(".html",""))+">"+title,
    "label":str(files[i].replace(".html","")),
    "x": random.gauss(0,1),
    "y": random.gauss(0,1),
    "size": (len(str(soup))/max(size))**(0.5)*3+2,
    "url": "1.html",
    
    "type": "image",
    "image": "e.svg",
    "color": "BLUE"

    }
    nodes.append(node_dic)

    #グラフ描画用、辺
    hrefs = []
    try: 
        #タグ付きのリンクリスト
        links1 = soup.find_all("a") 

        #タグなしのリンクリスト
        urls = []
        for link in links1:
            urls.append(link.get("href")) 

        #タグなしのリンクリスト(重複なし)
        urls = list(set(urls))
        for url in urls:
            if url in files:
                hrefs.append(url)
    except AttributeError:
        links1 = ""

    # coe = (1-math.exp(-(len(urls)-1))) #1toInf->0to1
    coe =len(urls)
    if coe > 20:
        coe = 20

    edge_color = colorMixer(dotcolor,backgroundColor,coe/20*0.9)

    # +hex(math.floor((1-coe/20)*15+1))[2:]

    for k in range(len(hrefs)):
        edge_dic = {
        # "id":"_"+str(files[i]).replace(".","")+"_"+str(k).replace(".",""),
        # "source":"_"+str(files[i]).replace(".",""),
        # "target":"_"+str(k).replace(".",""),
        "source": i,
        "target": k,
        # "label":"_"+str(files[i]).replace(".","")+"_"+str(k).replace(".",""),
        # "label":"r",
        

        # "size": (len(str(soup))/max(size))*30,
        # "size": 5,

        # "color": edge_color,

        # "type": 'curvedArrow',
        # "type": 'arrow',
        }
        links.append(edge_dic)
        


json1 = codecs.open('./json/meta.json', "w", "utf-8")
json.dump(dates, json1, indent = 2, ensure_ascii=False)
json1.close()

#jsonで出力する古いプログラム
# json2 = codecs.open('./json/meta2.js', "w", "utf-8")
# json.dump(graphs2, json2, indent = 2, ensure_ascii=False)
# json2.close()

#js形式
graphs2 = "var nodes = "+ str(nodes)
graphs3 = "var links = "+ str(links)
with codecs.open('./js/meta2.js',"w","utf-8") as o:
    print(graphs2, file = o)
    print(graphs3, file = o)