import scrapy

class vehicle_urls (scrapy.Item):
    images = scrapy.Field()
    image_urls = scrapy.Field()
    address =scrapy.Field()
    keywords = scrapy.Field()
    make = scrapy.Field()
    model = scrapy.Field()
    year = scrapy.Field()
    bodyType = scrapy.Field()
    listing_id = scrapy.Field()
    price = scrapy.Field()
    color_ext = scrapy.Field()
    color_int = scrapy.Field()
    transmission = scrapy.Field()
    mileage = scrapy.Field()
    restored = scrapy.Field()
    listing_url = scrapy.Field()

