import scrapy


class OpenlibraryLoginSpider(scrapy.Spider):
    name = "openlibrary_login"
    allowed_domains = ["openlibrary.org"]
    start_urls = ["https://openlibrary.org/account/login"]

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            formxpath="(//form)[2]",
            formdata={"username": "biruhtesfaye2121@gmail.com", "password": "password"},
            callback=self.after_login,
        )

    def after_login(self, response):
        if response.xpath("(//a[@href='/people/biruht'])[1]/text()").get():
            print("You have logged in successfuly!")
