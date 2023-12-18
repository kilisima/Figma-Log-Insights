DROP TABLE IF EXISTS logs;
CREATE TABLE IF NOT EXISTS logs (
    Log_ID INTEGER,
    Event_Name TEXT,
    Product TEXT,
    Actor_ID INTEGER,
    Actor_Name TEXT,
    Actor_Email TEXT,
    Acted_On_Type TEXT,
    Acted_On_ID_or_Key TEXT,
    Acted_On_Name_User TEXT,
    Acted_On_Email_User TEXT,
    IP_Address TEXT,
    Timestamp DATETIME,
    Metadata TEXT
)