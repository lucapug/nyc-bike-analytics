import io
import pandas as pd
import requests

import datetime

from zipfile import ZipFile
from urllib.request import urlopen

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    prefix = 'https://s3.amazonaws.com/tripdata/JC-'
    prefix_file = 'JC-'

    year = kwargs['year']
    months=[]
    for i in range(12):
        month = '0'+str(i+1)
        month = month[-2:]
        months.append(month) 

    suffix = '-citibike-tripdata.csv.zip'
    suffix_csv = '-citibike-tripdata.csv'

    date_schema_change = datetime.date(2021,1,31)


    df_list = []
    for month in months:

        before = year < 2021 or (year==2021 and int(month)==1)

        if before:
            bike_dtypes = {
                'tripduration': pd.Int64Dtype(),
                'start station id': pd.Int64Dtype(),
                'start station name': str,
                'start station latitude': float,
                'start station longitude': float,
                'end station id': pd.Int64Dtype(),
                'end station name': str,
                'end station latitude': float,
                'end station longitude': float,
                'bikeid': pd.Int64Dtype(),
                'usertype': str,
                'birth year': pd.Int64Dtype(),
                'gender': pd.Int64Dtype()
            }

            # native date parsing 
            parse_dates = ['starttime','stoptime']
        else:
            bike_dtypes = {
                'ride_id': str,
                'rideable_type': str,
                'start_station_name': str,
                'start_station_id': str,
                'end_station_name': str,
                'end_station_id': str,
                'start_lat': float,
                'start_lng': float,
                'end_lat': float,
                'end_lng': float,
                'member_casual': str
            }
            parse_dates = ['started_at','ended_at']


        url = prefix+str(year)+month+suffix

        r = urlopen(url).read()
        df_zip = ZipFile(io.BytesIO(r))

        df = pd.read_csv(df_zip.open(prefix_file+str(year)+month+suffix_csv), sep=',' , dtype=bike_dtypes, parse_dates=parse_dates)
        
        if before:
            df.drop(columns=['tripduration','birth year','gender','bikeid'], inplace=True)
            df.columns = df.columns.str.replace(' ', '_').str.lower()
            df['start_station_id'] = df['start_station_id'].astype(str)
            df['end_station_id'] = df['end_station_id'].astype(str)
            df.rename(columns={"starttime":"started_at","stoptime":"ended_at",
            "usertype":"member_casual","start_station_latitude":"start_lat",
            "end_station_latitude":"end_lat","start_station_longitude":"start_lng",
            "end_station_longitude":"end_lng"}, inplace=True)
            df.replace(to_replace='Customer', value='casual', inplace=True)
            df.replace(to_replace='Subscriber', value='member', inplace=True)
            df.insert(0,'rideable_type', '')
            df.insert(0,'ride_id', '')
        else:
            df.replace(to_replace='docked_bike', value='classic_bike', inplace=True)
        df_list.append(df)
    
    return pd.concat(df_list, ignore_index=True)

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
