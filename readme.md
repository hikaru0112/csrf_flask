# csrf_flask
Cross site Request forgeを体験できるwebサーバーです。

## バージョンや実行環境など
* MacBook Pro (13-inch, M1, 2020) v12.3.1
* Docker v20.10.12
### DockerImage
* mysql:8.0-oracle
* Python:3

Flaskなどについてはpipに依存するため不定
## 実行方法


```bash
docker-compose up --build
```
をターミナルで実行することでwebサーバーとDBサーバーが自動的に立ち上がります。

[localhost:5001](localhost:5001)が接続先URLです。（環境によって適度にポートなどを変更してください。)

攻撃用HTMLは`./attack`に格納しています。

`LiveServer` などを使ってオリジンを切り離して実行してください。

`attack.html` HTMLのフォームを使った攻撃方法です

`attack2.html` JavaScriptを使った攻撃方法です(自分の環境では動作不能)

## DBについて

DBのcliにて
```bash
mysql -u admin -p
```

`パスワード:pass`でログインできます。
