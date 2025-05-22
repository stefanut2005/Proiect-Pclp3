import pandas as pd
import numpy as np

def build_data_set(filename):
    companies = 2000
    np.random.seed(42)

    numar_angajati = np.random.normal(loc=100, scale=20, size=companies).astype(int)
    capital_social = np.random.uniform(50000, 500000, size=companies)
    an_infiintare = np.random.randint(1970, 2024, size=companies)
    numar_produse = np.random.uniform(1, 100, size=companies).astype(int)
    numar_clienti = np.random.randint(50, 1000, size=companies)
    numar_parteneri = np.random.randint(1, 20, size=companies)

    domenii = ['IT', 'Retail', 'Agricultura', 'Educatie', 'Financiar']
    tari = ['Romania', 'Germania', 'Franta', 'Italia', 'Spania']

    domeniu = np.random.choice(domenii, size=companies)
    tara = np.random.choice(tari, size=companies)
    vechime = 2025 - an_infiintare

    coef_domeniu = {
        'IT': 1.5,
        'Retail': 1.2,
        'Agricultura': 0.8,
        'Educatie': 0.9,
        'Financiar': 1.3
    }

    coef_tara = {
        'Romania': 1.0,
        'Germania': 1.4,
        'Franta': 1.3,
        'Italia': 1.2,
        'Spania': 1.1
    }

    venit = []
    for i in range(companies):
        x = (numar_angajati[i] * 3000 + capital_social[i] * 0.5 + vechime[i] * 1000 + numar_clienti[i] * 500 + numar_parteneri[i] * 1000) * coef_domeniu[domeniu[i]] * coef_tara[tara[i]]
        venit.append(x)

    venit = np.array(venit)

    dataset = pd.DataFrame({
        'numar angajati': numar_angajati,
        'capital social': capital_social,
        'an infiintare': an_infiintare,
        'numar produse': numar_produse,
        'domeniu de activitate': domeniu,
        'tara': tara,
        'clienti': numar_clienti,
        'parteneri': numar_parteneri,
        'venit': venit
    })

    for column in dataset.columns:
        if column != 'venit':
            nr = np.random.randint(50, 101)
            index = np.random.choice(dataset.index, size=nr, replace=False)
            dataset.loc[index, column] = np.nan

    dataset.to_csv(filename, index=False)
    print("Setul de date a fost salvat in: " + filename)
    print('\n')