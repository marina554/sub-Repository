Weather Data Fetch & Excel Export (API Practice)
Overview

This program is a sample Python script that uses the OpenWeatherMap API to fetch weather information for multiple cities and export the results to an Excel (.xlsx) file.

The retrieved data is sorted by temperature, and cells with temperatures of 25°C or higher are highlighted in red.

The purpose of this project is to practice:

API communication

Data processing

Excel file generation and formatting

Technologies & Libraries

Python 3.x

requests (API communication)

pandas (data processing)

openpyxl (Excel file operations)

OpenWeatherMap API

Setup
1. Install Required Libraries

Run the following command to install the necessary libraries:

pip install requests pandas openpyxl

2. Get an OpenWeatherMap API Key

Register on the OpenWeatherMap official website

Generate an API key

Insert your API key into the following part of the code:

api_key = "YOUR_API_KEY_HERE"

Program Details
Target Cities
cities = ["Tokyo", "Osaka", "Sapporo", "Nagoya", "Fukuoka"]

Retrieved Weather Data

City name

Weather description (Japanese)

Temperature (°C)

Feels-like temperature (°C)

Humidity (%)

Wind speed (m/s)

Atmospheric pressure (hPa)

Processing Flow

Send requests to the OpenWeatherMap API

Retrieve weather data in JSON format

Convert the data into a pandas DataFrame

Sort the data by temperature (descending order)

Export the data to an Excel file

Highlight cells with temperatures ≥ 25°C in red

Output File

File name: weather_multi.xlsx

Contents:

Weather data for each city

Temperature cells highlighted in red when ≥ 25°C

Example Output
Cells with temperatures of 25°C or higher have been highlighted in red:
/content/weather_multi.xlsx

Learning Points

How to use a REST API

Handling JSON data in Python

Data processing with pandas

Automatic Excel file generation and formatting

Basic API error handling

Notes

Do not share your API key publicly

The free OpenWeatherMap plan has API call limits

An internet connection is required

Possible Enhancements

Allow users to input cities dynamically

Support CSV output

Apply conditional formatting to other metrics (humidity, wind speed)

Schedule automatic execution (cron / task scheduler)

-----------------Jaoanese------------------------------------------

天気情報取得＆Excel出力（API練習）
概要

このプログラムは、OpenWeatherMap API を利用して複数都市の天気情報を取得し、
結果を Excelファイル（.xlsx） にまとめて出力するサンプルコードです。

取得したデータは気温順に並べ替えられ、
気温が25℃以上のセルは赤くハイライト表示されます。

API通信・データ加工・Excel操作をまとめて練習することを目的としています。

使用技術・ライブラリ

Python 3.x

requests（API通信）

pandas（データ整形）

openpyxl（Excel操作）

OpenWeatherMap API

事前準備
1. 必要なライブラリのインストール

以下のコマンドで必要なライブラリをインストールしてください。
pip install requests pandas openpyxl
2. OpenWeatherMap APIキーの取得

OpenWeatherMap公式サイトに登録

APIキーを発行

コード内の以下の部分に自分のAPIキーを入力
api_key = "ここにあなたのAPIキー"

プログラムの内容
取得する都市
cities = ["Tokyo", "Osaka", "Sapporo", "Nagoya", "Fukuoka"]
取得する天気情報

都市名

天気（日本語）

気温（℃）

体感温度（℃）

湿度（%）

風速（m/s）

気圧（hPa）

処理の流れ

OpenWeatherMap APIにリクエストを送信

JSONデータを取得

pandasのDataFrameに変換

気温の高い順に並び替え

Excelファイルに出力

気温が25℃以上のセルを赤く塗る

出力ファイル

ファイル名：weather_multi.xlsx

内容：

各都市の天気データ一覧

気温が25℃以上のセルは赤色表示

実行結果例
気温が25℃以上のセルを赤く塗りました: /content/weather_multi.xlsx

学習ポイント

REST APIの使い方

JSONデータの扱い方

pandasによるデータ整理

Excelファイルの自動生成・装飾

APIエラー時の簡単なエラーハンドリング

注意点

APIキーは公開しないようにしてください

無料プランではAPIの呼び出し回数に制限があります

インターネット接続が必要です

発展アイデア

都市をユーザー入力にする

CSV出力にも対応

気温以外（湿度・風速）で条件付き書式

定期実行（cron / タスクスケジューラ）
