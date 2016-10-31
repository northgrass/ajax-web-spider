from lxml import html
import requests

headers = {
    # 'accept-encoding': 'gzip, deflate, sdch, br',
    'x-requested-with': 'XMLHttpRequest',
    # 'accept-language': 'zh-CN,zh;q=0.8',
    # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    # 'accept': '*/*',
    # 'cache-control': 'max-age=0',
    # 'authority': 'bbs.byr.cn',
    'cookie': 'login-user=Irisdamon; nforum[UTMPUSERID]=Irisdamon; nforum[UTMPKEY]=56161361; nforum[UTMPNUM]=3718; nforum[PASSWORD]=CmriI6iZlaD1vLDWTirjWg%3D%3D; nforum[BMODE]=2; Hm_lvt_38b0e830a659ea9a05888b924f641842=1477274590; Hm_lpvt_38b0e830a659ea9a05888b924f641842=1477275679',
    # 'if-modified-since': 'Sun, 23 Oct 2016 12:55:26 GMT',
    # 'referer': 'https://bbs.byr.cn/',
}
# cookie:         login-user=Irisdamon; nforum[UTMPUSERID]=Irisdamon; nforum[UTMPKEY]=41615157; nforum[UTMPNUM]=3321; nforum[PASSWORD]=CmriI6iZlaD1vLDWTirjWg%3D%3D; Hm_lvt_38b0e830a659ea9a05888b924f641842=1477274590,1477298664; Hm_lpvt_38b0e830a659ea9a05888b924f641842=1477298670; nforum[BMODE]=2

page = requests.get('https://bbs.byr.cn/board/Recommend?p=1&_uid=Irisdamon', headers=headers)
tree = html.fromstring(page.text)

title_xpath = '//td[@class="title_9"]/a/text()'
author_xpath = '//a[@class="c63f"]/text()'
titles = tree.xpath(title_xpath)
authors = tree.xpath(author_xpath)
print "We got %s titles and %s authors" % (len(titles), len(authors))
for title in titles:
    print title
for author in authors:
    print author
