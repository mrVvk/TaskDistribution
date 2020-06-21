import csv

lista_zadan = []

for i in range(25):
    a = 'task {}'.format(i+1)
    lista_zadan.append(a)

print(lista_zadan)

tasks_csv = open('25tasks.csv','w',newline='')
outputWriter = csv.writer(tasks_csv)

# for row in range(len(lista_zadan)):
#     outputWriter.writerow(lista_zadan[row])

# outputWriter.writerow(lista_zadan)

for i in lista_zadan:
    outputWriter.writerow([i])

tasks_csv.close()