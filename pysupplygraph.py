import csv

# Open Csv file
def open_csv_file(csv_name):

    try:
        with open(csv_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                print(line)
    except:
        print("couldn't open file")

# main function
def main():
    print("Welcome to PySupplyGraph")
    open_csv_file('.//data.csv')

main()