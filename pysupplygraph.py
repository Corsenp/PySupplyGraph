import csv
import sys
import matplotlib.pyplot as plt
import numpy as np


# Create the graph
def create_graph(price, q_demand, q_supplied):
    try:
        plt.plot(price, q_demand, price, q_supplied)
        plt.ylabel('Price')
        plt.show()
    except:
        print('ERROR : can\'t create graph')

# Open Csv file
def open_csv_file(csv_name):

    try:
        price = []
        q_demand = []
        q_supplied = []
        with open(csv_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                line[0] = line[0].strip()
                line[1] = line[1].strip()
                line[2] = line[2].strip()
                if line[0].strip().isnumeric() == True and line[1].isnumeric() == True and line[2].isnumeric() == True:
                    price.append(int(line[0]))
                    q_demand.append(int(line[1]))
                    q_supplied.append(int(line[2]))
        create_graph(price, q_demand, q_supplied)

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