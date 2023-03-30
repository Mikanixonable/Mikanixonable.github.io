from bs4 import BeautifulSoup

# nums = [10,11,12,13,14,15,16,17,18,19,20,23,31,39,43,44]
nums = [4,49,41,54,120,121,122,123,123,125,126,127,128,129,130]
genre = "font"
names = map(lambda n: str(n)+".html",nums)
for name in names:
    with open(name, mode='rt', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')


    # nt = soup.new_tag('meta', id='hoge') # 新しい要素を作る
    # nt.string = 'ほげ'

    # soup.find('head').append(nt) # UL要素を検索して追加


    if soup.find("meta") is None:
        meta = soup.new_tag("meta",genre=genre)
        soup.find("head").append(meta)
    else:
        soup.find("meta")["genre"]=genre



    with open(name, mode='w',encoding='utf-8') as f:
        f.write(str(soup))