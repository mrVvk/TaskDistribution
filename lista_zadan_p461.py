import smtplib, csv, os, random, time

t_open = open('tasks.csv')
tReader = csv.reader(t_open)
w_open = open('workers.csv')
wReader = csv.reader(w_open)

duty_list = list(tReader)
worker_list = list(wReader)

print(worker_list)

smtpObj= smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('wojtus.dla.sandi@gmail.com','maluj123')

for i in worker_list:
    worker_duty_list=[]
    workertask.append(i)

    for i in worker_duty_list:
        
        randDuty = random.choice(duty_list)
        body = 'Good morning {}! \n Your task for today is: {}'.format(i[0],randDuty)
        duty_list.remove(randDuty)

        smtpObj.sendmail('wojtus.dla.sandi@gmail.com',i[1], 'Subject:Task for today \n {}'.format(body))

