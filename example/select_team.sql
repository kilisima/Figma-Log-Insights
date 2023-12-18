select 
    strftime('%Y-%m', Timestamp) as year_month,
    json_extract(Metadata, "$.team_name") as team_name ,
    count(0) as count
from
    logs
where
    json_extract(Metadata, "$.team_name") IS NOT NULL
group by team_name, year_month;