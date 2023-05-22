#イラスト管理用のillusts.jsonを項目別のタブ区切りcsvからビルドするプログラム

import json
import glob
import os
import codecs
from PIL import Image
# import pandas as pd
import csv


deskPath = "./Mikanixonable.github.io/"
jsonPath = deskPath + 'json/illusts5.json'
def makeCSV(filename,nums):
  
    illustRange = (min(int(nums)), max(int(nums)))
    csvPath = deskPath + "./json/" + filename
    with open(csvPath, "w", newline="") as f:
        writer = csv.writer(f, delimiter="\t", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(illustRange[0],illustRange[1]+1):
            writer.writerow([i, []])

#date.csvファイルを扱いやすい辞書オブジェクトに加工するプログラム
#jsonに代入する前処理
def csv2dic(filename):
    csv_file_path = deskPath + filename
    dateDic = {}
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            dateDic[row[0]] = row[1]

    return dateDic



#illustsjsonにタグ追加するプログラム

#illust辞書の作成
# dic = []
# pngs = glob.glob(deskPath + "illusts/*.png")
# for png in pngs:
    # update(png)

#タグ挿入
# targets = [1,2,3,4,5,7]
# targets = [str(target) for target in targets]
# target_name = "56"  # 書き換える辞書オブジェクトのname要素の値
# for item in dic:
#     if "name" in item and item["name"] in targets:
#         item["tags"].append("yuyu")

# f = codecs.open(jsonPath, "w", "utf-8")
# json.dump(dic, f, indent = 2, ensure_ascii=False)
# f.close()

# def main():

# def main(numList,illusts):
#     for illust in illusts:
#         img = Image.open(illust[])
#         num = os.path.splitext(os.path.basename(illust))[0]


#         imgDic = {
#         "name": num,
#         "width": img.width,
#         "height": img.height,
#         "title": "",
#         "description": "",

#         "date":dateDic[str(num)],
#         "licence":"",
#         "link":"",
#         "series":[],
#         "tags":[],
#         "colors":[],
#         }
#         dic.append(imgDic)

# def main(numList,illusts):

def main():
    nums = [os.path.splitext(os.path.basename(png))[0] for png in glob.glob(deskPath + "illusts/*.png")]
    
    #減少分更新
    for illust in illusts:
        if illust["num"] not in nums:
            del illust
    #増加分更新
    for num in nums:
        if num not in dicNums:
            illusts.append({
                "num":num
                           })
    #基本情報の追加
    
    for illust in illusts:
        imgPath = deskPath + "illusts/" + illust["num"] + ".png"
        img = Image.open(imgPath)
       
        illust["width"] = img.width
        illust["height"] = img.height
        illust["size"] = os.path.getsize(imgPath)

    #csv insert
    dateDic = csv2dic('json/date.csv')
    tagDic = csv2dic("json/tag.csv")
    for illust in illusts:
        illust["date"] = dateDic[illust["num"]]
    
    #特定の要素削除
    # for illust in illusts:
    #     delKey = "byte"
    #     try :
    #         del illust[delKey]
    #     except KeyError :
    #         print('存在しないキーです')

    # #csv make
    # makeCSV("tag2.csv",nums)

if os.path.isfile(jsonPath):
    f = codecs.open(jsonPath, "r", "utf-8")
    illusts = json.load(f)
    dicNums = [illust.get('num') for illust in illusts]
    f.close()
else:
    illusts = []
    dicNums = []


main()

f = codecs.open(jsonPath, "w", "utf-8")
json.dump(illusts, f, indent = 2, ensure_ascii=False)
f.close()
