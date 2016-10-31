# -*- coding: utf-8 -*-
import requests
from lxml import html
import json
import re

# headers = {'X-Requested-With': ' XMLHttpRequest'}

base_url = 'http://www.womai.com/{}'
next_page = 'http://www.womai.com/Sort-31000-6063.htm'
next_button_xpath = "//div[@class='page']/div[@class='page_l']/a[@class='next']/@onclick"
idsAll = []
namesAll = []
priceAll = []

file = open('womai.txt', 'a+')
file.write('id\t商品名\t价格\n')

while next_page:
    page = requests.get(next_page)
    tree = html.fromstring(page.content)

    re_extract = re.compile('id="itemPrice.*?(\d+)')
    ids_match = re.findall(re_extract, page.content)

    # print len(ids_match)
    # print len(idsAll)
    idsAll += ids_match
    # print len(idsAll)

    jd_names = tree.xpath("//div[@class='list-title']/p/a/text()")
    namesAll += jd_names
    # jd_ids = tree.xpath("//ul/li[@data-productid]/@data-productid")
    # idsAll += jd_ids
    next_pages = tree.xpath(next_button_xpath)
    # print next_pages
    if next_pages:
        re_extract = re.compile("\/(.*?)'")
        item_match = re.findall(re_extract, next_pages[0])
        if item_match:
            next_page = base_url.format(item_match[0])
            # print item_match[0]
    else:
        print "No next button found"
        next_page = None

    str = '&prices=buyPrice%2CWMPrice%2CmarketPrice%2CspecialPrice&defData=n&mid=0&cityid=31000&usergroupid=100&callback=jsonp1477535272568'
    skuIds = '%2C'.join(ids_match)
    print skuIds
    print ('http://price.womai.com/PriceServer/open/productlist.do?ids=%s%s'% (skuIds,str))
    page = requests.get('http://price.womai.com/PriceServer/open/productlist.do?ids=%s%s' % (skuIds,str))
    # print page.text

    # priceContent = page.text
    re_extract = re.compile("^jsonp1477535272568\((.*?)\)$")
    json_match = re.findall(re_extract, page.text)
    # print json_match[0]
    jsonStr = json.loads(json_match[0])
    for item in jsonStr['result']:
        priceAll.append(item['price']['buyPrice']['priceValue'])

print len(idsAll)
print len(namesAll)
print len(priceAll)

for i in range(len(idsAll)):
    print (idsAll[i].strip() + '\t' + namesAll[i].strip() + '\t' + priceAll[i].strip())
    out = idsAll[i].strip() + '\t' + namesAll[i].strip() + '\t' + priceAll[i].strip()
    file.write(out.encode('utf-8')+"\n")
file.close()