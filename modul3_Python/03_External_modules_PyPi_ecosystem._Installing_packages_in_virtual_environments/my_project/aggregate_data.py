import pandas as pd

all_data = [1.7, 0.5, None]
data_sum = pd.Series(all_data).sum(skipna=True) # исправил None на False
print(data_sum)
