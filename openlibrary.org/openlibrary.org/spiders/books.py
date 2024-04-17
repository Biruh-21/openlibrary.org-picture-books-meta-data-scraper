import scrapy
import json


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["openlibrary.org"]
    start_urls = ["https://openlibrary.org/subjects/picture_book.json?limit=12"]

    counter = 0

    def parse(self, response):
        resp = json.loads(response.body)
        works = resp["works"]

        for work in works:
            yield {
                "title": work["title"],
                "edition_no": work["edition_count"],
                "Authors": [i["name"] for i in work["authors"]],
            }
        self.counter += 1
        offset = 12
        end_of_list = offset * self.counter
        if end_of_list <= 252:
            yield scrapy.Request(
                url=f"https://openlibrary.org/subjects/picture_book.json?limit=12&offset={end_of_list}",
                callback=self.parse,
            )
