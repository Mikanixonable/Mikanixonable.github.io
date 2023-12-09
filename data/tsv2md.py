import csv
import chardet
from pprint import pprint 

def detect_encoding(file_path):
    # ファイルのエンコーディングを検出
    with open(file_path, 'rb') as file:
        detector = chardet.UniversalDetector()
        for line in file:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    return detector.result['encoding']

def tsv2dic(file_path):
    encoding = detect_encoding(file_path)
    with open(file_path, 'r', newline='', encoding=encoding) as file:
        reader = csv.DictReader(file, delimiter='\t')
        dic = []
        for row in reader:
            for key,value in list(row.items()):
                row[key] = row[key].split(",")
                #空なら入れない
                if value =='':
                    del row[key]
                

            #空なら入れない
            if len(row.keys()) != 0:
                dic.append(row)
        return dic

def dic2md(dic):
    md = ''
    for lang in dic:
        md += "### "+str(lang["言語名"][0])
        if "説明" in lang:
            for text in lang["説明"]:
                md += "\n　"+text
        md += "\n|基本情報||\n|---|---|"

        for key,value in list(lang.items()):
            if key != "説明":
                if key == "作者Twitter":
                    md+="\n|{k}|[@{a}]({b})|".format(k=key,a=value[0].split("com/")[1],b=value[0])
                    
                else:
                    md+="\n|{k}|{v}|".format(k=key,v=" ".join(value))
        # if len(lang["言語名"])>1:
        #     md+="\n|言語名|{}|".format("、".join(lang["言語名"]))
        # if "年代" in lang:
        #     md+="\n|年代|{}|".format(lang['年代'][0])
        # if "作者" in lang:
        #     md+="\n|作者|{}|".format("、".join(lang['作者']))
        # if "作者Twitter" in lang:
        #     md+="\n|作者Twitter|[@{a}]({b})|".format(a=lang['作者Twitter'][0].split("com/")[1],b=lang['作者Twitter'][0])
        # if "ホームページ" in lang:
        #     md+="\n|ホームページ|{}|".format(" ".join(lang['ホームページ']))
        # if "辞書" in lang:
        #     md+="\n|辞書|{}|".format(" ".join(lang['辞書']))
        # if "文法" in lang:
        #     md+="\n|文法|{}|".format(" ".join(lang['文法']))

        

        # for key in lang.keys():
        #     if 
        #     if key == "説明"
        #     print(lang[key])
        md += "\n\n"
    
    return md

dic = tsv2dic('conlang.tsv')
pprint(dic)
md = dic2md(dic)

with open("conlang.md", 'w', encoding='utf-8') as file:
    file.write(md)
