import scrapy


class PetMarketSpider(scrapy.Spider):
    name = "petmarket"
    fields = {
        'link_pagination': '//div[@class="pagination"]//a/@href',
        'link_category': '//div[@class="category-image"]/a/@href',
        'product': '//div[@class="row bxr-list"]',
        'price': './/span[@class="bxr-market-current-price bxr-market-format-price"]/text()',
        'old_price': './/span[@class="bxr-market-old-price"]/text()',
        'name': './div[@id!=""]/div/div/div[@class="bxr-element-name"]/a/@title',
        'img': './div[@id!=""]/div/div/div[@class="bxr-element-image"]/a/img/@src',
        'product_link': './div[@id!=""]/div/div/div/a/@href'
    }
    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 0,
        'CLOSESPIDER_ITEMCOUNT': 20
    }
    start_urls = [
        'https://tennismag.com.ua/catalog/myachi-futbolnye/',
        'https://tennismag.com.ua/catalog/muzhskie-krossovki/',
        'https://tennismag.com.ua/catalog/myachi/',
        'https://tennismag.com.ua/catalog/sumki/'
    ]
    allowed_domains = [
        'tennismag.ua'
    ]

    def parse(self, response):
        print(response.xpath('//div[@class="row bxr-list"]/div[@id!=""]/div/div/div'))
        for product in response.xpath(self.fields["product"]):
            price = product.xpath(self.fields['price']).get()
            print(type(product))
            yield {
                'link': product.xpath(self.fields['product_link']).get(),
                'price': price.strip() if price else product.xpath(self.fields['old_price']).get().strip(),
                'img': product.xpath(self.fields['img']).get(),
                'name': product.xpath(self.fields['name']).get()
            }
        '''for a in response.xpath(self.fields["link_category"]):
            yield response.follow(a.extract(), callback=self.parse)
        for a in response.xpath(self.fields["link_pagination"]):
            yield response.follow(a.extract(), callback=self.parse)
        '''