# a = []

# for i in range(5):
#     a.append(str(i))
# print(a)

# for i in range(len(a)):
#     print(a.index(str(i)))

# import csv

# c= open('workers.csv')
# cR= csv.reader(c)

# cl= list(cR)

# for i in cl:
#     print(i[1])

import smtplib, csv, os, random, time

t_open = open('25tasks.csv')
tReader = csv.reader(t_open)

dl=[]
for i in tReader:
    dl.append(str(i))
print(dl)