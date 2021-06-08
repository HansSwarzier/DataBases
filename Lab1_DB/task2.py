from scrapy import cmdline
import os
import lxml.etree as ET


def crawl():
    try:
        os.remove("results/tennismarket.xml")
    except OSError:
        print("results/tennismarket.xml not found")
    cmdline.execute("scrapy crawl petmarket -o results/tennismarket.xml".split())


def xslt_parse():
    dom = ET.parse('results/tennismarket.xml')
    xslt = ET.parse('results/tennismarket.xsl')
    transform = ET.XSLT(xslt)
    newdom = transform(dom)
    with open('results/tennismarket.html', 'wb') as f:
        f.write(ET.tostring(newdom, pretty_print=True))

#crawl()
xslt_parse()
