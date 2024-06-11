#	YNCNEO_UDPTransfer | ゆかコネNEO UDP転送プラグイン  

「ゆかりねっとコネクターNEO」（以下、ゆかコネNEO）のPython連携プラグイン用モジュールです。  

Plugin for Yukarinette Connector NEO(YNC NEO) that allows to transfer SR result to any UDP server  

##	機能  
-	ゆかコネNEOが音声認識した結果のテキストを、そのまま任意の宛先にUDP送信します。
-	現状、「母国語」のテキストのみ送信します。
-	サーバーからの応答は特に期待しません。返信があっても何もしません。

##	前提
-	ゆかりねっとコネクターNEO（Version 2.1.97 動作確認済み）
-	ゆかコネNEO「Python 連携」プラグイン（v1.0b 動作確認済み）
-	Python3（[ゆかコネNEOが定める前提](https://nmori.github.io/yncneo-Docs/plugin/plugin_pythonunit/#_4)に従うこと）

##	使い方
1.	本リポジトリから最新の `UDPTransfer.py` をダウンロードします。
2.	必要に応じて、 `UDPTransfer.py` の中身を編集し、宛先IPアドレスやポート番号を変更します。
3.	ゆかコネNEOの「Python 連携」プラグイン（以下、Python連携）を有効化します。  
（有効化にあたっては[ゆかコネNEOのマニュアル](https://nmori.github.io/yncneo-Docs/plugin/plugin_pythonunit/)に従って行うこと）  
4.	Python連携の設定画面を開き、[フォルダを開く]を押下します。
5.	Pythonモジュール格納用フォルダ（ `C:\Users\ユーザー名\AppData\Roaming\YukarinetteConnector\PythonLib` ）が表示されるので、その中に `UDPTransfer.py` を格納します。
6.	Python連携の設定画面に戻り、[モジュール再読み込み]を押下します。
7.	連携先（UDP送信先）を用意し、通常通り使用します。

##	使用例  
同じく私が作成した、PCゲーム用音声コマンディングツール「[SR2Control](https://github.com/Domtaro/)」で使用しています。
（というか、そのために作成しました。）

## ライセンス／利用規約

本プロジェクトは、GNU Lesser General Public License Version 3 (LGPL-3.0 またはそれ以上)に基づき、自由に利用いただけます。
