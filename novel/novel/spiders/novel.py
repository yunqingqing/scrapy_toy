import scrapy

from novel import items

class NovelSpider(scrapy.Spider):
    name = "novel"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "https://www.xbiquge.cc/book/5598/3599127.html"
    ]

    def parse(self, response):
        item = items.NovelItem()
        content = ""
        item['title'] = response.xpath('//div[@class="bookname"]/h1/text()')[0].extract()
        for sel in response.xpath('//div[@id="content"]/text()'):
            content += sel.extract()

        item['content'] = content
        item['next'] = response.xpath('//div[@class="bottem"]/a[last()-1]/@href').extract()
        yield item
        