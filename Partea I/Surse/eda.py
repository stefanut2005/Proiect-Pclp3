import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def eda(filename):
    dataset = pd.read_csv(filename)
    valori_lipsa = dataset.isnull().sum()
    print("Numarul de valori lipsa de pe fiecare coloana este:")
    print(valori_lipsa)
    print('\n')

    for column in dataset.columns:
        if dataset[column].dtype == 'float64':
            medie = dataset[column].mean()
            dataset[column].fillna(medie, inplace=True)
        else:
            frecv = dataset[column].mode()[0]
            dataset[column].fillna(frecv, inplace=True)

    filled_dataset_filename = '../Data/filled_dataset.csv'
    dataset.to_csv(filled_dataset_filename, index=False)

    print("Statistici descriptive:")
    print(dataset.describe())
    print('\n')

    numerice = dataset.select_dtypes(include=['float64']).columns
    categoriale = dataset.select_dtypes(include=['object']).columns

    for column in numerice:
        plt.figure(figsize=(6,4))
        sns.histplot(dataset[column], kde=True)
        plt.title(f"Histograma pentru {column}")
        plt.xlabel(column)
        plt.ylabel('Frecventa')
        plt.tight_layout()
        plt.show()

    for column in categoriale:
        plt.figure(figsize=(8,4))
        sns.countplot(data=dataset, x=column, order=dataset[column].value_counts().index)
        plt.title(f'Countplot pentru {column}')
        plt.xlabel(column)
        plt.ylabel('Frecventa')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    numerice = dataset.select_dtypes(include=['float64'])
    corelatii = numerice.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corelatii, annot=True, fmt=".2f", cmap="coolwarm", square=True)
    plt.title("Matricea de corelatii intre variabilele numerice")
    plt.show()
    
    numerice = dataset.select_dtypes(include=['float64']).columns.drop('venit')
    for column in numerice:
        plt.figure(figsize=(6, 4))
        sns.scatterplot(x=dataset[column], y=dataset['venit'], hue=dataset['venit'], palette='magma', legend=True)
        plt.title(f'{column} vs Venit')
        plt.xlabel(column)
        plt.ylabel('Venit')
        plt.tight_layout()
        plt.show

    for column in categoriale:
        plt.figure(figsize=(8, 5))
        sns.violinplot(x=dataset[column], y=dataset['venit'], palette='Set3')
        plt.title(f'Venit in functie de {column}')
        plt.xlabel(column)
        plt.ylabel('Venit')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    return filled_dataset_filename