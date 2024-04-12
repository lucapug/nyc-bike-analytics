{{
    config(
        materialized='table'
    )
}}

with tripdata_history as (
    select *
    from {{ ref('stg_JC_citibike_trips') }}
)
select rideable_type,
started_at,
ended_at,
start_station_name,
end_station_name,
member_casual
from tripdata_history