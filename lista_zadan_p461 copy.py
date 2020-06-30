import smtplib
import csv
import os
import random
import time
print(os.getcwd())
t_open = open('25tasks.csv')
tReader = csv.reader(t_open)
w_open = open('workers.csv')
wReader = csv.reader(w_open)


dl = list(tReader)
print('dl: \n', dl)
Dl = []
for i in dl:
    Dl.append(i[0])
print('Dl: \t', Dl)


worker_list = list(wReader)
print('worker list: \n', worker_list)

ToDo = {}
for worker in (worker_list):

    randDl = []
    for i in range(5):
        randD = random.choice(Dl)
        randDl.append(randD)
        Dl.remove(randD)
    ToDo[worker[0]] = randDl

print('ToDo \n', ToDo)

done = {}


def send_mail():
    # for worker in range(len(worker_list)):
    #    worker_list[worker]= rand_duty.append(randD)
    # Dl.remove(randD)

    # print('Dl: \n',Dl)
    # print('worker_list: \n',worker_list)

    # duty_list = []
    # for row in range(0,len(Dl),len(worker_list)):
    #     duty_list.append(Dl[row:row+5])

    # print('duty list: \n',duty_list)

    # ToDo = {}
    # for i in range(len(duty_list)):
    #     ToDo.setdefault(worker_list[i][0],duty_list[i])
    # print(' ToDo: \n', ToDo)

    # done = {}
    # for worker in range(len(worker_list)):
    #     done.setdefault(worker_list[worker][0], [])
    # print('duties - done! \n', done)

    # smtpObj= smtplib.SMTP('smtp.gmail.com', 587)
    # smtpObj.ehlo()
    # smtpObj.starttls()
    # smtpObj.login('wojtus.dla.sandi@gmail.com','maluj123')

    # for i in worker_duty_list:

    #     randDuty = random.choice(duty_list)
    #     body = 'Good morning {}! \n Your task for today is: {}'.format(i[0],randDuty)
    #     duty_list.remove(randDuty)

    #     smtpObj.sendmail('wojtus.dla.sandi@gmail.com',i[1], 'Subject:Task for today \n {}'.format(body))
