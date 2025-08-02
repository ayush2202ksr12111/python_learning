# python read data from raw

import csv
import io

# we are going to create a raw data with raw_dat_emp of employee

raw_data_emp = """ Name, Age, Location
Abhinav, 27, Noida
Priyanshu, 26, Gurgaon
Paras, 26, Hyderabad
Srishti, 26, Mumbai

"""

#Converting string into file type object

f_t_o = io.StringIO(raw_data_emp)

# Read data using csv reader

csv_reader = csv.reader(f_t_o)

# Now we are going to print the data in for loop

for row_csv_data in csv_reader:
    print(row_csv_data)
