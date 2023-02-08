import os.path
import datetime
import json
import glob

#htmlファイル名全取得
files = glob.glob("*.html")

#作成日時更新日時の取得、リスト化
dates=[] #{cdates:2023brbr, madtes:2023brbr}
for i in range(len(files)):
    path = files[i]
    #UnixTimeStamp取得
    ctime = os.path.getctime(path)
    mtime = os.path.getmtime(path)
    #日付化
    cdate = datetime.datetime.fromtimestamp(ctime).replace(microsecond=0)
    mdate = datetime.datetime.fromtimestamp(mtime).replace(microsecond=0)

    date_dic = {
    "ctime":str(ctime),
    "mtime":str(mtime),
    "cdate":str(cdate),
    "mdate":str(mdate),
    }
    dates.append(date_dic)
    # dates.append(mtime)

#キーの拡張子を取り除き先頭に_をつける
for i in range(len(files)):
    files[i] = os.path.splitext(files[i])[0]
    files[i]="_"+files[i]
##########################################################


##########################################################

dict1 = dict(zip(files,dates))
# dict2 = dict(zip(files,dates))

json1 = open('./meta.json', mode="w")
json.dump(dict1, json1)

json1.close()
