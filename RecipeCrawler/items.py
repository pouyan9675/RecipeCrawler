import scrapy


class Recipe(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    photos = scrapy.Field()
    score = scrapy.Field()
    rating_num = scrapy.Field()
    reviews_num = scrapy.Field()
    prep_time = scrapy.Field()
    cook_time = scrapy.Field()
    total_time = scrapy.Field()
    serving_size = scrapy.Field()
    yield_ = scrapy.Field()
    ingredients = scrapy.Field()
    directions = scrapy.Field()
    calories = scrapy.Field()
    nutritions = scrapy.Field()


class Author(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()

