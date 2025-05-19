import pandas as pd
from sklearn.model_selection import train_test_split

def build_train_test(filename):
    data_set = pd.read_csv(filename)
    train_set, test_set = train_test_split(data_set, train_size=1400, test_size=600, random_state=42)
    trainSetFilename = filename[:-4] + "_train.csv"
    testSetFilename = filename[:-4] + "_test.csv"
    train_set.to_csv(trainSetFilename, index=False)
    test_set.to_csv(testSetFilename, index=False)
    print("Separarea a avut loc si datele sunt salvate in: " + trainSetFilename + " si " + testSetFilename)
    return trainSetFilename, testSetFilename