## 定额支付宝 脚本
import pyperclip
from selenium import webdriver    #  爬虫框架 、
from time import sleep  #  延时触发
from selenium.webdriver.chrome.options import Options   # google driver
import requests
import re
from sys import argv
chrome_drive =  'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe' #chrome drive 路径
chrome_options =Options
chrome_options.add_argument('--headless') ## 无界面模式
browser = webdriver.Chrome(executable_path=chrome_drive)
class result_text:
    def first_url(self,o=argv[1]):
        return o
    browser.get(first_url())  # 跳转当前url
    sleep(5)
    try:
        url = browser.current_url
        print('当前url{}'.format(url))

        path = browser.find_element_by_xpath('//*[@id="copy_url"]')  # 查找此模块元素
        path.click()
        browser.switch_to.alert.accept()
        sleep(1)
        paste = pyperclip.paste()
        txt = paste
        result_url = txt[18:]
    except Exception as error:
        print(error)

if __name__ == '__main__':
    r1 = re.compile(r'var a = "(\d*)";')
    r2 = re.compile(r'var j = "(.*)";')

    url = result_text()  # 调用类
    res = url.result_url # 取得最终跳转url 地址
    r = requests.get(res)
    r_text = r.text
    user_id = r1.findall(r_text)
    user = r2.findall(r_text)
    print(user_id,user)
