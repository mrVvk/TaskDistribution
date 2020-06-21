import csv, os

abs= os.getcwd()
c = open(os.path.join(abs,'tasks.csv'))
cf = csv.reader(c)

# l=list(cf)
# print(l)
l2=[]
for i in cf:
    l2.append(cf.line_num)
print(l2)
