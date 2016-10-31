import requests
import re

url = 'http://book.douban.com/series/1163?page=11'
re_extract = re.compile('<a href="(.*?)" title="(.*?)"[\S\s]*?class="pub">([\S\s]*?)<\/div>')
page = requests.get(url)
item_match = re.findall(re_extract, page.content)
if item_match:
    for item_info in item_match:
        print item_info
        print item_info[0]
        print item_info[1]
        print item_info[2].strip(), '\n'