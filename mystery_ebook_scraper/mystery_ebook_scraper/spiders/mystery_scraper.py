import scrapy
from scrapy.loader import ItemLoader
from mystery_ebook_scraper.items import MysteryEbookScraperItem
from itemloaders.processors import TakeFirst

class MysteryEbookScraperSpider(scrapy.Spider):
    name = "mystery_scraper"
    start_urls = ["https://books.toscrape.com/catalogue/category/books/mystery_3/"]
    
    def parse(self, response):
        mystery_books = response.xpath("//article[contains(concat(' ' , normalize-space(@class), ' '), ' product_pod ')]")
        
        for mystery_book in mystery_books:
            # Create an ItemLoader instance for each ebook
            loader = ItemLoader(item=MysteryEbookScraperItem(), selector=mystery_book)
            
            loader.add_xpath("title", "./h3/a/@title")
            loader.add_xpath("price", "//p[@class='price_color']/text()")
            
            check_stock = mystery_book.xpath("//p[@class='instock availability']/i/@class").get()
            if check_stock == "icon-ok":
                loader.add_xpath("availability", "//p[@class='instock availability']/text()")
            else:
                loader.add_value('availability', 'Not In Stock')
            
            loader.add_xpath("rating", "//p[contains(concat(' ', normalize-space(@class), ' '), ' star-rating ')]/@class")
                
            loader.default_output_processor = TakeFirst()
            
            # Yield the item (instead of a dictionary)
            yield loader.load_item()
            
            
            