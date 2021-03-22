import csv

with open('output.csv', 'w+') as output_file:
    with open('input.csv') as input_file:
        for line in input_file.readlines():
            row = line.split(',')

            # NASDAQ data
            if len(row[5]) and float(row[5]) > 1000000000 and float(row[8]) > 1000000:
                output_file.write(row[0])
                output_file.write('\n') 