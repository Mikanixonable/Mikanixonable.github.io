from bs4 import BeautifulSoup

nums = [10,11,12,13,14,15,16,17,18,19,20,23,31,39,43,44]
names = map(lambda n: str(n)+".html",nums)
for name in names:
    with open(name, mode='rt', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')


    # nt = soup.new_tag('meta', id='hoge') # 新しい要素を作る
    # nt.string = 'ほげ'

    # soup.find('head').append(nt) # UL要素を検索して追加


    if soup.find("meta") is None:
        meta = soup.new_tag("meta",genre="illust")
        soup.find("head").append(meta)
    else:
        soup.find("meta")["genre"]="illust"
    del soup.find("meta")["tag"]


    with open(name, mode='w',encoding='utf-8') as f:
        f.write(str(soup))