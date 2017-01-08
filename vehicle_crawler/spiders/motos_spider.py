import scrapy


class QuotesSpider(scrapy.Spider):
	name = "motos"
	start_urls = [
	'https://www.car.gr/classifieds/bikes/?condition=%CE%9A%CE%B1%CE%B9%CE%BD%CE%BF%CF%8D%CF%81%CE%B9%CE%BF&condition=%CE%9C%CE%B5%CF%84%CE%B1%CF%87%CE%B5%CE%B9%CF%81%CE%B9%CF%83%CE%BC%CE%AD%CE%BD%CE%BF&offer_type=sale&pg=1&variant=kle+500'
	]

	def parse(self, response):
		for moto in response.css('.clsfd_list_row_group'):
			
			yield {
		        'title': moto.css(".vehicle").css("span.p_t strong").xpath('.//span/text()').extract(),
			'time': moto.css(".clsfd_list_row_options").xpath('.//strong/text()').extract()[0],
			'registration': moto.css(".registration").xpath('.//text()').extract()[0].strip(),
			'mileage': moto.css(".mileage").xpath('.//text()').extract()[0].strip(),
			'price': moto.css(".price").xpath('.//span/text()').extract()[0].split()[1],
			'condition': moto.xpath('.//strong[contains(@itemprop, "itemCondition")]/text()').extract(),
			'engine': moto.css(".engine").xpath('.//text()').extract()[0].strip(),
			'power': moto.css(".power").xpath('.//text()').extract()[0].strip(),
			'transmision': moto.css(".transmision").xpath('.//text()').extract()[0].strip(),
			'fueltype': moto.css(".fueltype").xpath('.//text()').extract()[0].strip(),
			'city': moto.css(".city").xpath('.//span[contains(@itemprop, " addressRegion ")]/text()').extract(),			
            	}
		next_page = response.css('a.next::attr(href)').extract_first()
        	if next_page is not None:
            		next_page = response.urljoin(next_page)
            		yield scrapy.Request(next_page, callback=self.parse)
