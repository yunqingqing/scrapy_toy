# http://mysql.taobao.org/monthly/

import scrapy

from mysql_taobao_blog import items

domain = 'http://mysql.taobao.org'

urls = ['/monthly/2020/03', '/monthly/2020/02', '/monthly/2020/01', '/monthly/2019/12', '/monthly/2019/11', '/monthly/2019/10', '/monthly/2019/09',
'/monthly/2019/08', '/monthly/2019/07', '/monthly/2019/06', '/monthly/2019/05', '/monthly/2019/04', '/monthly/2019/03', '/monthly/2019/02',
'/monthly/2019/01', '/monthly/2018/12', '/monthly/2018/11', '/monthly/2018/10', '/monthly/2018/09', '/monthly/2018/08', '/monthly/2018/07',
'/monthly/2018/06', '/monthly/2018/05', '/monthly/2018/04', '/monthly/2018/03', '/monthly/2018/02', '/monthly/2018/01', '/monthly/2017/12', '/monthly/2017/11',
'/monthly/2017/10', '/monthly/2017/09', '/monthly/2017/08', '/monthly/2017/07', '/monthly/2017/06', '/monthly/2017/05', '/monthly/2017/04',
'/monthly/2017/03', '/monthly/2017/02', '/monthly/2017/01', '/monthly/2016/12', '/monthly/2016/11', '/monthly/2016/10', '/monthly/2016/09',
'/monthly/2016/08', '/monthly/2016/07', '/monthly/2016/06', '/monthly/2016/05', '/monthly/2016/04', '/monthly/2016/03', '/monthly/2016/02', '/monthly/2016/01', 
'/monthly/2015/12', '/monthly/2015/11', '/monthly/2015/10', '/monthly/2015/09', '/monthly/2015/08', '/monthly/2015/07', '/monthly/2015/06', 
'/monthly/2015/05', '/monthly/2015/04', '/monthly/2015/03', '/monthly/2015/02', '/monthly/2015/01', '/monthly/2014/12', '/monthly/2014/11',
'/monthly/2014/10', '/monthly/2014/09', '/monthly/2014/08'] 

class BlogSpider(scrapy.Spider):
    name = "mysql_taobao_blog"
    allowed_domains = ["mysql.taobao.org"]
    start_urls = [domain+url for url in urls]

    def parse(self, response):
        item = items.MysqlTaobaoBlogItem()
        links = response.xpath('//ul[@class="posts"]/li/h3/a/@href').extract()
        titles = response.xpath('//ul[@class="posts"]/li/h3/a/text()').extract() 
        for i in zip(links, titles):
            item['title'] = i[1].strip()
            item['link'] = domain+i[0].strip()
            yield item
        