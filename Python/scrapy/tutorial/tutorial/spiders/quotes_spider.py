from pathlib import Path

import scrapy

"""
Spiders are classes that you define and that Scrapy uses to scrape information from a website. They must subclass Spider and define the initial request to make, optionally how to follow link in the pages, and hwo to parese the dowloaded page content to extract data.
"""


class QuotesSpider(scrapy.Spider):
    name = "quotes" #indetifies the Spider. it must be unique within a project

"""
must return an iterable of Requests ( you can return a list of request or write a generator function) which the Spider will begin to crawl from. Subsequent requests will be generated successively from these initial request
"""
    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

"""
A method that will be called to handle the response downloaded for each of the request made. The response parameter is an instance of TextResponse that holds the page content and has futher helpful methods to handle it

Usually parses the response extracting the scraped data as dicts and salso finding new URL´s to follow and creating new request
"""
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")


#Run Code scrapy crawl quotes
