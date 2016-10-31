from lxml import html
import requests
import re

headers = {
    'x-requested-with': 'XMLHttpRequest',
    'cookie': 'login-user=Irisdamon; nforum[UTMPUSERID]=Irisdamon; nforum[UTMPKEY]=56161361; nforum[UTMPNUM]=3718; nforum[PASSWORD]=CmriI6iZlaD1vLDWTirjWg%3D%3D; nforum[BMODE]=2; Hm_lvt_38b0e830a659ea9a05888b924f641842=1477274590; Hm_lpvt_38b0e830a659ea9a05888b924f641842=1477275679',
}

page = requests.get('https://bbs.byr.cn/board/Recommend?p=1&_uid=Irisdamon', headers=headers)
re_extract = re.compile('.*?<td class="title_9"><a href="(.*?)">(.*?)</a>(<samp class="tag-att ico-pos-article-attach"></samp>)?</td><td class="title_10">')
testString = ''
item_match = re.findall(re_extract, page.text)
if item_match:
    for item_info in item_match:
        print item_info[0]
        print item_info[1]


# tree = html.fromstring(page.text)
#
# title_xpath = '//td[@class="title_9"]/a/text()'
# author_xpath = '//a[@class="c63f"]/text()'
# titles = tree.xpath(title_xpath)
# authors = tree.xpath(author_xpath)
# print "We got %s titles and %s authors" % (len(titles), len(authors))
# for title in titles:
#     print title
# for author in authors:
#     print author
