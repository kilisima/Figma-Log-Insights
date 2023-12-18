DROP VIEW if EXISTS DATE_COUNT_SUMMARY;
DROP VIEW if EXISTS DATE_EVENT_SUMMARY;
DROP VIEW if EXISTS MONTH_EVENT_SUMMARY;
DROP VIEW if EXISTS MONTH_TEAM_EVENT_SUMMARY;
DROP VIEW if EXISTS EMAIL_EVENT_SUMMARY;
DROP VIEW if EXISTS FILENAME_EVENT_SUMMARY;


CREATE VIEW IF NOT EXISTS DATE_COUNT_SUMMARY as  select strftime('%Y-%m-%d' , Timestamp) as date , count(0) as count from logs group by strftime('%Y-%m-%d' , Timestamp) ;
CREATE VIEW IF NOT EXISTS DATE_EVENT_SUMMARY as  select strftime('%Y-%m-%d' , Timestamp) as date , Event_Name,  count(0) as count  from logs group by strftime('%Y-%m-%d' , Timestamp), Event_Name ;
CREATE VIEW IF NOT EXISTS MONTH_EVENT_SUMMARY as  select strftime('%Y-%m' , Timestamp) as date , Event_Name,  count(0) as count from logs group by strftime('%Y-%m' , Timestamp), Event_Name ;
CREATE VIEW IF NOT EXISTS MONTH_TEAM_EVENT_SUMMARY as select 
        strftime('%Y-%m', Timestamp) as year_month,
        Event_Name as event,
        json_extract(Metadata, "$.team_name") as team_name ,
        count(0) as count
    from
        logs
    where
        json_extract(Metadata, "$.team_name") IS NOT NULL
group by team_name, year_month;

CREATE VIEW IF NOT EXISTS EMAIL_EVENT_SUMMARY AS
    SELECT 
        Actor_Email as email,
        Event_name as event,
        count(0) as count
    FROM
        logs
    group by email, event;

CREATE VIEW IF NOT EXISTS FILENAME_EVENT_SUMMARY AS
    SELECT 
        json_extract(Metadata, "$.name") as name,
        Event_name as event,
        count(0) as count
    FROM
        logs
    WHERE name IS NOT NULL
    group by email, event;