import scrapy


class BigbankltItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
