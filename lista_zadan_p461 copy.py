import smtplib, csv, os, random, time
print(os.getcwd())
t_open = open('25tasks.csv')
tReader = csv.reader(t_open)
w_open = open('workers.csv')
wReader = csv.reader(w_open)

    
dl = list(tReader)
# print(duty_list)
worker_list = list(wReader)

duty_list = []
for row in range(0,21,5):
    duty_list.append(dl[row:row+5])
# print(worker_list)
# print(duty_list)
print(duty_list)
print(duty_list[3])
worker_duties2do = {}
# for i in range(1,25,5):


# for i in worker_list:
#     worker_duties2do.setdefault(i[0],duty_list)

# print(worker_duties2do)

# smtpObj= smtplib.SMTP('smtp.gmail.com', 587)
# smtpObj.ehlo()
# smtpObj.starttls()
# smtpObj.login('wojtus.dla.sandi@gmail.com','maluj123')

    # for i in worker_duty_list:
        
    #     randDuty = random.choice(duty_list)
    #     body = 'Good morning {}! \n Your task for today is: {}'.format(i[0],randDuty)
    #     duty_list.remove(randDuty)

    #     smtpObj.sendmail('wojtus.dla.sandi@gmail.com',i[1], 'Subject:Task for today \n {}'.format(body))

