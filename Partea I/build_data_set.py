import pandas as pd

data_set = pd.read_csv("data_set.csv")
new_data_set = data_set[data_set['company_category_list'].notna()]
first_2000 = new_data_set.head(2000).copy()
first_2000.to_csv("selected_companies.csv", index=False)
print("Am salvat in fisierul selected_companies.csv")
