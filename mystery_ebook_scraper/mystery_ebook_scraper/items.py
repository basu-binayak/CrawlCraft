# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from itemloaders.processors import MapCompose

class MysteryEbookScraperItem(Item):
    title = Field(
        input_processor = MapCompose(lambda x : x.strip()) # Strip leading/trailing whitespace
        # output_processor = TakeFirst()
    )
    
    price = Field(
        input_processor=MapCompose(lambda x: x.replace('£', '').strip(),
                                   lambda x: float(x)),  # Remove currency symbol and strip
        # output_processor = TakeFirst()
    )
    
    availability = Field(
        input_processor=MapCompose(lambda x: ''.join(x).strip())
    )
    
    rating = Field(
        input_processor=MapCompose(lambda x : x.split(' ')[-1])
    )

# Here I have defined a MysteryEbookScarperItem with four fields - title, price, availability and rating. Each field is a scrapy.Field() object. 