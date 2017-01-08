import scrapy

class QuotesSpider(scrapy.Spider):
	name = "vehicle"
	
	def start_requests(self):
		url = 'https://www.car.gr/classifieds/'
		tag = getattr(self, 'tag', None)
		if tag is not None:
		    url = url + tag
		yield scrapy.Request(url, self.parse)

	def parse(self, response):
		for vehicle in response.css('.clsfd_list_row_group'):
			
			yield {
		        'title': vehicle.css(".vehicle").css("span.p_t strong").xpath('.//span/text()').extract(),
			'time': vehicle.css(".clsfd_list_row_options").xpath('.//strong/text()').extract()[0],
			'registration': vehicle.css(".registration").xpath('.//text()').extract()[0].strip(),
			'mileage': vehicle.css(".mileage").xpath('.//text()').extract()[0].strip(),
			'price': vehicle.css(".price").xpath('.//span/text()').extract()[0].split()[1],
			'condition': vehicle.xpath('.//strong[contains(@itemprop, "itemCondition")]/text()').extract(),
			'engine': vehicle.css(".engine").xpath('.//text()').extract()[0].strip(),
			'power': vehicle.css(".power").xpath('.//text()').extract()[0].strip(),
			'transmision': vehicle.css(".transmision").xpath('.//text()').extract()[0].strip(),
			'fueltype': vehicle.css(".fueltype").xpath('.//text()').extract()[0].strip(),
			'city': vehicle.css(".city").xpath('.//span[contains(@itemprop, " addressRegion ")]/text()').extract(),
			'category': vehicle.xpath('.//span[starts-with(@id,"clsfd_category_")]/text()').extract()[0],			
            	}
		next_page = response.css('a.next::attr(href)').extract_first()
        	if next_page is not None:
            		next_page = response.urljoin(next_page)
            		yield scrapy.Request(next_page, callback=self.parse)
