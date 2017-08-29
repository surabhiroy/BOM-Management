import scrapy
import csv


class QuotesSpider(scrapy.Spider):
	name = "spidey"

	def start_requests(self):
		with open('tester.txt', 'r', encoding='utf-8') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=',')
			i = 0
			for row in spamreader:
				i += 1
				if i < 3:
					continue
				else:
					mpn = row[3]
					homepage = 'https://www.digikey.com/products/en?keywords='
					url = homepage + mpn
						# print(url)
					yield scrapy.Request(url, self.parse_resp)

	def parse_resp(self, response):
		ori = response.request.url.split("=")
		compliance = response.css('.rohs-foilage').extract_first()
		with open("output.csv", "a", encoding='utf-8') as f:
			if compliance is not None:
				if "is RoHS compliant" in compliance:
					f.write(ori[1] + "," + "compliant")
					f.write("\n")
			else:
				f.write(ori[1] + "," + "error")
				f.write("\n")
				# yield scrapy.Request(url, self.parse)



	# def parse(self, response):
	# 	for quote in response.css('div.quote'):
	# 		yield {
	# 			'text': quote.css('span.text::text').extract_first(),
	# 			'author': quote.css('small.author::text').extract_first(),
	# 			'tags': quote.css('div.tags a.tag::text').extract(),
	# 		}

	# 	next_page = response.css('li.next a::attr(href)').extract_first()
	# 	if next_page is not None:
	# 		next_page = response.urljoin(next_page)
	# 		yield scrapy.Request(next_page, callback=self.parse)

