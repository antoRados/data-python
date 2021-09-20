# import library to parse csv files easily
import csv

# open CupcakeInvoice file
file_open = open('CupcakeInvoices.csv')

# print contents of .csv file
for info in file_open:
    print(info)

file_open.close()

# printing out cupcake type
with open('CupcakeInvoices.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file)

  for line in csv_reader:
    print(line[2])

csv_file.close()

# printing out cupcake prices
with open('CupcakeInvoices.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    sum_float = 0

    for line in csv_reader:
        print(line[4])
        float_num = float(line[4])
        print(float_num)

        sum_float += float_num
    print(sum_float)
csv_file.close()