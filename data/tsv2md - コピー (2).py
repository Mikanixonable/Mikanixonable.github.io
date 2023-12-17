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
        if 'site' in lang:
            md += "### "+"[{a}]({b})".format(a=lang["言語名"][0],b=lang['site'][0])
        else:
            md += "### "+"{a}".format(a=lang["言語名"][0])
        if "era" in lang:
             md += "\n年代: "+lang["era"][0]
        if "説明" in lang:
            for text in lang["説明"]:
                md += "\n　"+text
        

        
        md+="\n"
        for key,value in list(lang.items()):
            if key not in ["説明","era"]:
                # md+="\n"
                if key == "作者Twitter":
                    md+="作者Twitter: [@{a}]({b}) ".format(k=key,a=value[0].split("com/")[1],b=value[0])
                elif value[0][0:4] == "http":
                     for i,elm in enumerate(value): 
                        index = str(i+1)
                        if i == 0:
                            index = ""
                        md+="[{k}]({v}) ".format(k=str(key)+str(index),v=elm)
                else:
                    md+="{k}: {v}".format(k=key,v=" ".join(value))
        md += "\n\n"
    
    return md

dic = tsv2dic('conlang.tsv')
pprint(dic)
md = dic2md(dic)

with open("conlang.md", 'w', encoding='utf-8') as file:
    file.write(md)
