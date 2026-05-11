
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

df = pd.read_csv(BASE / 'output' / 'clean_sales_data.csv')

threshold = df['amount'].mean() + (2 * df['amount'].std())

anomalies = df[df['amount'] > threshold]

anomalies.to_csv(BASE / 'output' / 'anomalies.csv', index=False)

print(f'Anomalies detected: {len(anomalies)}')
