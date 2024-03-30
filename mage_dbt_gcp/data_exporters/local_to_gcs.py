import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/.dbt/dtc-de-zoomcamp-2024-4a477d7bc858.json'

bucket_name = 'nyc_bike_lucapug'
project_id = 'dtc-de-zoomcamp-2024'

@data_exporter
def export_data(data, *args, **kwargs):
    #data['month'] = data['starttime'].dt.month

    #schema = pa.Schema.from_pandas(data)
    '''
    table_schema_bike = pa.schema(
        [
            ('tripduration', pa.int64()),
            ('starttime', pa.timestamp('us')),
            ('stoptime', pa.timestamp('us')),
            ('start_station_id', pa.int64()),
            ('start_station_name', pa.string()),
            ('start_station_latitude', pa.float64()),
            ('start_station_longitude', pa.float64()),
            ('end_station_id', pa.int64()),
            ('end_station_name', pa.string()),
            ('end_station_latitude', pa.float64()),
            ('end_station_longitude', pa.float64()),
            ('bike_id', pa.int64()),
            ('usertype', pa.string()),
            ('birth_year', pa.int64()),
            ('gender', pa.int64())
            ]
        )
    '''

    table_name = str(kwargs['year'])+'_bike_data'

    root_path = f'{bucket_name}/{table_name}'    

    table = pa.Table.from_pandas(data)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
    #    partition_cols=['month'],
        filesystem=gcs,
        coerce_timestamps='us'
    )