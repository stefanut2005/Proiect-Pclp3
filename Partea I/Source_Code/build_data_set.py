import pandas as pd

def build_data_set(filename):
    data_set = pd.read_csv(filename)
    new_data_set = data_set[data_set['company_category_list'].notna()]
    first_2000 = new_data_set.head(2000).copy()
    new_filename = filename[:-4] + "_modified.csv"
    first_2000.to_csv(new_filename, index=False)
    print("Am salvat in fisierul " + new_filename)
    return new_filename
