import pyperclip
from  selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
chrome_drive = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
req_url = "https://yeah.hdy1949.com/api/pay_trade?cid=1015&tid=130712171"
chrome_options=Options()
#设置chrome浏览器无界面模式
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(executable_path=chrome_drive)
# 开始请求
browser.get(req_url)
sleep(5)
#打印页面网址
try:
    url = browser.current_url
    print(url)
    bb =browser.find_element_by_xpath('//*[@id="copy_url"]')
    if url == 'http://www.wap321.cn/Pay_Index.html':
        print(bb.text)

        bb.click()
        browser.switch_to.alert.accept()
        sleep(2)
        paste = pyperclip.paste()
        print(paste)
    else:
        cc =browser.find_element_by_xpath('//*[@id="payBtn"]')
        cc_url = cc.click()

        paste = pyperclip.paste()
        print(paste)

        #document.querySelector("#copy_url")


except Exception:
    print(Exception)

#关闭浏览器
browser.close()
#关闭chromedriver进程

#//*[@id="payBtn"]
