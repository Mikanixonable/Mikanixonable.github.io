---
layout: top
title: 月面植物園
date: 2023-10-07 00:00:00
image: ./logo.png
categories: main
---

<blockquote>
  <p id="quote">テクノなまこ、科学の力</p>
</blockquote>

### ミクボタン（音が鳴ります）

  <div class="mikuButton">
    <button onclick="btn('./musics/1.mp3', this)">ミクボタン</button>
    <button onclick="btn('./musics/2.mp3', this)">ねう</button>
    <button class="poland" onclick="btn('./musics/3_1.mp3', this)">Mazurek Dąbrowskiego</button>
    <button onclick="btn('./musics/4.mp3', this)">ねこーっ</button>
    <button onclick="btn('./musics/5.mp3', this)">ねこねこ</button>
    <button onclick="btn('./musics/6.mp3', this)">にゃう</button>
    <button onclick="btn('./musics/7.mp3', this)">ぬい~</button>
    <button onclick="btn('./musics/21.mp3', this)">JR-SH3-3(東京駅)</button>
    <button onclick="btn('./musics/82.mp3', this)">water crown(目黒駅)</button>
  </div>

### Random Gallery

<div id="randomg"></div>
<script>
let randomg = document.getElementById("randomg");
let rand = Math.floor(Math.random()*570)+1
randomg.innerHTML = `<a href="./5.html?n=${rand}"><img src="./illusts/${rand}.png"/></a>`;
randomg.innerHTML += `<p>No: ${rand}</p>`
</script>


### About
[みかぶるについて](143)
[このサイトについて](37)
~~~javascript
let email = "Mikanixonable1" + "@" + "gmail.com";
~~~

## サイトマップ
~~~mermaid
graph TD;
  D[(ページ一覧)]
  click D "1"
  D .- pages

  G{{GitHubRepository}}
  click G "https://github.com/Mikanixonable/Mikanixonable.github.io"

  G .- D

  subgraph pages;
  direction LR
    subgraph function;
    direction LR
    I((ホーム))
    L{144\nロビー}
    click L "144"
    R[159\nラウンジ]
    click R "159"
    A[160\nアトリウム]
    click A "160"
  end

    E[129\n絵]
    click E "129"
    S[154\n写真]
    click S "154"
    M[145\n音楽]
    click M "145"
    N[146\n小説]
    click N "146"
    Con[128\n人工言語]
    click Con "128"

    E --- E1
      E1[5\n作品番号表示]
      click E1 "5"
    E ---E163
      E163[163\n赤の部屋]
      click E163 "163"
    E ---E164
      E164[164\n青の部屋]
      click E164 "164"
    
    S --- S1
    S1[155\n駅構造情報]
    click S1 "155"


    I---R
    I---L
    I---A

    L---E
    L---S
    L---M
    L---N
    L---F
    L---Con
    F[165\nフォント]
    click F "165"
    F---F1[4\nシリーズ一覧]
    click F1 "4"
    F---F2[18\nデモページ]
    click F2 "18"
  end
~~~


## コンテンツ
### function
[ページ一覧](1)
[ロビー](144)
[ラウンジ](159)
[アトリウム](160)

### 創作
[絵](129)
[写真](154)
[音楽](145)
[小説](146)
[架空世界](166)
[人工言語](128)

### リンク
[SNS](132)
[相互リンク](135)
[非相互リンク](142)


## バナー
<a href=""><img src="https://mikanixonable.github.io/banner.png" width="200" height="40" alt="月面植物園" /></a>  
> 画像: https://mikanixonable.github.io/banner.png  

>タグ: &lt;a href="">&lt;img src="https://mikanixonable.github.io/banner.png" width="200" height="40" alt="月面植物園" />&lt;/a>

このサイトはリンク自由です

## 相互リンク
[![](https://ideoaves.github.io/banner.png)](https://ideoaves.github.io/)
[mythfinder](https://haxibami.net/)
[ふぁぼんのホームページ](https://fabon.info)
[SnO2WMaN.net](https://sno2wman.net/)
[まだ相互ではないリンク](142)


## アクセスカウンター
![](https://count.getloli.com/get/@:mikanixonable)
2023-10-27設置