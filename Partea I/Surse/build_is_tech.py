import pandas as pd

def is_tech(company_category_list):
    tech_keywords = [
    'software', 'internet', 'electronics', 'mobile',
    'computer', 'cloud', 'machine learning', 'data', 'cybersecurity',
    'saas', 'digital', 'e-commerce', 'web', 'online', 'apps','iot'
    ]

    if isinstance(company_category_list, str):
        company_category_list = company_category_list.lower()
        return int(any(keyword in company_category_list for keyword in tech_keywords))
    return 0

def build_is_tech(filename):
    data_set = pd.read_csv(filename)
    data_set['is_tech'] = data_set['company_category_list'].apply(is_tech)
    data_set.to_csv(filename, index=False)
    print("Coloana 'is_tech' a fost adaugata.")
