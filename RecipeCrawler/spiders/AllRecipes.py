import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from RecipeCrawler.items import *


class AllrecipesSpider(CrawlSpider):
    name = 'AllRecipes'
    allowed_domains = ['allrecipes.com']
    start_urls = ['https://allrecipes.com/']

    rules = (
        Rule(LinkExtractor(allow=r'recipe\/', deny=[r'\?printview',r'recipe\/.*\?page=\d+']), callback='parse_item', follow=True),
        Rule(LinkExtractor(), follow=True),
    )

    def parse_item(self, response):
        item = {}

        splits = response.request.url.split('/')
        if len(splits) >= 5:
            item['id'] = splits[4]
        
        item['title'] = response.css('.headline-wrapper h1.heading-content::text').get()

        author = Author()
        author['name'] = response.css('div.author span.author-name::text').get()
        author['url'] = response.css('div.author a.author-block').attrib['href']
        item['author'] = author

        # item['photos']

        item['score'] = response.css('div.recipe-ratings span.review-star-text::text').get()       \
                            .replace('Rating:', '').replace('stars', '').strip()

        item['rating_num'] = response.css('div.recipe-review-container span.ugc-ratings-item::text').get()
        if item['rating_num']:
            item['rating_num'] = item['rating_num'].replace('Ratings', '').strip()
        else:
            item['rating_num'] = '0'


        # item['reviews_num'] = response.css('div.recipe-review-container a.ugc-reviews-link::text').get()
        # if item['reviews_num']:
        #     item['reviews_num'] = item['reviews_num'].replace('Ratings', '').strip()
        # else:
        #     item['reviews_num'] = 0

        meta_tags = response.css('.recipe-info-section section.recipe-meta-container div.recipe-meta-item')

        infobox = {}
        for meta in meta_tags:
            header = meta.css('.recipe-meta-item-header::text').get().replace(':', '').strip().lower()
            body = meta.css('.recipe-meta-item-body::text').get().strip()

            infobox[header] = body

        if 'prep' in infobox:
            item['prep_time'] = infobox['prep']

        if 'cook' in infobox:
            item['cook_time'] = infobox['cook']

        if 'total' in infobox:
            item['total_time'] = infobox['total']

        if 'servings' in infobox:
            item['serving_size'] = infobox['servings']

        if 'yield' in infobox:
            item['yield_'] = infobox['yield']


        ingradients = response.css('ul.ingredients-section li.ingredients-item span.ingredients-item-name::text')   \
                    .getall()
        ingradients = [x.strip() for x in ingradients]
        item['ingradients'] = ingradients

        item['directions'] = response.css('ul.instructions-section li.instructions-section-item div.section-body p::text').getall()

        item['calories'] = response.xpath('//div[@class="ng-dialog-content"]/div[@class="nutrition-top light-underline"]/span[text()="Calories:"]/following-sibling::text()[1]').get().strip()

        names = response.xpath('//div[@class="ng-dialog-content"]//*[@class="nutrition-body"]//*[@class="nutrition-row"]//span[@class="nutrient-name"]/text()[1]').getall()
        values = response.xpath('//div[@class="ng-dialog-content"]//*[@class="nutrition-body"]//*[@class="nutrition-row"]//span[@class="nutrient-name"]//span[@class="nutrient-value"]/text()').getall()
        nutrition = {}
        for k,v in zip(names,values):
            k = k.replace(':','').strip()
            v = v.strip()
            nutrition[k] = v
        item['nutritions']= nutrition

        return item
