from bs4 import BeautifulSoup
from urllib.request import urlopen
import re  # 正则模块
import requests


# 主要修改的地方
words = 'topological insulator'
number = 3


key_words = {'clauses': '[{"field":"all","value":"'+words+'","operator":"AND"}]','sort': 'relevance', 'per_page': number}
r = requests.get('https://journals.aps.org/search/results', params=key_words)
print('\n响应结果：', r)
print('\n访问的链接是：', r.request.url)

soup = BeautifulSoup(r.text, features='lxml')

all_script = soup.find_all('script')
print('')
for script in all_script:  
    if re.search(re.compile('^window.results'), script.get_text()):  # 在所有script中找出包含主要内容的script区域
        n = 0
        for s in re.split('{"actions":', script.get_text()):   # 用字符串'{"actions":'把每个搜索的结果分开
            if re.search(re.compile('title.*?date'), s) != None:  # 只选取有包含title的区域
                n += 1
                print(n)
                print('标题：', re.search(re.compile('title.*?date'), s).group()[8:-7])  # 找出对应搜索结果的标题
                link = re.search(re.compile(',"link":".*?title'), s).group()[9:-8]
                if re.search(re.compile('^http'), link):
                    print('链接：', link)
                else:
                    print('链接：https://journals.aps.org'+ link)
                print('')