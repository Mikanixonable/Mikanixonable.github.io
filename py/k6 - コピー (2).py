#イラスト管理用のillusts.jsonを項目別のタブ区切りcsvからビルドするプログラム

import json
import glob
import os
import codecs
from PIL import Image
import pandas as pd
import csv



# range1 = (-213, 531+1)
# with open("./json/tag2.csv", "w", newline="") as f:
#     # 「delimiter」に区切り文字、「quotechar」に囲い文字を指定します
#     # quotingにはクォーティング方針を指定します（後述）
#     writer = csv.writer(f, delimiter="\t", quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     # writerowに行列を指定することで1行分を出力できます
#     for i in range(range1[0],range1[1]):
#         writer.writerow([i, []])


#date.csvファイルを扱いやすい辞書オブジェクトに加工するプログラム
#jsonに代入する前処理
csv_file_path = './json/date.csv'
dateDic = {}
with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for row in reader:
        dateDic[row[0]] = row[1]


#illustsjsonにタグ追加するプログラム
import json


jsonPath = './json/illusts2.json'
def update(png):
    img = Image.open(png)
    name = os.path.splitext(os.path.basename(png))[0]


    imgDic = {
    "name": name,
    "width": img.width,
    "height": img.height,
    "title": "",
    "description": "",

    "date":dateDic[str(name)],
    "licence":"",
    "link":"",
    "series":[],
    "tags":[],
    "colors":[],
    }
    dic.append(imgDic)

#illust辞書の作成
dic = []
pngs = glob.glob("illusts/*.png")
for png in pngs:
    update(png)

#タグ挿入
targets = [1,2,3,4,5,7]
targets = [str(target) for target in targets]
target_name = "56"  # 書き換える辞書オブジェクトのname要素の値
for item in dic:
    if "name" in item and item["name"] in targets:
        item["tags"].append("yuyu")

f = codecs.open(jsonPath, "w", "utf-8")
json.dump(dic, f, indent = 2, ensure_ascii=False)
f.close()
