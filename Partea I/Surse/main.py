from build_data_set import build_data_set
from build_train_test import build_train_test

filename = "../Data/dataset.csv"
dataset = build_data_set(filename)
trainSetFilename, testSetFilename = build_train_test(filename)