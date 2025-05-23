###### Duță Ștefan-Horia, 311CA

# Proiect Pclp3


### Descriere:
#### 1. Tipul problemei: 

Setul de date este destinat unei probleme de regresie, care consta in predictia veniturilor unei companii. 

#### 2. Structura setului de date: 
Setul de date va avea 2000 de exemple si este impartit in doua subseturi: 
 - Subsetul de antrenare: are 1400 de exemple 
 - Subsetul de testare: are 600 de exemple 

#### 3. Caracteristici: 

Fiecare instanta are 9 coloane relevante, dintre care “venit” este cea tinta. Pentru acestea am folosit, 3 tipuri diferite de date: numere intregi(numar angajati, an infiintare, numar produse, numar clienti, numar parteneri), numere reale(capital social, venit) si valori categoriale(domeniu de activitate, tara) 

#### 4. Salvarea dataseturilor: 

Subsetul de antrenare va fi salvat in “train.csv”, iar cel de testare in “test.csv”. 

#### 5. Explicarea modului de constructie a setului de date: 

Problema noastra consta in predictia veniturilor unei companii. Setul de date a fost generat aleator, folosind distributia normala si uniforma, cu urmatoarele restrictii: media numarului de angajati este de 100, capitalul social este intre 50000 si 500000 de euro, anul de infiintare este intre 1970 si 2024, numarul de produse este intre 1 si 100, numarul de clienti este intre 50 si 1000, iar numarul de parteneri intre 1 si 20. Tara si domeniul de activitate au fost alese aleator dintr-un set fix de optiuni, acestea fiind Romania, Germania, Franta, Italia, Spania, respectiv, IT, Retail, Agricultura, Educatie, Financiar. Venitul a fost calculat folosind o formula la care contribuie toate caracteristicile unei instante si anume:  

`(numar_angajati * 3000 + capital_social * 0.5 + vechime * 1000 + numar_clienti * 500 + numar_parteneri * 1000) * coef_domeniu * coef_tara. `

Apoi, alegem un numar intre 50 si 100 de valori din fiecare coloana pentru a le sterge. 

#### 6. Antrenarea si evaluarea unui model de baza:
 - MAE: 65922.13
 - RMSE: 98376.38
 - R^2: 0.9205