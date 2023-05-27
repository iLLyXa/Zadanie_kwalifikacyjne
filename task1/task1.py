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




# merged_df = pd.merge(data_df, price_df, on=['part_number', 'manufacturer', 'price'])
# merged_df = pd.merge(merged_df, quantity_df, on=['part_number', 'manufacturer'])

# filtered_df = merged_df[(merged_df['quantity'] > 0) & (merged_df['price'] > 0)]

# filtered_df.to_csv('processed_data.csv', index=False)

# report_df = filtered_df.groupby('manufacturer').size().reset_index(name='count')
# report_df['report'] = report_df.apply(lambda x: f"{x['manufacturer']} — {x['count']} rows", axis=1)

# report_df['report'].to_csv('manufacturer_report.txt', index=False)


# sample_supplier_df = pd.read_csv('sample_supplier.csv')

# comparison_df = pd.merge(filtered_df, sample_supplier_df, on=['part_number', 'manufacturer'], how='inner')
# comparison_df['better_price'] = np.where(comparison_df['price_x'] < comparison_df['price_y'], 'processed_data.csv', 'sample_supplier.csv')

# comparison_df.to_csv('price_comparison.csv', index=False)


# print("Обработанный CSV файл прайс-листа:")
# print(filtered_df.head())

# print("\nТекстовый файл с итогами анализа производителей:")
# print(report_df['report'].to_string(index=False))

# print("\nCSV файл сравнения из второго задания:")
# print(comparison_df.head())