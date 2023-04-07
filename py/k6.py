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


# CSVファイルのパス
csv_file_path = './json/tags.csv'

# 書き換える行のインデックスと新しい値を指定
row_index = 2  # 書き換える行のインデックス (0から始まる)
new_value = 'new_value'  # 新しい値

# CSVファイルを読み込み、指定された行の値を書き換え
with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]  # CSVの各行をリストとして取得

    if row_index < len(rows):
        # 指定された行の値を書き換え
        rows[row_index][0] = new_value

# CSVファイルを上書き保存
with open(csv_file_path, 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)

print(f"行 {row_index} の値を書き換えました: {new_value}")




# タブ区切りCSVファイルのパス
csv_file_path = './json/date.csv'

# 辞書オブジェクトを格納する変数
dateDic = {}

# CSVファイルを読み込み、辞書オブジェクトを作成
with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for row in reader:
        # 一列目をキー、二列目を値として辞書に追加
        dateDic[row[0]] = row[1]

# print(my_dict)
# print(dateDic["1"])


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


dic = []
pngs = glob.glob("illusts/*.png")
for png in pngs:
    update(png)

f = codecs.open('./json/illusts.json', "w", "utf-8")
json.dump(dic, f, indent = 2, ensure_ascii=False)
f.close()
