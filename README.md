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
- @SFan12 - Tessy Fan - Politics and Data Science, 1st year 🐰
- @Charlotte1126 -  Charlotte Hong - Politics and Data Science, 1st year 🦊
- @harrytugwell - Harry Tugwell - Politics and Data Science, 1st year 🐬
---

## Motivation 
Cocktails are great; they can be the start of a great night out, or a way to meet someone, or catch up with a friend. This is especially the case in London, 
with a thriving bar scene, amounting to £587 million in the UK in 2019. [^1] By looking to capture this culture in data, we aim to identify price variations in 
cocktails across London, to help those looking for that perfect cocktail that is within their budget. 

The team has decided to include cocktails as an  *'alcoholic spirit (or spirits) mixed together with other ingredients'* as per the Oxford English Dictionary. [^2]
Under this definition, the team decided to include cocktail shots, which although much smaller compared to traditional cocktails, and as such will be cheaper. But 
this would be noticeable, and since bars separate their menus too, this inclusion did not present a problem, and instead presented more depth to the study. Similarly, 
**mocktails** (mock cocktails), which are non-alcoholic cocktails, are included too in order to provide more depth to the study, since mocktails are seeing increasing 
popularity in the UK market. [^3] Hence, insights gained through our analysis will be of even more use in an ever-changing market. 

### How our project changed 
Our project was originally motivated by looking to understand trends in cocktail popularity, trying to understand which cocktails were in fashion, and what 
taste profiles were most popular. However, finding data sources proved difficult, and as such, our analysis moved towards analysing price variation instead, 
providing a tool that is aimed more towards consumers than businesses. It could still prove useful to bars, by providing a quick way to check cocktail prices 
in an area, so that they can stay competitive in the market. 

To go into further detail, we specified our focus on certain bars in London. For each of these bars we used various methods to extract and clean data on the price of certain cocktails on their respected menus. From this data, we aimed to highlight overlaps between different cocktails relative to price, concluding with analysis on the popularity of cocktails. Within this particular topic, the term popularity can be loosely defined. Therefore, we decided to focus directly on the price of cocktails. Since ‘price’ represents a large factor within the cocktail sector, we specifically concentrated on ‘price range analysis’. 

The objectives of our price range analysis were to determine specific ranges of cocktail prices in London relative to their respected bars.  Identifying overlaps within popularity demonstrates the popularity of certain cocktails, further calculating averages, minimum and maximum prices allows for us to obtain a broader picture of the pricing landscape. From this, outliers or trends can be highlighted.


---

## Data Gathering Process
We used a variety of databases to collate information on cocktails and bars, with some forming part of our initial analysis. 

### Initial exploration

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
This data was cleaned by checking for duplicates, and then removing 'NaN' values. The final piece of data cleaning was simply converting the prices to a float. Floats are compatible with mathematical operations such as averages and therefore are more useful to use within the process of visualisation as leverage is increased. There are 
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

---

## Explanatory Analysis and Visualisations 

Once all the data on bar prices for cocktails was gathered, this was appended to the `price_data` dataframe. This dataframe was then used to help visualise the cocktail price data for the above mentioned bars in London, containing the ‘name’, ‘composition’, ‘price’ and ‘description’ as headers. 

`price_data` contains an automatically assigned index, non-reflective of any ranking. The ‘Name’ header is a string of the cocktail’s name, with the ‘composition’ header being a list of ingredients. The ‘description’ header, again containing strings, provides a text description of the drink, as one website contained this extra information, with the others not. This column is not used during analysis. The ‘price’ header contains floats, representing prices in Pound Sterling (£). Figure 2 displays an example of the `price_data` dataframe. The dataframe holds 78 rows, with 4 columns. 

Data displayed below is an example, and not necessarily representative of the collected data. 

| | name | composition | price | description |
|-|------|-------------|-----|---------|
| 0 | Old Fashioned | Bourbon, bitters, sugar, syrup | 13 | NaN | 
| 1 | Margarita | Tequila, orange liqueur, lime juice, syrup | 11.5 | A popular sweet drink | 
| 2 | Cosmopolitan | Vodka, orange liqueur, cranberry juice, lime juice | 12.5 | NaN |

*Figure 2 – `price_data` dataframe with example data.*

### Visualisations of price distribution
Using the `plotnine` package, the `price_data` dataframe is used to generate a violin plot, box plot and a density curve. In using these visualisation techniques, the distribution of prices can be easily analysed.

#### Violin plot and density curve
These visualise the distribution curve of cocktail prices, with the large majority of cocktail prices falling in between **£12-14**, with some cocktails clustering below the £11 price line. When comparing to a normal distribution, it can be said that there is positive skew, as there are no cocktails cheaper than £10, and as such, the bottom tail of the curve is higher than expected for a normal distribution

#### Box plot
This plot confirms the observations obtained from the price density curve. The median price is £12.50, lying closer to the upper quartile, confirming the positive skew. The minimum price is £10, and maximum of £16, meaning the range is £6. The prices are not extremely dispersed, nor very dense. No outliers are observed. 

From this analysis, what we can observe is that cocktails are first of all, **quite expensive**. Considering that currently (as of 2023) we live in a time of rising living costs, going out for cocktails is not cheap, with the average cocktail setting you back the equivalent of 3 ‘Meal Deals’ (exact number varies by retailer). [^7] Interestingly, it seems that beyond £14, prices drop off quite sharply, as seen in the density curve graph. This suggests that businesses know consumers are not willing to pay much more than that, and as such, will not set many prices beyond this threshold. 

#### Composition Word Cloud for `price_data`
Using the ‘composition’ header for `price_data`, the most common ingredients in the cocktails served by bars can be seen, appearing larger if occurring more frequently. The most utilised spirits are vodka, rum and liqueur. Seemingly, the most common taste profile is tropical as citrus, lime and pineapple are the most popular. Soda and syrups is a common mixer too. Another noticeable element is ‘fresh’, suggesting that maybe bars should look to use other words to describe their ingredients, as if one is paying over £10 for a drink, the fruit being fresh should be given. 

This word cloud is a simple visualisation of common words appearing in the ‘composition’ header, but by no means is perfect. The data itself does not represent what are the most popular drinks, as the team did not have access to sale data. As such, the results could present inferred popularity, in which the most common cocktails and ingredients being chosen by bars. Of course, bars choose menus as part of a business decision, so that the cocktails served will generate the most revenue for the bars, and so more common recurring cocktails across multiple bars could signify a ‘popular cocktail’. However, this is not conclusive, not proved in this study, and as such, the word cloud is used to just visualise common trends in cocktail composition. 

### Analysing the relationship between price and type
*insert how type was assigned and obtained from* 
This formed a new dataframe, named `type_data`, which had a similar layout to `price_data`, but instead of a ‘description’ column, a ‘type’ column exists. Again, an index was automatically generated, with no meaning to order.  Figure 3 displays an example of the `type_data` dataframe. This dataframe contains 79 rows and 4 columns.

Data displayed below is an example, and not necessarily representative of data collected. 

| | name | composition | price | type |
|-|------|-------------|-----|---------|
| 0 | Old Fashioned | Bourbon, bitters, sugar, syrup | 13 | Classic Cocktail | 
| 1 | Margarita | Tequila, orange liqueur, lime juice, syrup | 11.5 | Modern Cocktail | 
| 2 | Patron Silver | NaN | 4.75 | Tequila’s |

*Figure 3 - `type_data` dataframe with example data.*

A summary statistics table was generated too, displaying the count of each type, the mean price, standard deviation, minimum, maximum and quartile boundaries. Prices are all in Pound Sterling (£). These are displayed in Appendix A.



This provides some indication as to the variations in prices depending on the type of drink purchased. But numbers just by themselves can be boring, so the use of graphs is important to really understand and breakdown this data.

### Visualisation of `type_data`
Using the ggplot package again, a boxplot and bar chart are used to analyse relationships between the type of cocktail, and its price, as well as how the number of ingredients changes too.

#### Boxplot 
A clear segregation can be seen between drinks below £4.25, and those above £8.25. This shows the stark contrast in cost between what are effectively shots, and traditional cocktails. 
With most traditional cocktail types exhibiting just one price, except ‘champagne cocktails’ which has one cheaper outlier and ’modern cocktails’ that has some variation. 2 drinks have a cheaper price of £8.25, whilst the other 7 cost £8.75. From analysing these cocktails, we can see that cocktails themselves are similar price, ranging from £8.25 to £9.25, with just champagne cocktails costing more. 

When comparing the lower tier of prices, interestingly, mocktails cost just £3.50, illustrating the extra cost of alcohol and spirits cause a price increase of around £5. The ‘Shots’ type has a range of £1 between £3-4, with most costing £3. The other types, brandy, liquors, tequila and whiskeys, are spirit shots, and are not the subject of this study, and are simply displayed for comparison purposes. 

#### Text Counter and Bar Chart
In order to use the text counter, the ‘NaN’ values had to be removed. In doing so, this removed the spirit shots, since these only contained the spirit, of which the shot was named. Hence, including these in this analysis made little logical sense, so cleaning the data in this manner effectively solved two issues. A function was defined to count the number of words in the ‘composition’ column within `type_data`. In order to stop double counting of ingredients with 2 words e.g. lime juice, white space is joined together to avoid this from distorting results. The code for the text counter is shown below:
```

def split_count(t):
    text = ' '.join(list(t))
    # Split words by text punctuation divider
    punctTokenizer = tk.WordPunctTokenizer()
    word_list = punctTokenizer.tokenize(text)
    Word_text = list(filter(lambda x:x not in [',','.','!','-',';','?',"'",'&','),',"(",")","’",":"],
                            word_list))

    count_text = len(pd.value_counts(Word_text).tolist())
    return count_text

```
This function is used on the ‘composition’ column, and using a `groupby` to aggregate the data under each cocktail type. Using ggplot, this data is converted into a bar chart.
The bar chart shows that premium cocktails clearly use more ingredients when compared to other cocktail types, with mocktails, champagne cocktails and prosecco cocktails being less complicated. Shots are unsurprisingly the least ingredient intensive. 

As such, shots and mocktails being cheaper, and containing less ingredients have a clear correlation. However, this correlation does not continue as champagne and prosecco cocktails cost similar to premium cocktails (more in the case of champagne cocktails), yet have less ingredients. Thus, the price of champagne and prosecco is what causes these cocktails to cost more, even though they are not as ingredient dense. 

#### Composition word cloud for `type_data`
This word cloud is slightly different when compared to the one for `price_data`. Here, liqueur is the most common spirit, with gin and prosecco being quite prominent specifically white rum is more frequent, with vodka still being popular. Again, citrus flavours occur the most with lime, orange and lemon all occurring frequently, with mint also being somewhat common. Coffee is used more often, opposed to `price_data` where coffee was not used much. There is also less mention of mixers like soda or syrup. Coming up again is the use of ‘fresh’ which clearly shows that bars should use a thesaurus and find a different word to make their menu descriptions more interesting. 

### What are the key trends
- Cocktails in Central London cost more (about £4)
  -	Cocktail rarely exceeded £14 in Central, and £9.25 in the suburbs
-	Cocktail complexity is not necessarily associated with higher cost
-	Mocktails are as cheap as a shot (alcohol is expensive)
-	Citrus flavours are the most commonly used ingredient 
-	Bar menu designers need to find a different word than ‘fresh’

## Conclusions 
### Summary 

### Limitations 

## Appendix A

|type | count | mean | std | min | max |
| -- | --- | --- | --- | --- | ---- |
| Brandy | 1 | 3.25 | NaN | 3.25 | 3.25 |
| Champagne Cocktail | 7 | 10.39 | 0.94 | 8.25 | 10.75 | 
| Gin Cup Cocktail | 6 | 9.25 | 0.00 | 9.25 | 9.25 | 
| Liquors | 9 | 3.22 | 0.15 | 3.00 | 3.50 | 
| Mocktail | 4 | 3.50 | 0.00 | 3.50 | 3.50 | 
| Modern Cocktail | 9 | 8.53 | 0.26 | 8.25 | 8.75 | 
| Premium Cocktail | 5 | 9.25 | 0.00 | 9.25 | 9.25 |
| Prosecco Cocktail | 8 | 9.25 | 0.00 | 9.25 | 9.25 |
| Shots | 6 | 3.33 | 0.52 | 3.00 | 4.00 |
| Tequila | 9 | 3.83 | 0.57 | 3.00 | 4.25 | 
| Whiskey/ Bourbon | 5 | 3.5 | 0.31 | 3.25 | 4.00 | 
| Classic Cocktail | 10 | 8.25 | 0.00 | 8.25 | 8.25|

*`type_data` summary statistics based on each cocktail type (quartile data omitted). Figures rounded to 2 D.P. where applicable.*



[^1]: https://drinksint.com/news/fullstory.php/aid/8346/UK_cocktail_market_valued_at__A3587m.html (last viewed 10/06/2023)
[^2]: https://www.oed.com/viewdictionaryentry/Entry/35499 (under II.3.a.; last viewed 12/06/2023) 
[^3]: https://www.forbes.com/sites/elvaramirez/2019/05/22/make-mine-a-mocktail-why-the-non-alcoholic-drinks-trend-is-here-to-stay/?sh=33f6e9be3eb2 (last viewed 12/06/2023)
[^4]: https://www.thecocktaildb.com/ (last viewed 12/06/2023)
[^5]: https://www.masterofmalt.com/ (last viewed 12/06/2023)
[^6]: https://www.timeout.com/london/search#/?sort=relevance&q=cocktail%20bars&viewstate=list (last viewed 12/06/2023)
[^7]: https://www.bbc.com/news/business-65265234 (last viewed 13/06/2023)


