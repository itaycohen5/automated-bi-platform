
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

df = pd.read_csv(BASE / 'data' / 'sales_data.csv')

df = df.drop_duplicates()
df = df[df['amount'] > 0]
df['order_date'] = pd.to_datetime(df['order_date'])

df.to_csv(BASE / 'output' / 'clean_sales_data.csv', index=False)

print('Data cleaning completed.')
