{{ config(
    materialized='table'
)}}

with tripdata_history as (
    select *
    from {{ ref('stg_JC_citibike_trips') }}
)
select rideable_type,
started_at,
ended_at,
TIMESTAMP_DIFF(ended_at, started_at, MINUTE) as duration_in_mins,
start_station_name,
start_lat,
start_lng,
end_station_name,
member_casual
from tripdata_history