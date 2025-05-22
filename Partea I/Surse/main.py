from build_data_set import build_data_set
from build_train_test import build_train_test
from eda import eda

filename = "../Data/dataset.csv"
dataset = build_data_set(filename)
filled_dataset_filename = eda(filename)
trainSetFilename, testSetFilename = build_train_test(filled_dataset_filename)