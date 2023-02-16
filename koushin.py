import os.path
import datetime
import json
import glob
import math

#htmlファイル名全取得
files = glob.glob("*.html")

#作成日時更新日時の取得、リスト化
dates=[] #{cdates:2023brbr, madtes:2023brbr}
for i in range(len(files)):
    path = files[i]
    #UnixTimeStamp取得
    ctime = math.floor(os.path.getctime(path))
    mtime = math.floor(os.path.getmtime(path))
    #日付化
    cdate = datetime.datetime.fromtimestamp(ctime).date()
    mdate = datetime.datetime.fromtimestamp(mtime).date()

    date_dic = {
    "name":"_"+str(files[i]).replace(".",""),
    "ctime":str(ctime),
    "mtime":str(mtime),
    "cdate":str(cdate),
    "mdate":str(mdate),
    }
    dates.append(date_dic)
    # dates.append(mtime)

#キーの拡張子を取り除き先頭に_をつける
# for i in range(len(files)):
#     files[i] = os.path.splitext(files[i])[0]
#     files[i]="_"+files[i]
##########################################################


##########################################################

# dict1 = dict(zip(files,dates))

json1 = open('./meta.json', mode="w")
json.dump(dates, json1)

json1.close()
