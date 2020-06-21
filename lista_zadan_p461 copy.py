import smtplib, csv, os, random, time
print(os.getcwd())
t_open = open('25tasks.csv')
tReader = csv.reader(t_open)
w_open = open('workers.csv')
wReader = csv.reader(w_open)

    
dl = list(tReader)
Dl=[]
for i in dl:
    Dl.append(i[0])
print(Dl)

worker_list = list(wReader)
print('worker list: \n', worker_list)

duty_list = []
# for row in range(0,21,5):
#     duty_list.append(dl[row:row+5])
#     print(dl[row])
for row in range(0,len(Dl),len(worker_list)):
    duty_list.append(Dl[row:row+5])


print('duty list: \n',duty_list)


ToDo = {}
for i in range(len(duty_list)):
    ToDo.setdefault(worker_list[i][0],duty_list[i])
print(' ToDo: \n', ToDo)

done = {}
for worker in range(len(worker_list)):
    done.setdefault(worker_list[worker][0], [])
print('duties - done! \n', done)





# smtpObj= smtplib.SMTP('smtp.gmail.com', 587)
# smtpObj.ehlo()
# smtpObj.starttls()
# smtpObj.login('wojtus.dla.sandi@gmail.com','maluj123')

    # for i in worker_duty_list:
        
    #     randDuty = random.choice(duty_list)
    #     body = 'Good morning {}! \n Your task for today is: {}'.format(i[0],randDuty)
    #     duty_list.remove(randDuty)

    #     smtpObj.sendmail('wojtus.dla.sandi@gmail.com',i[1], 'Subject:Task for today \n {}'.format(body))

