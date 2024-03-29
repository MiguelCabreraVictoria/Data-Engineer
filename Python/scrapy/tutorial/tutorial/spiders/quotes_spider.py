from pathlib import Path

import scrapy

"""
Spiders are classes that you define and that Scrapy uses to scrape information from a website. They must subclass Spider and define the initial request to make, optionally how to follow link in the pages, and hwo to parese the dowloaded page content to extract data.
"""


class QuotesSpider(scrapy.Spider):
    name = "quotes" #indetifies the Spider. it must be unique within a project

    start_urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",]
    
    
    """
A method that will be called to handle the response downloaded for each of the request made. The response parameter is an instance of TextResponse that holds the page content and has futher helpful methods to handle it

Usually parses the response extracting the scraped data as dicts and salso finding new URL´s to follow and creating new request
    """
    
    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }

            """
            The parse method looks for the link to the next page, builds a full absolute URL using the urljoin method and yields a new request to the next page, registering itself as callback to handle the data extraction for the next page and to keep the crawling going throught the pages
            """
            next_page = response.css("li.next a::attr(href)").get()

            if next_page is not None:
                next_page = response.urljoin(next_page)
                print(next_page)
                yield scrapy.Request(next_page, callback=self.parse)

"""
must return an iterable of Requests ( you can return a list of request or write a generator function) which the Spider will begin to crawl from. Subsequent requests will be generated successively from these initial request
"""





#Run Code scrapy crawl quotes
# scrapy crawl quotes -o quotes.json 
