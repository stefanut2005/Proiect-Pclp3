from build_data_set import build_data_set
from build_is_tech import build_is_tech
from build_train_test import build_train_test

filename = "../Data/data_set.csv"
new_filename = build_data_set(filename)
build_is_tech(new_filename)
trainSetFilename, testSetFilename = build_train_test(new_filename)