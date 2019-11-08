import csv
import sys

# Open Csv file
def open_csv_file(csv_name):

    try:
        with open(csv_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                print(line)
    except:
        print("ERROR : couldn't open file")
       
    finally: 
        return

# main function
def main():

    try:
        open_csv_file(sys.argv[1])
    except:
        print("ERROR : incorrect number of argument")

main()