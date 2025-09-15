# 開発環境

## javaコンパイル方法

### 前提条件
コンテナに以下をダウンロードする。
- gradle-9.1.0  
※Dockerビルド時にダウンロードされる。

### コンパイル
1. `$ sh deploy.sh ` を実行する。  
※ tomcatサーバーのstop+startコマンドも含まれているので任意で外してもよい。pushしないこと。


## デバッグ方法

### 前提条件
以下の拡張機能をインストールする。
- Community Server Connectors 
- Runtime Server Protocol UI
- Extension Pack for Java

### tomcatサーバーにアタッチ
1. `$ sh start_tomcat.sh ` を実行してtomcatサーバーを起動する。
2. vscodeのエクスプローラを開きSERVERから Community Server Connector を右クリックして Create new server... を選択する。
3. bin、conf、webapps…があるtomcatフォルダを選択する。
4. 任意のサーバー名を入力して Finish を選択する。
5. /app/tomcat/webapps/ROOT/WEB-INF フォルダを選択して Debag on Server 選択する。
6. ブレークポイントを置くことでデバッグ出来る。  
※ デバッガを停止する場合には 起動中のデバッガを右クリックしてRemove Deployment を選択する。
