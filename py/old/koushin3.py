import codecs
# テキストファイルを読み込む
with codecs.open('1.txt', 'r',"utf-8") as f:
    text = f.read()

# HTMLコードを文字列として作成する
html_code = '''
<!DOCTYPE html>
<html>
<head>
	<title>My Website</title>
</head>
<body>
	<h1>My Text File</h1>
	<p>{}</p>
</body>
</html>
'''.format(text)

# ファイルを開き、HTMLコードを書き込む
with codecs.open('90.html', 'w',"utf-8") as f:
    f.write("<DOCTYPE html>")
    f.write("<head>")
    f.write("<html lang='ja'>")
    f.write("</head>")
    f.write("<body>")
    f.write("</body>")
    f.write("</html>")
    f.write(html_code)

# ファイルを閉じる
f.close()
