import scrapy
from ..items import HousingItem

class HousingSpider (scrapy.Spider):
    name = 'midlife'


    def parse(self, response):
        items = HousingItem()
        list_house = response.css('.content')
        for house in list_house:
            items['link'] = house.css('img.desktop_myimage.detail_page::attr(href)').extract()
            items['price'] = house.css('.priceDesc::text').extract()
            items['price_per'] = house.css('.unitPrice::text').extract()
            items['location'] = house.css('.cat::text').extract()
            items['tags'] = house.css('.label::text').extract()
            items['area'] = house.css('div.header::text')[6].extract()
            yield items
            next_page = 'https://www.squarefoot.com.hk/buy?page='+str(HousingSpider.page_number)+'&searchText=&myfav=&myvisited=&item_ids=&sortBy''=&search_words_thing=default&buyRent=buy&mobilePageChannel=&cat_ids=&search_words_value' \
                        '=&is_return_newmenu=0&plan_id=&propertyDoSearchVersion=2.0&sortBy=default&locations=0' \
                        '&locations_by_text=0&price=0&price_by_text=0&mainType=0&mainType_by_text=0&others=0' \
                        '&others_by_text=0&roomRange=&roomRange_by_text=0&areaOption=&areaOption_by_text=0&areaRange' \
                        '=&areaRange_by_text=0&yearRange=&yearRange_by_text=0&floors=&floors_by_text=0&searchTags' \
                        '=&searchTags_by_text=0'
            if HousingSpider.page_number < 610:
                HousingSpider.page_number += 1
                yield response.follow(next_page, callback=self.parse)

