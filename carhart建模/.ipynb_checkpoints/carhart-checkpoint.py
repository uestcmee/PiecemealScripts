import pandas as pd
DATA_FILE='./Data_Input/data.CSV'
df=pd.read_csv(DATA_FILE,encoding='gbk')

print(df.head())
