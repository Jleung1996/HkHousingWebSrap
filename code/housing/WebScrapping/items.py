# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HousingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    price = scrapy.Field()
    price_per = scrapy.Field()
    area = scrapy.Field()
    tags = scrapy.Field()
    location = scrapy.Field()
    link = scrapy.Field()

    pass
