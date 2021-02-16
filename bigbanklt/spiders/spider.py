import scrapy

from scrapy.loader import ItemLoader
from ..items import BigbankltItem
from itemloaders.processors import TakeFirst


class BigbankltSpider(scrapy.Spider):
	name = 'bigbanklt'
	start_urls = ['https://www.bigbank.lt/blog/']

	def parse(self, response):
		post_links = response.xpath('//div[@class="col col-12-24"]/div/a/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//section[@class="color-navy bg- "]//div[@class="wrapper fluid"]//text()[normalize-space() and not(ancestor::a)]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()

		item = ItemLoader(item=BigbankltItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		return item.load_item()
