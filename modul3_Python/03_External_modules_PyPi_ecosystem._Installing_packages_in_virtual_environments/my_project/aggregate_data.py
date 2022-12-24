import pandas as pd

all_data = [1.7, 0.5, None]
data_sum = pd.Series(all_data).sum(skipna=None) # исправил False на None поставил pandas < 1.4
print(data_sum)
