# Welcome to the Cocktail Whirlwind Repository 🍾🌪️

## Our Aims
- Creating a database with **cocktail** information 🍷
- Producing a set of insights and predictions based on this databse 📈
  - Creating histograms and a network diagram to link cocktail's together with ingredients 📊

### Potential Extensions 
- Linking multiple APIs 🤖
- Recommender Algorithm 💻
- Linking data on calories to cocktail ingredients 🫀

## The Team 👥
---
- @ajlaw138 - Alistair Law - Geography with Economics, 3rd year 🐧
- @harrytugwell - Harry Tugwell - Politics and Data Science, 1st year 🐬
- @SFan12 - Tessy Fan - Politics and Data Science, 1st year 🐰
- @Charlotte1126 -  Charlotte Hong - Politics and Data Science, 1st year
- @dmir123 - Daniyal Mirza - Economics, 2nd year
---

## Motivation
Cocktails are great; they can be the start of a great night out, or a way to meet someone, or catch up with a friend. This is especially the case in London, 
with a thriving bar scene, amounting to £587 million in the UK in 2019 [^1]. By looking to capture this culture in data, we aim to identify price variations in 
cocktails across London, to help those looking for that perfect cocktail that is within their budget. Matching geo-located data with price data, we can
generate a tool that will help people find the right bar, that has the right cocktail. 

### How our project changed 
Our project was originally motivated by looking to understand trends in cocktail popularity, trying to understand which cocktails were in fashion, and what 
taste profiles were most popular. However, finding data sources proved difficult, and as such, our analysis moved towards analysing price variation instead, 
providing a tool that is aimed more towards consumers than businesses. It could still prove useful to bars, by providing a quick way to check cocktail prices 
in an area, so that they can stay competitive in the market. 


## Data Gathering Process
We used a variety of databases to collate information on cocktails, and bars. 
#### CocktailDB - API


#### Master of Malt - Web Scraping
Master of Malt is a UK distributor of various wines, spirits, and other alcohol and cocktail related ingredients. This website contains much valuable information 
on distributor prices, alcoholic content and volumes. By using BeautifulSoup4, the website can be scraped for this information, as it appears in a regular format. 
Thus, a function can be defined to retrieve important information amounting to a panda data frame.

#### The Alchemist - Web Scraping
Data on cocktail prices was collected by scraping The Alchemist's website. This provided some insight into what price levels are like, closer towards the centre of 
London. This data was cleaned by checking for duplicates, and then removing 'NaN' values, which was present in the price column. This meant some loss of data, due to
some prices being missing from the website, but out of the 78 cocktails collected. 63 were retained. The final piece of data cleaning was simply converting the prices 
to a float. 

#### Google Maps - API
Google maps has estimations of suggested price levels, based on reviews made by visitors. Thus, a price level (on a scale from 1 to 5) is determined, with 1 being the 
cheapest, and 5 being the most expensive. A set location is given, with the API retrieving the Place IDs, bar name, and it's given price level. Using a private API key,
name and price level are saved to a csv, with 18 results of bars in London.

## Explanatory Analysis and Visualisations 


## Conclusions 
### Summary 

### Limitations 

## Sources 
[^1] - https://drinksint.com/news/fullstory.php/aid/8346/UK_cocktail_market_valued_at__A3587m.html (last viewed 10/06/2023)

## Appendix 
