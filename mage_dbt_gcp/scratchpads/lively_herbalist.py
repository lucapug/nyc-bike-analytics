"""
NOTE: Scratchpad blocks are used only for experimentation and testing out code.
The code written here will not be executed as part of the pipeline.
"""
from mage_ai.data_preparation.variable_manager import get_variable


df = get_variable('bike_analytics', 'api_to_local', 'output_0')
months=[]
for i in range(12):
    month = '0'+str(i+1)
    month = month[-2:]
    print(month)
    months.append(month)
print(months)