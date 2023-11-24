
import csv


def find_total_visits():
    total = 0
    with open('files/week-1.csv') as csv_file:
         rows = csv.reader(csv_file, delimiter=',')
         next(rows)
         for row in rows:
             total = total + sum(int(x) for x in row[1:])
             
    with open('files/week-2.csv') as csv_file:
         rows = csv.reader(csv_file, delimiter=',')
         next(rows)
         for row in rows:
             total = total + sum(int(x) for x in row[1:])
    with open('files/week-3.csv') as csv_file:
         rows = csv.reader(csv_file, delimiter=',')
         next(rows)
         for row in rows:
             total = total + sum(int(x) for x in row[1:])
    return total
            

def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")

ex2()