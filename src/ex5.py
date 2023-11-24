import csv
from pprint import pprint

def build_car_list():
    carids = []
    with open('files/car-ids.txt','r') as csv_file:
         rows = csv.reader(csv_file, delimiter=',')
        
         
        #  with open('files/input.txt','r') as csv_file:
        #     input= csv.reader(csv_file, delimiter=',')
        #     next(input)
         for row in rows:
             if(row[0] != '4'):
                carids.append(row)
    input = []
    with open('files/input.txt','r') as csv_file:
         rows = csv.reader(csv_file, delimiter=',')
         next(rows)
         for row in rows:
             if(row[0] != '4'):
                input.append(row)
    carlist = []
    for i in range(len(input)):
        carlist.append({'id': int(carids[i][0]),'miles': int(input[i][1]),'model':carids[i][1]})
    
    return carlist

         
        

             



def ex5():
    car_list = build_car_list()
    pprint(car_list)

ex5()
