#!/usr/bin/env python
# coding: utf-8
#
# [FILE] util.py
#
# [DESCRIPTION]
#  RESメソッドで利用するユーティリティ関数を定義する。
#
import json
import base64, os, sys
from dotenv import load_dotenv

# .envファイルの内容を読み込見込む
load_dotenv()

# ローカルフォルダー
local_folder = os.environ.get("LOCAL_FOLDER")
if local_folder == None:
    print("環境変数LOCAL_FOLDERが設定されていません")
    sys.exit()

#
# [FUNCTION] storeBinaryFile()
#
# [DESCRIPTION]
#  Base64文字列からバイナリファイルを保存する。
#
# [INPUTS]
#  fileName - 保存するファイル名（拡張子なし）
#  b64Text  - Base64文字列
#    data:image/jpeg;base64,/9j/4AAQSkZJR...
#    data:application/pdf;base64,JVBERi0xLjQNCiXi4...
#
# [OUTPUTS] 
#  成功 - ファイル名を返却
#  失敗 - None
#
# [NOTES]
#
def storeBinaryFile(fileName, b64Text):
    # 保存する内容を取得
    binString = b64Text.split(',')
    binContent = base64.b64decode(binString[1])

    # ファイル拡張子を取得
    binString = binString[0].split('/')
    ext = binString[1].split(';')

    # 保存するファイル名を準備する
    binFile = local_folder + "/" + fileName + "." + ext[0]

    # ファイルを保存
    try:
        with open(binFile, 'wb') as file:
            file.write(binContent)
    except Exception as e:
        print(e)
        binFile = None
    
    return binFile
#
# HISTORY
# [1] 2024-12-27 - Initial version
#

#
# [FUNCTION] storeJsonFile()
#
# [DESCRIPTION]
#  JSONデータをファイルに保存する。
#
# [INPUTS]
#  fileName - 保存するファイル名（拡張子なし）
#  jsonData - 保存するJSONデータ
#
# [OUTPUTS] 
#  成功 - ファイル名を返却
#  失敗 - None
#
# [NOTES]
#
def storeJsonFile(fileName, jsonData):

    # 保存するファイル名を準備する
    jsonFile = local_folder + "/" + fileName + ".json"
   
    # JSONファイルを保存
    try:
        with open(jsonFile, 'w', encoding='utf-8') as file:
            json.dump(jsonData, file, indent=4)
    except Exception as e:
        print(e)
        jsonFile = None
    
    return jsonFile
#
# HISTORY
# [1] 2024-12-27 - Initial version
#