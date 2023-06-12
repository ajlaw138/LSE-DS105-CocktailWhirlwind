# Welcome to the Cocktail Whirlwind Repository 🍾🌪️

## Our Aims 🎯
- [x] Creating a database with **cocktail price** information 🍷
- [x] Visualising how **price** and **cocktail type** are linked 📊

### Potential Extensions 
- Geo-locating bars and cocktail prices 📌
  - Interactive map that filters cocktail of interest, and shows according prices 🌍    

---
## The Team 👥

- @ajlaw138 - Alistair Law - Geography with Economics, 3rd year 🐧
- @harrytugwell - Harry Tugwell - Politics and Data Science, 1st year 🐬
- @SFan12 - Tessy Fan - Politics and Data Science, 1st year 🐰
- @Charlotte1126 -  Charlotte Hong - Politics and Data Science, 1st year
- @dmir123 - Daniyal Mirza - Economics, 2nd year
---

## Motivation 
Cocktails are great; they can be the start of a great night out, or a way to meet someone, or catch up with a friend. This is especially the case in London, 
with a thriving bar scene, amounting to £587 million in the UK in 2019. [^1] By looking to capture this culture in data, we aim to identify price variations in 
cocktails across London, to help those looking for that perfect cocktail that is within their budget. 

The team has decided to include cocktails as an  *'alcoholic spirit (or spirits) mixed together with other ingredients'* as per the Oxford English Dictionary. [^2]
Under this definition, the team decided to include cocktail shots, which although much smaller compared to traditional cocktails, and as such will be cheaper. But 
this would be noticeable, and since bars separate their menus too, this inclusion did not present a problem, and instead presented more depth to the study. Similarly, 
**mocktails** (mock cocktails), which are non-acloholic cocktails, are included too in order to provide more depth to the study, since mocktails are seeing increasing 
popularity in the UK market. [^3] Hence, insights gained through our analysis will be of even more use in an ever-changing market. 

### How our project changed 
Our project was originally motivated by looking to understand trends in cocktail popularity, trying to understand which cocktails were in fashion, and what 
taste profiles were most popular. However, finding data sources proved difficult, and as such, our analysis moved towards analysing price variation instead, 
providing a tool that is aimed more towards consumers than businesses. It could still prove useful to bars, by providing a quick way to check cocktail prices 
in an area, so that they can stay competitive in the market. 

---

## Data Gathering Process
We used a variety of databases to collate information on cocktails and bars, with some forming part of our intial analysis. 

### Inital exploration

#### The CocktailDB - API [^4]
This database provided through this API presented information on over 400 cocktails, including data on ingredients, recipe, measurements, glass type and the drink
type *(cocktail or shot)*. Using an API request, a function which loops through the alphabet is used to call information on each cocktail starting with a given letter,
since the API has request limits *(when using the free version)*. This bypasses the issue, and allows for a complete database. When it comes to cleaning the database, 
after checking for duplicates, of which there was none, there were a few steps that had to be taken. First, the column names were cleaned up, removing the 'str' 
characters at the start of the string. Afterwards, columns were dropped that included unimportant information, such as: 'Tags', 'Video' and 'IBA'. Finally, the 'idDrink'
column is converted into a float. 

#### Master of Malt - Web Scraping [^5]
Master of Malt is a UK distributor of various wines, spirits, and other alcohol and cocktail related ingredients. This website contains much valuable information 
on distributor prices, alcoholic content and volumes. By using BeautifulSoup4, the website can be scraped for this information, as it appears in a regular format. 
Thus, a function can be defined to retrieve important information which loops through different sections of the website amounting to a pandas data frame. The sections scraped
were:
1. Barware
2. Bitters
3. Fuit Purees
4. Glassware
5. Mixers
6. No and low alcohol
7. Pre-bottled cocktails
8. Syrups and cordials
9. Vermouth

As there were multiple websites scraped, with different dataframes being created for each section of the website, these dataframes are merged, concatenating into one larger dataframe.
Only wanted information is scraped, and as such, there is no need for column dropping, with duplicates also being checked. Finally, since the dataframe is setup 
prior to adding data, data types are assigned already and as such, the Master of Malt dataframe is clean.

---

### Final Data Sources 

#### Time Out London [^6]
This website was used to select bars that would have their prices analysed. Ideally, a random selection would be used, in which bar names would be scraped with their 
website links. Assigning a number ID to each bar would then allow for a true random number generator to choose bars at random. However, not all bars display their prices, 
and those that do, may display prices in a format that would be difficult to scrape. As such, the five chosen provide insight into what prices in London are like, with 3 
chain bars and 2 independent bars, one of which is in Central London, and the other in the suburbs. Each bar's website is scraped, as described below.


#### Bar Websites - Web Scraping
Data on cocktail prices was collected by scraping each bar's website. This provided insight into cocktail prices at each bar, and was added to a dataframe.
This data was cleaned by checking for duplicates, and then removing 'NaN' values. The final piece of data cleaning was simply converting the prices to a float. There are 
variations in code for each bar, based on the html tag that is assigned to the price, which differed between websites, with other similarly small variations. However, in 
general, the code for each website was structured in the same manner as described. 

The list of bar websites used are as follows:
| Bar name | Website | Location | 
| -------- | ------- | -------- |
| All Bar One | https://www.allbarone.co.uk/drink#/ | Multiple Locations |
| The Alchemist | https://thealchemist.uk.com/drinks/london-bevis-marks/ | Multiple Locations |
| Dirty Martini |  https://dirtymartini.uk.com/cocktails-food/cocktails/ | Multiple Locations |
| Fire & Ice Lounge | https://kiosx.com/cocktails-and-spirits/ | Uxbridge | 
| BEasy Bar | https://beasybar.co.uk/beasy-drinks-menu | Soho |


## Explanatory Analysis and Visualisations 


## Conclusions 
### Summary 

### Limitations 

## Sources 
[^1]: https://drinksint.com/news/fullstory.php/aid/8346/UK_cocktail_market_valued_at__A3587m.html (last viewed 10/06/2023)
[^2]: https://www.oed.com/viewdictionaryentry/Entry/35499 (under II.3.a.; last viewed 12/06/2023) 
[^3]: https://www.forbes.com/sites/elvaramirez/2019/05/22/make-mine-a-mocktail-why-the-non-alcoholic-drinks-trend-is-here-to-stay/?sh=33f6e9be3eb2 (last viewed 12/06/2023)
[^4]: https://www.thecocktaildb.com/ (last viewed 12/06/2023)
[^5]: 
[^g]:

## Appendix 
