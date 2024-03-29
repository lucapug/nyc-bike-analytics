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
    data['starttime_date'] = data['starttime'].dt.date

    table_name = str(kwargs['year'])+'_bike_data'

    root_path = f'{bucket_name}/{table_name}'    

    table = pa.Table.from_pandas(data)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['starttime_date'],
        filesystem=gcs
    )