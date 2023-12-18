import csv
import sqlite3
from datetime import datetime
import json


# SQLiteデータベースファイル（なければ新規作成される）
db_file = 'example.sqlite'

# データ挿入用のSQL
insert_sql = '''
INSERT INTO logs (
    Log_ID,
    Event_Name,
    Product,
    Actor_ID,
    Actor_Name,
    Actor_Email,
    Acted_On_Type,
    Acted_On_ID_or_Key,
    Acted_On_Name_User,
    Acted_On_Email_User,
    IP_Address,
    Timestamp,
    Metadata
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''

# データベースに接続
conn = sqlite3.connect(db_file)
cur = conn.cursor()

# CSVファイルを開く
with open('example.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)

    # ヘッダー行を読み飛ばす場合（必要に応じて）
    next(csvreader)

    # 行ごとに処理
    for row in csvreader:
        row[11] = datetime.strptime(row[11], '%Y-%m-%d %H:%M:%S %Z')
        row[12] = row[12].replace("=>", ":").replace("nil", "null")
        # print(row[12])
        # jsondata = json.loads(row[12])
        # print(jsondata)
        cur.execute(insert_sql, row)
        # print(row)  # ここで各行を処理


# 変更をコミット
conn.commit()

# データベースを閉じる
conn.close()

print("データベースにテーブルとサンプルデータが作成されました。")