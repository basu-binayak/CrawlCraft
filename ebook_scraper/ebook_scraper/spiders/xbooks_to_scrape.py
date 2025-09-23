import scrapy # Import Scrapy framework

# Define a spider class inheriting from scrapy.Spider
class BooksToScrapeSpider(scrapy.Spider):
    # Unique name for this spider (used to run it)
    name = "xbooks_to_scrape"
    
    # Domains that this spider is allowed to scrape
    allowed_domains = ["books.toscrape.com"]
    
    # Starting URL(s) for the spider
    start_urls = ["https://books.toscrape.com/"]
    
    