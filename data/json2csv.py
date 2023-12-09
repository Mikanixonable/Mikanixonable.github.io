import json
import csv
import re

# JSONファイルのパス
json_file_path = './tweets.json'

with open(json_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# CSVファイルに書き込む
csv_file_path = './tweets.csv'
csv_columns = ['tweet']  # 取得したいキーを指定

# pattern = re.compile(r'(.*wikipedia.*)')
# print(bool(pattern.match("yui lhttps://t.co/KxpOn5eqOT")))
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
    writer.writeheader()
    for tweet in data:
        # 各ツイートから"text"キーの値を取得しCSVに書き込む
        # if bool(pattern.match(tweet["tweet"]["full_text"])):
        # if "wikipedia" in tweet["tweet"]["full_text"]:
        # if tweet["tweet"]["source"] == "<a href=\"https://www.hootsuite.com\" rel=\"nofollow\">Hootsuite Inc.</a>":
            writer.writerow({'tweet': tweet["tweet"]["full_text"]})

