"""
NOTE: Scratchpad blocks are used only for experimentation and testing out code.
The code written here will not be executed as part of the pipeline.
"""
from mage_ai.data_preparation.variable_manager import get_variable


df = get_variable('bike_analytics', 'api_to_local', 'output_0')

#df.member_casual.unique()

#print(df.at[0, 'start_lat'])

df.rideable_type.unique()

#df.start_station_id.unique()

#df.tail(100)