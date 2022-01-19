from pathlib import Path
import csv
Path.cwd()
path = r"/home/hanoch/Desktop/python/jamesbond.csv"
f = open(path)
for i in csv.reader(f):
    print( i)
def read_bond(file_path):
    with open(file_path) as emp:
        next(emp)
        count=0
        budge=0
        for i in csv.reader(emp):
            count+=1
            budge+=float(i[5])
        return (count, round(budge/count, 2))
read_bond(path)
from collections import Counter
z = ['red', 'blue', 'yellow', 'blue', 'red', 'blue']
x= Counter(z)
x.most_common()[0][0]
def count_actors(file_path):
    with open(file_path) as emp:
        next(emp)
        lst=[]
        for i in csv.reader(emp):
            lst.append(i[2])
        y=Counter(lst)
        
        return y.most_common()[0][0]
count_actors(path)
def actor_period(file_path, start, stop):
    with open(file_path) as emp:
        next(emp)
        lst=[]
        for i in csv.reader(emp):
            if int(i[1])<start or int(i[1])>stop:
                pass
            else:
                lst.append(i[2])
        
        
        return list(set(lst))
count_actors(path, 1990, 2000)
