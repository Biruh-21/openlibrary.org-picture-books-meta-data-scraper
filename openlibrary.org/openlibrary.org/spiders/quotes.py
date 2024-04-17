import scrapy
import json


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/api/quotes?page=1"]

    def parse(self, response):
        resp = json.loads(response.body)
        quotes = resp["quotes"]
        print(quotes)
        for quote in quotes:
            yield {
                "Author": quote["author"]["name"],
                "Tags": quote["tags"],
                "quote_text": quote["text"],
            }

        has_next = resp["has_next"]
        if has_next:
            next_page = resp["page"] + 1
            yield scrapy.Request(
                url=f"https://quotes.toscrape.com/api/quotes?page={next_page}",
                callback=self.parse,
            )
