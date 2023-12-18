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
        reader = csv.DictReader(file, delimiter=',')
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
        if 'サイト' in lang:
            md += "### "+"[{a}]({b})".format(a=lang["言語名"][0],b=lang['サイト'][0])
        else:
            md += "### "+"{a}".format(a=lang["言語名"][0])
        if "年代" in lang:
             md += "\n年代: "+lang["年代"][0]
        if "説明" in lang:
            for text in lang["説明"]:
                md += "\n　"+text
        

        
        md+="\n"
        for key,value in list(lang.items()):
            if key not in ["説明","年代"]:
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

def dic2md2(dic):
    legends = ["年代","作者","サイト","文法","辞書","架空世界","分類"]
    md = '|言語名|年代|作者|サイト|文法|辞書|架空世界|分類|'
    md += '\n|---|---|---|---|---|---|---|---|'
    for lang in dic:
        if 'site' in lang:
            md += "\n|[{a}]({b})".format(a=lang["言語名"][0],b=lang['site'][0])
        else:
            md += "\n|{a}".format(a=lang["言語名"][0])
        


        for legend in legends:
            md +="|"
            if legend in lang:
                if lang[legend][0][0:4] == "http":
                    md +="[{a}]({b})".format(a=legend,b=lang[legend][0])
                else:
                    md +=lang[legend][0]
            else:
                md+=' '
        
        md+="|"
    
    return md

def dic2md3(dic):
    md = '|言語名|活動年代|作者|'
    md += '\n|---|---|---|'
    for lang in dic:
        aa = ''
        if 'サイト' in lang:
            aa += "[{a}]({b})".format(a=lang["言語名"][0],b=lang['サイト'][0])
        else:
            aa += "{a}".format(a=lang["言語名"][0])

        a = lang['年代'][0]


        b = ''
        if '作者' in lang:
            if '作者Twitter' in lang:
                b += '[{a}]({b})'.format(a=lang['作者'][0],b=['作者Twitter'][0])
            else:
                b += lang['作者'][0]
        # if '説明' in lang:
        #     b += lang['説明'][0]
        
        c = ''
        if 'サイト' in lang:
            if len(lang['サイト'])>2:
                for i in range(len(lang['サイト']) - 1):
                    c+= '([サイト{i}]({a}))'.format(i=str(i+2),a = lang['サイト'][i+1])
        if '文法' in lang:
            c += '([文法]({a}))'.format(a = lang['文法'][0])
            
        if '文法' in lang:
            if len(lang['文法'])>2:
                for i in range(len(lang['文法']) - 1):
                    c+= '([文法{i}]({a}))'.format(i=str(i+2),a = lang['文法'][i+1])
        
        if '辞書' in lang:
            c += '([辞書]({a}))'.format(a = lang['辞書'][0])

        if '辞書' in lang:
            if len(lang['辞書'])>2:
                for i in range(len(lang['辞書']) - 1):
                    c+= '([辞書{i}]({a}))'.format(i=str(i+2),a = lang['辞書'][i+1])


        md +="\n|{a}     {d}|{b}|{c}|".format(a=aa,b=a,c=b,d=c)


        # if legend in lang:
        #     if legend
        #     if lang[legend][0][0:4] == "http":
        #         md +="[{a}]({b})".format(a=legend,b=lang[legend][0])
        #     else:
        #         md +=lang[legend][0]
        # else:
        #     md+=' '
        
        md+="|"
    
    return md


md = """

# 日本語圏人工言語リスト(2023年12月)
　日本語圏の人工言語のリストが最近作られていないと思ったので、底となるリストを参考に、新しい言語も合わせてつくったものです。リストのすべての言語の情報は私がアクセスして確認しなおしています。
　このリストは後で作るリストのための下準備という位置づけで、人工言語として言及されているものは見つけ次第すべて入れています。そのため、創作世界の設定に名前だけ登場するような言語や、ツイッター上で思い付きで作られた言語も含んでいます。
　言語の説明やCLAコードの入った生データは以下のリンクからアクセスできます。tsv(タブ区切り値)形式であり、Excelから開けます。私は著作権を放棄するので、利用したい方は使ってください。
https://mikanixonable.github.io/data/conlang.tsv

追記 utf-8でcsv形式に書き直しました
https://mikanixonable.github.io/data/conlang.csv

## 底としたリスト
- [人工言語リスト 日本人による人工言語（アイウエオ順）](http://dos.chottu.net/conlang_link.html?l=index) - 2nd LVG IMG.The Second Living Image.
2004年

- [人工言語リンク集](https://conlinguistics.org/link.html) - 人工言語学
2012年

- [言語記事一覧](https://conlinguistics.fandom.com/ja/wiki/%E8%A8%80%E8%AA%9E%E8%A8%98%E4%BA%8B%E4%B8%80%E8%A6%A7) - 人工言語wiki
2016年ごろと思われる

- [人工言語界隈リスト](https://itest.5ch.net/test/read.cgi/twwatch/1513511369/) - 5ch
2017-12-17

- [人工言語を作ってるor勉強してる人が少し分かるリスト](https://docs.google.com/spreadsheets/d/1t_WxHJ_b39PWXIMauHwnSww_Ac2m_Mw7zC-vQkp59PQ/edit#gid=0) - Maycia Arenberg
2018-02-24
現在はリクエスト承認が必要という表示が出る
[紹介ツイート](https://x.com/mayciaarenberg/status/963447200087879680?s=46&t=rWvY73qZa5Ie23yU0UA6WA)
[人工言語クラスタフォロー](https://twitter.com/jin_kou_gengo)というこのリストに入っていたアカウントをフォローするアカウントがあったため、少し漏れがあるがリストを復元することができる。@2me_ma_sagiさんありがとう

- [辞書リスト](http://twoc.ever.jp/twoc/conlang.cgi?mode=list) - The world of conlangs
 2020年ごろ

- [人工言語リスト](https://sites.google.com/site/moyacilang/conlanglist) - slaimsan
たぶんもっとも網羅的
2020年

- [リンク集 人工言語](https://ziphil.com/other/other/1.html) - Ziphil
文法が確認できるものに絞って載せている
2021年3月

- [conlanger](https://x.com/i/lists/994189952551346176) - Mikanixonable
私みかぶるが手当たり次第人工言語作者っぽい人を入れているツイッターの人工言語ラーのリスト
2023年

- [架空言語](https://tanukipedia.miraheze.org/wiki/%E6%9E%B6%E7%A9%BA%E8%A8%80%E8%AA%9E) - Tanukipedia (タヌキペディア) 
2023年

- [人工言語 柳霞](https://sites.google.com/view/ryuuka/k-ren-gong-yan-yurinku-ji?authuser=0) - J．人工言語リンク集
2020年ごろ?

- [架空の言語一覧](https://japan.fandom.com/wiki/%E6%9E%B6%E7%A9%BA%E3%81%AE%E8%A8%80%E8%AA%9E%E4%B8%80%E8%A6%A7) - 架空の言語一覧 | Japan | Fandom

- [アーカイブ](https://w.atwiki.jp/kakis/pages/5471.html#id_1b7f8ccd) - atwiki（アットウィキ） 

- [Faras' Room](https://sites.google.com/site/faraspalt/links?authuser=0 ) - Links 

- [アルカ-リンク](https://w.atwiki.jp/kursodeesperanto/pages/36.html) - はじめてのエスペラント - atwiki（アットウィキ）  

- [世界模擬実験塔設定集](https://w.atwiki.jp/koreori/) - atwiki（アットウィキ） 
"""

dic = tsv2dic('conlang.csv')
for lang in dic:
    if '年代' not in lang:
        print(lang['言語名'])
dic = sorted(dic, key=lambda x: int(x['年代'][0][0:4]))
pprint(dic)


md +="""
## 人工言語リスト
"""
md += dic2md3(dic)

md += """

2023年12月 Mikanixonable
"""

with open("conlang.md", 'w', encoding='utf-8') as file:
    file.write(md)
