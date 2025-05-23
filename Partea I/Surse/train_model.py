import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import numpy as np

def train_model(trainSetFilename, testSetFilename):
    train = pd.read_csv(trainSetFilename)
    test = pd.read_csv(testSetFilename)
    categoriale = train.select_dtypes(include='object').columns
    train_encoded = pd.get_dummies(train, columns=categoriale, drop_first=True)
    test_encoded = pd.get_dummies(test, columns=categoriale, drop_first=True)
    test_encoded = test_encoded.reindex(columns=train_encoded.columns, fill_value=0)

    X_train = train_encoded.drop('venit', axis=1)
    y_train = train_encoded['venit']
    X_test = test_encoded.drop('venit', axis=1)
    y_test = test_encoded['venit']

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    test['venit_prezis'] = y_pred
    predictions_filename = "../Data/predictii.csv"
    test.to_csv(predictions_filename)
    print("Predictiile au fost salvate in: " + predictions_filename)
    print('\n')

    mae = mean_absolute_error(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    r2 = r2_score(y_test, y_pred)
    print(f"MAE: {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R^2: {r2:.4f}")

    plt.figure(figsize=(6,6))
    plt.scatter(y_test, y_pred, alpha=0.5, color='dodgerblue')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.xlabel("Venit real")
    plt.ylabel("Venit prezis")
    plt.title("Predictii vs valori reale")
    plt.tight_layout()
    plt.show()

    erori = y_test - y_pred
    plt.figure(figsize=(6,4))
    plt.hist(erori, bins=30, color='darkorange', edgecolor='black')
    plt.title("Distributia erorilor")
    plt.xlabel("Eroare")
    plt.ylabel("Frecventa")
    plt.tight_layout()
    plt.show()
