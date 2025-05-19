from build_data_set import build_data_set
from build_is_tech import build_is_tech

filename = "../Data/data_set.csv"
new_filename = build_data_set(filename)
build_is_tech(new_filename)