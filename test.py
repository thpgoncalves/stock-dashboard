import pandas as pd 

from data_acquisition import *
from data_processing import *

data = get_stock_data('BERK34.SA')

df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)

print(data)