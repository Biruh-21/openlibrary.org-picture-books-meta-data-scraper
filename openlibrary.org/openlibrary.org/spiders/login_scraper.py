import scrapy


class LoginScraperSpider(scrapy.Spider):
    name = "login_scraper"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/login"]

    def parse(self, response):

        yield scrapy.FormRequest.from_response(
            response,
            formxpath="//form",
            formdata={"username": "admin", "password": "admin"},
            callback=self.after_login,
        )

    def after_login(self, response):
        if response.xpath("(//a[@href='/logout'])/text()").get():
            print("You're loggedin")
