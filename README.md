# README
リンガポルタのBotで穴埋め問題で使えます

## Vの違い

V1はウィンドウが表示されません。

V2はウィンドウが表示されます。

V3とV4は全問正解することができます。

V3は解答の保存に.txtファイルを使っておりV4は.jsonファイルを使っています。

V3は[ansfile](https://github.com/tawakemono/LingaBot/blob/master/ansfile)を

V4は[data.json](https://github.com/tawakemono/LingaBot/blob/master/data.json)を一緒にダウンロードしてください。

お好きなものをお使いください。

## アプリを使う場合

このリポジトリの中にある[bot.exe](https://github.com/tawakemono/LingaBot/blob/master/bot.exe)もしくは、[botv2.exe](https://github.com/tawakemono/LingaBot/blob/master/botv2.exe)をダウンロードしてください

ダウンロードしたら実行することができます。

ファイルを実行するとき警告画面が出ると思うので詳細設定から使えるようにしてください。

**注意**

このexeはWindowsOSでのみ使用可能です。


## スクリプトを使う場合

```
pip install selenium
pip install webdriver-manager
```
この二つをTerminalなどで入力してください。

できないときはこちらを試してみてください。
```
py -m pip install selenium
py -m pip install webdriver-manager
```

始めるときは
```
py LingaBotV1.py
```

または、
```
py LingaBotV2.py
```
で実行できます。

**注意**

別途Pythnの環境構築とGoogle Chromeのインストールがされている必要があります。
