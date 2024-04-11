{{ config(
    materialized='table',
    partition_by={
      "field": "started_at",
      "data_type": "timestamp",
      "granularity": "day"
    },
	cluster_by="start_station_name"
)}}

WITH tripdata AS(
		SELECT * FROM  {{ source('external_bigquery_source', 'external_2019_tripdata') }}
		UNION ALL
		SELECT * FROM {{ source('external_bigquery_source', 'external_2020_tripdata') }}
		UNION ALL
		SELECT * FROM {{ source('external_bigquery_source', 'external_2021_tripdata') }}
		UNION ALL
		SELECT * FROM {{ source('external_bigquery_source', 'external_2022_tripdata') }}
		UNION ALL
		SELECT * FROM {{ source('external_bigquery_source', 'external_2023_tripdata') }}
	)
SELECT * FROM tripdata 
WHERE start_station_id is NOT NULL AND end_station_id is NOT NULL
--ORDER BY started_at

--LIMIT 1000