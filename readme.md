## Summary

The Expenses Visualisation dives into the area how people are spending 
their money for private (consumerism) expenses. It allows a comparison by
various different groups (Age, Sex, Employment, etc.), for all expenses or
some special expenses (Only Food, etc.) and allows a conversion between 
money spend per household and per person (member of a household).

All expenses are monthly. The data is about expenses in Germany in 
the year 2015. The data was collected by the Federal Government. Sex, Age, Income-Braket
etc. all refer to the main income provider in the household.

The visualisation explains how some expenses are related to the people living in 
the household, or to be more precise, mostly the main income provider. 

One thing to notice is, while bigger households spend more in total, they spend 
less per person (eg. 1,531 € per person in a single household, 778 € per person 
in household of 5 people and up). This brings the spending per person of large 
households very near te the spending per person in a household with a jobless main
income earner (726 € per person). Large households are usually families that have
many kids. These have apparently often only the financial means of a jobless living
of wellfare.

Another thing is the spending compared by income bracket of the main income earner. Richer 
households spend about the same on some expenses (per person): food, living, communication.
Other expenses differ widely. I would have expected a bigger spread in the living cost but
richer household seem to not spend the extra money on bigger or more expensive apartments.
The food does not include dining out and is probably therefore more or less the same. The
richer households spend a lot more on eating out.

While it looks like men spend a lot more than women (1,892 € for household where 
a woman is the main income earner, 2,755 € for household where the men is the main
income earner), the spending per person is roughly the same with a bit more spending in 
households where a woman is the main income earner. 

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

First Feedback: "I like the different groups of households and to see how they
 differ in their spending. But to compare them I would like to know how much they 
 spend for each one living in the household. Groceries for 2 people are not the same
 like for 4 people. Also if I could know more about the people living in the household
 I would be interested in that."

After this feedback I added the option to switch between expenses for the 
whole household and the expenses per household member (expenses of the whole household 
divided by the count of its members). This shows e. g. that couples with children spend 
more in total but much less for each member. It also showes that households with a 
male main earner spend a lot more, but they spend about the same per household member.
Data on the particular members of a household was not available in this study.

Second Feedback: "I think the credit card design shows very good the proportional 
size of the budget of the household, but I would like to know how big the budget
 actually is. I would have to add the bar all togher what is very difficult."

After this feedback I added the titles and the total amount an no. of persons 
directly into the cards instead of into a legend. Further feedback made me 
change the subtitle in the cards  between ### € for # persons and ### @ * # persons, 
thus making it easy to understand how the amount is calculated.

Third Feedback: "The visualisation looks sometimes very cluttered when there are more 
than four of five charts on the page. They just all become very small and they are very
hard to compare."

I removed the "Type" group because it was to convoluted and split it up between 
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
