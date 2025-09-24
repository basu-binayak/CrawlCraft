import scrapy # Import Scrapy framework

# Define a spider class inheriting from scrapy.Spider
class BooksToScrapeSpider(scrapy.Spider):
    
    # Unique name for this spider (used to run it)
    name = "books_to_scrape"
    
    # Domains that this spider is allowed to scrape
    allowed_domains = ["books.toscrape.com"]
    
    # Starting URL(s) for the spider
    start_urls = ["https://books.toscrape.com/"]
    
    # Parse function is called for each response from start_urls or followed links
    def parse(self, response):
        # Loop through all books on the current page
        for book in response.css("article.product_pod"):
            # Extract and yield data for each book as a Python dictionary
            yield {
                # Get book title from the 'title' attribute of the <a> tag inside <h3>
                'title' : book.css("h3 > a::attr(title)").get(),
                
                # Get book price (text inside <p class="price_color">)
                'price' : book.css("p.price_color::text").get()[1:], # get() returns the first match
                
                # Get availability status
                # .getall() returns a list of all texts, the last item contains availability info
                # .strip() removes any extra spaces or newline characters
                'availability' : book.css("p.availability::text").getall()[-1].strip(),
                
                # Get the ratings 
                # The rating is a class itself i.e. <p class="star-rating Three"> and alll we want is the Three
                'rating': book.css("p.star-rating::attr(class)").get().split(' ')[-1]
            }
        