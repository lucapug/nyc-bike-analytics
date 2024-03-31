-- Docs: https://docs.mage.ai/guides/sql-blocks
-- Creating external table referring to gcs path
CREATE OR REPLACE EXTERNAL TABLE dtc-de-zoomcamp-2024.nyc_bikes.external_{{year}}_tripdata (
tripduration INT64,
starttime TIMESTAMP,
stoptime TIMESTAMP,
start_station_id INT64,
start_station_name STRING,
start_station_latitude FLOAT64,
start_station_longitude FLOAT64,
end_station_id INT64,
end_station_name STRING,
end_station_latitude FLOAT64,
end_station_longitude FLOAT64,
bike_id INT64,
usertype STRING,
birth_year INT64,
gender INT64
) 
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://nyc_bike_lucapug/{{year}}_bike_data/*.parquet']
);