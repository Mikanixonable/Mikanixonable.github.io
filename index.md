---
layout: top
title: 月面植物園
date: 2023-10-07 00:00:00
image: ./logo.png
categories: main
---



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

### 音楽再生コーナー

<div class="musicButton">
<button onclick="btn('./musics/11.mp3', this)">きのこの森での記録</button>
<button onclick="btn('./musics/22.mp3', this)">恒星間播種船のテーマ</button>
<button onclick="btn('./musics/19.mp3', this)">時計台</button>
</div>

<div class="musicButton">
<button onclick="btn('./musics/8.mp3', this)">pikopiko tune</button>
<button onclick="btn('./musics/9.mp3', this)">人のいない美術館</button>
<button onclick="btn('./musics/10.mp3', this)">warabimochi</button>
<button onclick="btn('./musics/12.mp3', this)">game music 1</button>
<button onclick="btn('./musics/13.mp3', this)">雨</button>
<button onclick="btn('./musics/14.mp3', this)">土曜日のテーマ</button>
<button onclick="btn('./musics/15.mp3', this)">piano matrix</button>
<button onclick="btn('./musics/16.mp3', this)">piano matrix2</button>
<button onclick="btn('./musics/17.mp3', this)">Tetete</button>
<button onclick="btn('./musics/18.mp3', this)">台風のうた</button>
<button onclick="btn('./musics/20.mp3', this)">対流圏</button>
</div>

ミクボタンの流用。このボタンのJavaScriptは[ここ](https://mikanixonable.hatenablog.com/entry/2023/10/08/171856)にある、ほとんど全部ChatGPTに書いてもらった

[他の音楽](145)

### Random Gallery(クリックで詳細に飛びます)

<div id="randomg"></div>
<script>
let randomg = document.getElementById("randomg");
let rand = Math.floor(Math.random()*570)+1
randomg.innerHTML = `<a href="./5.html?n=${rand}"><img src="./illusts/${rand}.png"/></a>`;
randomg.innerHTML += `<p>No: ${rand}</p>`
</script>

## コンテンツ
### About
[みかぶるについて](143)　自己紹介のような文章
[このサイトについて](37)　サイト史

### function
[ページ一覧](1)　すべてのページとその新しさ加減が見れる
[ロビー](144)　とりあえずいろいろのリンクはここにまとめてある

### 創作
[絵](129)　pixivの方が見やすい
[音楽](145)　再生ボタンが並ぶ
[人工言語](128)　記事はmigdalにもある。ehtaplenチートシートや日本の人工言語関連リンクリストがある
[フォント](165)
[写真](154)
[小説](146)　kakuyomuの抜粋
[架空世界](166)　未整備
[SNS一覧](132)　トップページ上部に載せきれない網羅的な各サービスへのリンク


## サイト構造
実際はもっと大量のページがある

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


## Now Listening
![Alt text](https://spotify-recently-played-readme.vercel.app/api?user=cjsdijim4zllci0624b1wbak2)
powerd by Spotify Recently Played README Generator

[みかぶるspottify](https://open.spotify.com/user/cjsdijim4zllci0624b1wbak2)

## GitHubの芝生
![](https://ghchart.rshah.org/mikanixonable)
powerd by GitHub Chart API
[GitHub](https://github.com/Mikanixonable)

## バナー
<a href=""><img src="https://mikanixonable.github.io/banner.png" width="200" height="40" alt="月面植物園" /></a>  
画像: https://mikanixonable.github.io/banner.png  

タグ: &lt;a href="">&lt;img src="https://mikanixonable.github.io/banner.png" width="200" height="40" alt="月面植物園" />&lt;/a>

このサイトはリンク自由です

## 相互リンク
[notolitary](https://notolyte.github.io/)
[![](https://ideoaves.github.io/banner.png)](https://ideoaves.github.io/)
[mythfinder](https://haxibami.net/)
[ふぁぼんのホームページ](https://fabon.info)
[SnO2WMaN.net](https://sno2wman.net/)

[相互リンク](135)
[まだ相互ではないリンク](142)

↓ネットワークグラフ

~~~mermaid
graph TD;
A{Mikanixonable.github.io}
click A Mikanixonable.github.io
  A <--> I
  A <--> H
  A <--> F
  A <--> S
  A <--> No

  subgraph direct;
  direction TB
    A
    I
    H
    F
    S
    No
  end

No((notolyte.github.io))
click No "https://notolyte.github.io/"
  

I((ideoaves.github.io))
click I "https://ideoaves.github.io"



F((fabon.info))
click F "https://fabon.info"

  F <--> sueakiyama.github.io

  F <--> S
  F <--> taisa.site
  click taisa.site "https://taisa.site"

    taisa.site <----> hakariuri.blog
    click hakariuri.blog "https://hakariuri.blog"
      hakariuri.blog <--> tommytestpage.ie-yasu.com

    taisa.site <---> tommytestpage.ie-yasu.com
    click tommytestpage.ie-yasu.com "https://tommytestpage.ie-yasu.com"

  F <---> tommytestpage.ie-yasu.com
  F <---> gitdmnt.github.io

H((haxibami.net))
click H "https://haxibami.net"

    H <--> F
    H <--> S
    H <--> N

    H <--> fuku.day
    click fuku.day "https://fuku.day"

    H <--> donabe8898.dev
    click donabe8898.dev "https://donabe8898.dev"
    H <---> Y

    H <--> charlotteace.github.io
    click charlotteace.github.io "https://charlotteace.github.io/"

      charlotteace.github.io <--> sueakiyama.github.io
      click sueakiyama.github.io "https://sueakiyama.github.io/"
       sueakiyama.github.io <--> comphand.pages.dev
       click comphand.pages.dev "https://comphand.pages.dev/"

      charlotteace.github.io <--> gitdmnt.github.io
      click gitdmnt.github.io "https://gitdmnt.github.io/"
      
 

S((sno2wman.net))
click S "https://sno2wman.net"
    S <---> N
    S <--> okkaradon.com
    S <--> fuku.day

    S <--> shigu.jp
    click shigu.jp "https://shigu.jp"
      shigu.jp <--> D

    S <-->  rz7.dev
    click rz7.dev "https://rz7.dev"
      rz7.dev <--> shigu.jp
      rz7.dev <--> blog.gattxxa.org
      rz7.dev <--> laynor.me

    S <--> D

        blog.gattxxa.org <--> D
        click blog.gattxxa.org "https://blog.gattxxa.org"

        blog.gattxxa.org <--> shigu.jp
        
        click laynor.me "https://laynor.me"
      
    S --> uynet.work
    click uynet.work "https://uynet.work/"

      uynet.work <--> owarino.xyz
      click owarino.xyz "https://owarino.xyz/"

    S --> ryota-ka.me
    click ryota-ka.me "https://ryota-ka.me"

    S <--> gfngfn.github.io
    click gfngfn.github.io "https://gfngfn.github.io/ja/"

    S <--> xeiaso.net
    click xeiaso.net "https://xeiaso.net"
    S <--> rinsuki.net
    click rinsuki.net "https://rinsuki.net"


D[dekameshi.com]
click D "https://dekameshi.com"

  D <--> laynor.me

  D <------> rinsuki.net

  D <----> kewiihai.com
  click kewiihai.com "https://kewiihai.com"

  D <-----> do.un0.me
  click do.un0.me "https://do.un0.me"

  D <------> okkaradon.com
  click okkaradon.com "https://okkaradon.com"

  D <-------> rz7.dev






N[not-miso-inside.netlify.app]
click N "https://not-miso-inside.netlify.app"

Y[yude.jp]
click Y "https://yude.jp"
    rz7.dev <--------> Y
    Y <----> fuku.day
    fuku.day <---> s7tya.com
    click s7tya.com "https://s7tya.com"
    fuku.day <--> abap34.com
    click abap34.com "https://abap34.com"

    Y <---> E
    Y <----> nona-takahara.github.io
    click nona-takahara.github.io "https://nona-takahara.github.io"
      nona-takahara.github.io <--> myanosasa.github.io
      click myanosasa.github.io "https://myanosasa.github.io/"

    Y <----> pepepper.net
    click pepepper.net "https://pepepper.net"

    Y <-----------> arkw.net/en
    click arkw.net/en "https://arkw.net/en"

      arkw.net/en <---> yotiosoft.com
      click yotiosoft.com "https://yotiosoft.com/"
        yotiosoft.com <--> hirokitv2009.wixsite.com
        click hirokitv2009.wixsite.com "https://hirokitv2009.wixsite.com/black-mask-man"

        yotiosoft.com <--> hsp.tv

      arkw.net/en <----> nona-takahara.github.io

      arkw.net/en <-----> bvetk.arkw.net
      click bvetk.arkw.net "https://bvetk.arkw.net/"

      arkw.net/en <------> pass-case.com
      click pass-case.com "https://pass-case.com/"

      arkw.net/en <-------> hsp.tv
      click hsp.tv "https://hsp.tv/"

        hsp.tv <--> onionsoft.net
        click onionsoft.net "https://www.onionsoft.net/"

      arkw.net/en <--------> shinohara03.starfree.jp
      click shinohara03.starfree.jp "http://shinohara03.starfree.jp/"

      arkw.net/en <---------> uotaka.hamazo.tv
      click uotaka.hamazo.tv "https://uotaka.hamazo.tv/"

      arkw.net/en <---> ramlife.net
      click ramlife.net "https://ramlife.net/"

      arkw.net/en <----> wizforest.com
      click wizforest.com "https://www.wizforest.com/"

      arkw.net/en <----> kusoft.moo.jp
      click kusoft.moo.jp "https://kusoft.moo.jp/"

      

    Y <-----> kris.fail
    click kris.fail "https://kris.fail"
    Y <--> qqey.net
    Y <--> yank-nvim.com

    Y <---------> kusaremkn.com
    click kusaremkn.com "https://kusaremkn.com"
    kusaremkn.com <-----> qqey.net
    click qqey.net "https://qqey.net"
    kusaremkn.com <----> pepepper.net
    click pepepper.net "https://pepepper.net"

    kusaremkn.com <---> moyashim-25.com
    click moyashim-25.com "https://moyashim-25.com"

    kusaremkn.com <--> donabe8898.dev
    click donabe8898.dev "https://donabe8898.dev"

    kusaremkn.com <--> ajinori.f5.si
    click ajinori.f5.si "https://ajinori.f5.si/"

      ajinori.f5.si <--> 777shuang.github.io
      ajinori.f5.si <--> sasakulab.com
      ajinori.f5.si <--> yank-nvim.com
      ajinori.f5.si <--> taboroom.html.xdomain.jp
      click taboroom.html.xdomain.jp "http://taboroom.html.xdomain.jp/"


      click 777shuang.github.io "https://777shuang.github.io/"
        777shuang.github.io <---> pepepper.net
        777shuang.github.io <---> yank-nvim.com

        777shuang.github.io <---> tmksoft.net
        click tmksoft.net "https://tmksoft.net"
          tmksoft.net <---> gbudou.com

          tmksoft.net <---> nekokawa.net
          click nekokawa.net "https://nekokawa.net/"

          tmksoft.net <---> rumi-room.net
          click rumi-room.net "https://rumi-room.net/"

            rumi-room.net <--> 256server.com
            click 256server.com "https://256server.com/"

              256server.com <--> azusa.libertia-net.com
              click azusa.libertia-net.com "https://azusa.libertia-net.com/"

                  azusa.libertia-net.com <--> hakurei.win
                  click hakurei.win "https://hakurei.win/"

                    hakurei.win <--> hassy1216.github.io
                    click hassy1216.github.io "https://hassy1216.github.io/"

                      hassy1216.github.io <--> rumi-room.net

                256server.com <--> m1ntooo.com
                click m1ntooo.com "https://m1ntooo.com/"
                  m1ntooo.com <--> ame-x.net
                  click ame-x.net "https://www.ame-x.net/home"

                  m1ntooo.com <--> hakurei.win

                  m1ntooo.com <--> rumiserver.com
                  click rumiserver.com "https://rumiserver.com/"
                    rumiserver.com <--> hakurei.win

                  m1ntooo.com <--> da-tenshi.github.io

                  click da-tenshi.github.io "https://da-tenshi.github.io/WebSite/"
                    da-tenshi.github.io <--> hakurei.win

                  m1ntooo.com <--> azusa.libertia-net.com

            rumi-room.net <--> hassy1216.github.io
            rumi-room.net <--> massangooo.net
            click massangooo.net "https://massangooo.net/"

              massangooo.net <--> hassy1216.github.io
              massangooo.net <--> m1ntooo.com


            rumi-room.net <--> azusa.libertia-net.com
            rumi-room.net <--> nekokawa.net

          


        777shuang.github.io <---> gbudou.com
        click gbudou.com "https://gbudou.com/"

          gbudou.com <---> shinkhun.web.fc2.com
          click shinkhun.web.fc2.com "https://shinkhun.web.fc2.com/"

          gbudou.com <---> caymankun.us.to
          click caymankun.us.to "https://caymankun.us.to/"

            caymankun.us.to <--> shinkhun.web.fc2.com

            caymankun.us.to <---> activetk.jp
            click activetk.jp "https://www.activetk.jp/"

              activetk.jp <--> 256server.com

              activetk.jp <--> kobakoo.com
              click kobakoo.com "https://www.kobakoo.com/"

              activetk.jp <--> ichiru-game.com
              click ichiru-game.com "https://ichiru-game.com/"

              activetk.jp <--> m1ntooo.com
              activetk.jp <--> nakasyou.github.io
              activetk.jp <--> morishous.f5.si
              click morishous.f5.si "https://morishous.f5.si/"

                morishous.f5.si <--> dhmo.xyz
                click dhmo.xyz "https://dhmo.xyz/"

                morishous.f5.si <--> chariot-lab.com
                click chariot-lab.com "https://chariot-lab.com/"

              activetk.jp <--> choko1229.net
              click choko1229.net "https://www.choko1229.net/"

              activetk.jp <--> xely.net
              click xely.net "https://xely.net/"

              activetk.jp <--> けびん.jp
              click けびん.jp "https://xn--08j8cqe.jp/"

              activetk.jp <--> p-nutsk.github.io
              click p-nutsk.github.io "https://p-nutsk.github.io/"

                p-nutsk.github.io <--> harusamemelon.github.io
                click harusamemelon.github.io "https://harusamemelon.github.io/"
                  harusamemelon.github.io <--> nakasyou.github.io

                p-nutsk.github.io <--> nakasyou.github.io
                click nakasyou.github.io "https://nakasyou.github.io/"
                
        ajinori.f5.si <--> sasakulab.com
        click sasakulab.com "https://sasakulab.com/"
          sasakulab.com <--> kusaremkn.com
          sasakulab.com <--> pepepper.net
          sasakulab.com <--> sites.google.com/view/happy-busy <--> Y
          click sites.google.com/view/happy-busy "https://sites.google.com/view/happy-busy/"

          sasakulab.com <--> yank-nvim.com
          click yank-nvim.com "https://www.yank-nvim.com/"
            yank-nvim.com <---> gbudou.com

          





    Y <--> sasakulab.com


      
      



    Y <----> donabe8898.dev
    click donabe8898.dev "https://donabe8898.dev"


E[exout.net/~kirby3ds]
click E "https://exout.net/~kirby3ds"
~~~

## 萌え萌えアクセスカウンター
![](https://count.getloli.com/get/@:mikanixonable)
2023-10-27設置