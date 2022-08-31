# RecipeCrawler
A crawler built by Scrapy to crawl recipe from different websites and save them as structrued data.

The extracted data looks like this:
```
{
  "id": "259887", 
  "title": "Simple Teriyaki Sauce", 
  "author": {
        "name": "Goat Berry Kitchen", 
        "url": "https://www.allrecipes.com/cook/goatberrykitchen/"
        }, 
  "score": "4.44", 
  "rating_num": "263", 
  "prep_time": "5 mins", 
  "cook_time": "6 mins", 
  "total_time": "11 mins", 
  "serving_size": "12", 
  "yield_": "cups", 
  "ingradients": [
        "1 cup water", 
        "1/4 cup soy sauce", 
        "5 teaspoons packed brown sugar", 
        "1 tablespoon honey, or more to taste", 
        "1/2 teaspoon ground ginger", 
        "1/4 teaspoon garlic powder", 
        "2 tablespoons cornstarch", 
        "1/4 cup cold water"
        ], 
  "directions": [
        "Combine 1 cup water, soy sauce, brown sugar, honey, ginger, and garlic powder in a saucepan over medium heat. Cook until nearly heated through, about 1 minute.", 
        "Mix cornstarch and 1/4 cold water together in a cup; stir until dissolved. Add to the saucepan. Cook and stir sauce until thickened, 5 to 7 minutes."
        ], 
  "calories": "21", 
  "nutritions": {
        "protein": "0.4g", 
        "carbohydrates": "5g", 
        "dietary fiber": "0.1g", 
        "sugars": "3.4g", 
        "vitamin a iu": "0.1IU", 
        "niacin equivalents": "0.2mg", 
        "folate": "0.8mcg", 
        "calcium": "3.6mg", 
        "iron": "0.1mg", 
        "magnesium": "3mg", 
        "potassium": "17mg", 
        "sodium": "302.1mg", 
        "calories from fat": "0.1"
        }
}
```

Currently Supported websites:
- [AllRecipes](https://allrecipes.com)
- Adding more soon...


## Installation
1. Install scrapy according to [installation guide](https://docs.scrapy.org/en/latest/intro/install.html) using `pip`:
```console
$ pip install Scrapy
```

or using `conda`:
```console
conda install -c conda-forge scrapy
```

2. Run the spider using `scrapy` command.
```console
$ scrapy crawl AllRecipes
```
You can use `-o` arugment to save the outputs as a file:
```console
$ scrapy crawl AllRecipes -o sample.json
```