import scrapy

class QuotesToScrape(scrapy.Spider):
	name = 'quotestoscrape'
	start_urls = ['https://quotes.toscrape.com/']

	def parse(self, response):
		quotes = response.css('div.quote')
		
		for quote in quotes:
			# text = quote.css('span.text::text').get().strip('\u201c').strip('\u201d'),
			text = quote.css('span.text::text').get(),
			author = quote.css('small.author::text').get(),
			tag = quote.css('meta').attrib['content']

			yield {
				'text' : text,
				'author' : author,
				'tag' : tag
				}

		next_page = 'https://quotes.toscrape.com' + response.css('li.next').css('a').attrib['href']
		if next_page is not None:
			yield response.follow(next_page, callback=self.parse)