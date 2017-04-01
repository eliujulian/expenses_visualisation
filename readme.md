## Summary

The Expenses Visualisation dives into the area how people are spending 
their money for private (consumerism) expenses. It allows a comparison by
various different groups (Age, Sex, Employment, etc.), for all expenses or
some special expenses (Only Food, etc.) and allows a conversion between 
money spend per household and per person (member of a household).

All expenses are monthly. The data is about expenses in Germany in 
the year 2015. The data was collected by the Federal Government. Sex, Age, Income-Braket
etc. all refer to the main income provider in the household.

## Design

The original report about this data (see resources) uses nearly no 
visalisations and the only one they use is a kind of pie chart. I find
these very hard to understand because the pie-pieces move around to much. 
Therefore, I was looking for something with a more fixed position and 
therefore choose bar charts by a choosen order. I want the expenses to 
be comparable at "first glance" and for me this means I need very strong anchors, 
like a fixed point. I also choose to color code the expenses categories to 
bring them into groups that I can intuitively compare. 
 
I did some experiments with an advanced mouseover tooltip, but did not find something
 that I liked.

I want to show the expenses with a visual key and therefore used the format of
a credit card, to compare the "credit-cards" of the different households. Therefore 
I made the card bigger when more money was spend. The are of the card is equivalent to
the relativ amount spend in this group. 

Feedback showed that the size alone is not enough, so I added the total amount for this 
group the the title of the card. Also I added the amount of people living in this
household on average.

## Feedback

After feedback from friends I added the option to switch between expenses for the 
whole household and the expenses per household member (expenses of the whole household 
divided by the count of its members). This shows e. g. that couples with children spend 
more in total but much less for each member. It also showes that households with a 
male main earner spend a lot more, but they spend about the same per household member.

I also added the titles and the total amount an no. of persons directly into the cards
instead of into a legend. Further feedback made me change the subtitle in the cards 
between ### € for # persons and ### @ * # persons, thus making it easy to understand
how the amount is calculated.

Feedback also requested more groups to compare and did not like some others. 
So I removed the "Type" group because it was to convoluted and split it up between 
"Singel, Couple, Other", "Single Household" and "Couple Household". Age was was given to
more groups, one for the younger, one for the older. The youngest group (< 25 years) was removed
completely because the data was to sparse. Some subcategories were removed because the 
amount spend was very low and the information value therefore very low. E. g. nobody was 
interested if households spend 1 or 2 Euros on radios.

## Resources

The data comes from destatis.de, Statistisches Bundesamt Deutschland (Federal German Agency for
Statistical Analysis) and was published in a report.

https://www.destatis.de/DE/Publikationen/Thematisch/EinkommenKonsumLebensbedingungen/EinkommenVerbrauch/EinnahmenAusgabenprivaterHaushalte.html
https://www.destatis.de/DE/Publikationen/Thematisch/EinkommenKonsumLebensbedingungen/EinkommenVerbrauch/EinnahmenAusgabenprivaterHaushalte2150100157004.pdf

The data was collected by monitoring aprox. 8,000 households in Germany in 2015. 

Households with a monthly income of over 18,000 Euros or without a home (homeless people)
were not included in the study.

I did some cleaning of the data by removing some mostly irrelevant categories: From 
the group "Clothes and Shoes" the subgroup "Repairs, Dry-Cleaner, Lendings" was removed. 
"Interior Fittings, Domestic Appliances" : "Fridge, Freezer" was removed. From the 
group "Leisure, Entertainment, Culture" the categories "Radios", 
"Portable Devices", "Other devices" and "Repairs" were removed. "Photo-Equipment, Film-Equipment" removed

I translated the names from german into english. All prices are in Euros. 

Positions that could not be validated by the creators of the study, because 
the standard error would be greater that 20 % were treated a 0.

The data was collected and most transformations done in Excel (csv file), correct 
transformation to json by a python script. The data was then integrated into the 
html file directly. 

Besides this I used the dimple.js dokumentation including some examples. 
