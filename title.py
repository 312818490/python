
#python/title.py
#递归爬取网站板块的博主 在线人数 url 
import requests
from lxml import etree

class bbs():
    domain = 'http://www.newsmth.net'
    parse_url ='/nForum/section/{}?ajax '
    headers = {
        'Host': "www.newsmth.net",
        'Connection': "keep-alive",
        'Accept': "*/*",
        'X-Requested-With': "XMLHttpRequest",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        'Referer': "https://www.newsmth.net/nForum/",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cookie':  "left-index=10000000000; main[UTMPUSERID]=guest; main[UTMPKEY]=94372357; main[UTMPNUM]=11889; Hm_lvt_bbac0322e6ee13093f98d5c4b5a10912=1558715510,1558879145; Hm_lpvt_bbac0322e6ee13093f98d5c4b5a10912=1558880176",
        'cache-control': "no-cache",
    }
    def get_page(self,page_num):
        all_url = self.domain + self.parse_url.format(page_num)
        respone = requests.get(all_url,headers =self.headers)
        return respone.text

    def bord_list(self,connect):
        tree =etree.HTML(connect)
        #//*[@id="body"]/div[2]/table/thead/tr
        rows = tree.xpath('//table[@class="board-list corner"]/tbody/tr')
        boards = []
        for row in rows:
            board = {}
            columns = row.xpath('td')
            board['url'] = columns[0].xpath('a')[0].attrib['href']
            board['title'] = columns[0].xpath('a')[0].text

            if len(columns[1].xpath('a')) != 0:
                board['版主'] = columns[1].xpath('a')[0].text
            else:
                url = self.domain + board['url']
                r = requests.get(url,headers=self.headers)
                chid = self.bord_list(r.text)
                boards.append(chid)
            boards.append(board)
            board['在线'] = columns[3].text
        print(boards)











if __name__ == '__main__':
    bb = bbs()
    for i in range(1,9):
        c =bb.get_page(i)
        bb.bord_list(c)
        
    
