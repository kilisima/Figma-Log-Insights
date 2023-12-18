import sqlite3
import traceback
import csv
from datetime import datetime
import glob
from io import StringIO



def _fetch_all(database_file:str , table_name:str):
    # データベースに接続
    conn = sqlite3.connect(database_file)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # クエリの実行
    cur.execute(f"SELECT * FROM {table_name};")

    # すべての行を取得
    # data = cur.fetchall()
    data = [dict(row) for row in cur.fetchall()]
    # # 各行を処理
    # for row in rows:
    #     print(row)

    # 接続を閉じる
    conn.close()
    return data



def create_database(filename:str) -> bool:
    try:
        conn = sqlite3.connect(f"database/{filename}.sqlite")
        cur = conn.cursor()

        for file in glob.glob("sql/*"):
            print(f"file:{file}")
            with open(file) as initial:
                sql = initial.read()
                # cur.execute(sql)
                # cur.executemany(sql)
                cur.executescript(sql)

        cur.close()
        conn.close()
        return True 
    except Exception as e:
        stack_trace = traceback.format_exc()
        print("エラーが発生しました:\n", stack_trace)
        return False



def import_data(import_data, database_file:str) -> bool:
    try:
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
        conn = sqlite3.connect(database_file)
        cur = conn.cursor()

        # CSVファイルを開く
        # with open(import_data_file, newline='') as csvfile:
        csvio = StringIO(import_data.getvalue().decode("utf-8"))

        
        csvreader = csv.reader(csvio)

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
        return True
    except Exception as e:
        stack_trace = traceback.format_exc()
        print("エラーが発生しました:\n", stack_trace)
        return False



def get_tean_event_sumamry(database_file:str):
    table_name = "MONTH_TEAM_EVENT_SUMMARY"
    return _fetch_all(database_file=database_file, table_name=table_name)



def get_email_event_summary(database_file:str):
    table_name = "EMAIL_EVENT_SUMMARY"
    return _fetch_all(database_file=database_file, table_name=table_name)



