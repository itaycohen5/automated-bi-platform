
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

df = pd.read_csv(BASE / 'output' / 'clean_sales_data.csv')

total_revenue = round(df['amount'].sum(), 2)
avg_order = round(df['amount'].mean(), 2)

summary = pd.DataFrame({
    'metric': ['Total Revenue', 'Average Order Value'],
    'value': [total_revenue, avg_order]
})

summary.to_csv(BASE / 'output' / 'kpi_summary.csv', index=False)

top_products = (
    df.groupby('product')['amount']
    .sum()
    .sort_values(ascending=False)
)

top_products.to_csv(BASE / 'output' / 'top_products.csv')

print('KPI generation completed.')
