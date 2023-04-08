#illustsjsonにタグ追加するプログラム
import json

# JSONファイルのパス
json_file_path = './json/illusts2.json'

# JSONファイルを読み込み
with open(json_file_path, 'r', encoding='utf-8') as jsonfile:
    data = json.load(jsonfile)  # JSONデータを読み込み

# 書き換える辞書オブジェクトのname要素の値を指定
target_name = "56"  # 書き換える辞書オブジェクトのname要素の値
new_age = 26  # 新しいage要素の値

# 特定のname要素を持つ辞書オブジェクトを書き換え
for item in data:
    if "name" in item and item["name"] == target_name:
        item["tags"].append("yuyu")



# JSONファイルに書き込み
with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, indent=2, ensure_ascii=False)






