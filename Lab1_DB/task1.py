from scrapy import cmdline
from lxml import etree

cmdline.execute("scrapy crawl golosua".split())
root = None
with open('results/shkole.xml', 'r') as file:
    root = etree.parse(file)

pagesCount = root.xpath('count(//page)')
textFragmentsCount = root.xpath('count(//fragment[@type="text"])')
print('Average count of text fragments per page %f' % (textFragmentsCount / pagesCount))
