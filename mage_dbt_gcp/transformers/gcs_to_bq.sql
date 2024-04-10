-- Docs: https://docs.mage.ai/guides/sql-blocks
-- Creating external table referring to gcs path
CREATE OR REPLACE EXTERNAL TABLE dtc-de-zoomcamp-2024.nyc_bikes.external_{{year}}_tripdata (
ride_id STRING,
rideable_type STRING,
started_at TIMESTAMP,
ended_at TIMESTAMP,
start_station_name STRING,
start_station_id STRING,
end_station_name STRING,
end_station_id STRING,
start_lat FLOAT64,
start_lng FLOAT64,
end_lat FLOAT64,
end_lng FLOAT64,
member_casual STRING
) 
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://nyc_bike_lucapug/{{year}}_bike_data/*.parquet']
);