import csv
from ValidationException import ValidationException


def validate_file(input):
    with open(input) as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        next(rows)
        for row in rows:
             try:
                 int(row[1])
             except BaseException:
                 print("invalid mileage: " + row[1])
        
        



def ex1():
    try:
        validate_file("files/input.txt")
    except ValidationException as ve:
        print(ve)

ex1()