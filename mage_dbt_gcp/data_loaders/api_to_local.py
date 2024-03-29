import io
import pandas as pd
import requests
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

    year = kwargs['year']
    months=[]
    for i in range(12):
        month = '0'+str(i+1)
        month = month[-2:]
        months.append(month) 

    suffix = '-citibike-tripdata.csv.zip'

    
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
    

    df_list = []
    for month in months:
        url = prefix+str(year)+month+suffix
        df = pd.read_csv(url, sep=',', compression='zip', dtype=bike_dtypes, parse_dates=parse_dates)
        df_list.append(df)
    
    return pd.concat(df_list, ignore_index=True)

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
