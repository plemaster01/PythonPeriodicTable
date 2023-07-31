# get the data for our periodic table!
import pandas as pd
# pip install lxml

url = "https://en.wikipedia.org/wiki/Periodic_table"

tables = pd.read_html(url)
print(len(tables))
target_data = tables[1]
pd.set_option('display.max_columns', 35)
pd.set_option('display.max_rows', 35)
print(target_data)

target_data.to_csv('Periodic Data.csv', index=False, encoding='utf-8')
