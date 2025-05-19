###### Duță Ștefan-Horia, 311CA

# Proiect Pclp3


### Descriere:

Proiectul consta intr-o problema de clasificare. Am folosit o baza de date de pe platforma Kaggle, pe care am extras-o de la urmatorul link: https://www.kaggle.com/datasets/chhinna/crunchbase-data/data. De aici, pentru a face rost de exemplele pentru antrenare si de cele pentru testare, am extras 2000 de companii care aveau completata coloana company_category_list.

In continuare, adaugam coloana is_tech care reprezinta problema de clasificare pe care trebuie sa o rezolvam noi. Aceasta coloana is_tech va avea valoarea 1 daca respectiva companie activeaza in domenii precum: software, cloud, data, cybersecurity, electronics, e-commerce, online media etc. Altfel, va avea valoarea 0.

Acum, trebuie sa impartim cele 2000 de exemple in cele de antrenare si cele de testare(1400 si 600) si le salvam in fisierele corespunzatoare.