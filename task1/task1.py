import pandas as pd


data_df = pd.read_csv('data.csv', sep="\t")
price_df = pd.read_csv('prices.csv', sep="\t")
quantity_df = pd.read_csv('quantity.csv', sep="\t")


merged_df = pd.merge(data_df, price_df, on='part_number', how='inner')
# print(merged_df)
merged_df = pd.merge(merged_df, quantity_df, on='part_number', how='inner')
# print(merged_df)
merged_df['price'] = merged_df['price'].str.replace(',', '.').astype(float)


filtered_df = merged_df[(merged_df['price'] > 0)]


result_df = filtered_df[['part_number', 'manufacturer', 'price', 'quantity']]
result_df.to_csv('result.csv', sep="\t", index=False)


report_df = filtered_df.groupby('manufacturer').size().reset_index(name='count')
report_df['report'] = report_df.apply(lambda x: f"{x['manufacturer']} — {x['count']} rows", axis=1)
report_df.to_csv('report.txt', columns=['report'], index=False)