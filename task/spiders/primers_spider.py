import scrapy
import json

class PrimersSpiderSpider(scrapy.Spider):
    name = 'primers_spider'
    allowed_domains = ['midsouthshooterssupply.com/dept/reloading/primers?currentpage=1']
    start_urls = ['https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1/']

    def parse(self, response):
        container = response.css("div.product-container")
        products = container.css("div.product")
        result = []
        for product in products:
            price = product.css("span.price").css("span::text").get()
            title = product.css("a.catalog-item-name::text").get()
            stock = product.xpath("//span[@class='out-of-stock']/text()").get()
            if stock == "Out of Stock":
                stock = False
            else:
                stock = True
            manufacturer = product.css("a.catalog-item-brand::text").get()
            ele = {}
            ele["price"] = float(price[1:])
            ele["title"] = title
            ele["stock"] = stock
            ele["maftr"] = manufacturer
            result.append(ele)
        print(result)
        
        #optionally writing json data to a file
        with open('output.json', 'w') as f:
            json.dump(result, f)
        