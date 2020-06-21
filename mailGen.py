import csv


workers_csv = open('workers.csv','w',newline='')
outputWriter = csv.writer(workers_csv)

for i in range(5):
    worker_info = []
    wname = 'worker{}'.format(i)
    wmail = 'wojtus.dla.sandi@gmail.com'
    worker_info.append(wname)
    worker_info.append(wmail)
    outputWriter.writerow(worker_info)


print(worker_info)

# workers_csv = open('workers.csv','w',newline='')
# outputWriter = csv.writer(workers_csv)

# for row in range(len(worker_info)):
#     outputWriter.writerow(worker_info[row])

# outputWriter.writerow(worker_info)

# for i in worker_info:
#     outputWriter.writerow([i])

workers_csv.close()