# SpotifySongAnalysisProject

## Summary
The goal of this project is to analyze the data available from Spotify to answer questions about Spotify Audio Features by song year, correlation between Audio Features and country metrics, and the Spotify Audio Features by song year. Technologies to be used are Python, Jupyter Notebooks, Pandas, Requests, and Matplotlib. Optionally, the Spotify API can be used but will match the Kaggle Data. For this we used the following data sources:

1. [Spotify Audio Features](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks)
2. [Spotify Charts](https://spotifycharts.com/regional)
3. [World Metrics](https://www.kaggle.com/unsdsn/world-happiness)
4. [2017 Musician Deaths](https://en.wikipedia.org/wiki/List_of_2017_deaths_in_rock_and_roll)

# Questions

## In 2019, do Audio Features of charting songs correlate to a country's Happiness Score?

* Use the Happiness Score from [World Metrics](https://www.kaggle.com/unsdsn/world-happiness), scrape the 2019 weekly data for each region from [Spotify Audio Features](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks), and use the Audio Features from here [Spotify Audio Features](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks).
* Merge the 3 data sets and aggregate each Audio Feature by the appropriate measure of central tendency.
* Show plots with regression lines and give the r value for each Audio Feature by Country Happiness Score.


## In 2019, do Audio Features of charting songs correlate to a country's Freedom to Make Life Choices Score?

* Use the Freedom to Make Life Choices Score from [World Metrics](https://www.kaggle.com/unsdsn/world-happiness), scrape the 2019 weekly data for each region from [Spotify Audio Features](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks), and use the Audio Features from here [Spotify Audio Features](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks).
* Merge the 3 data sets and aggregate each Audio Feature by the appropriate measure of central tendency.
* Show plots with regression lines and give the r value for each Audio Feature by Freedom to Make Life Choices Score.

## In 2019, do Audio Features of charting songs correlate to a country's GDP per Capita?

* Use the GDP per Capita from [World Metrics](https://www.kaggle.com/unsdsn/world-happiness), scrape the 2019 weekly data for each region from [Spotify Audio Features](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks), and use the Audio Features from here [Spotify Audio Features](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks).
* Merge the 3 data sets and aggregate each Audio Feature by the appropriate measure of central tendency.
* Show plots with regression lines and give the r value for each Audio Feature by GDP per Capita.

## How have Audio Features changed over time?

* Use the Audio Features from here [Spotify Audio Features](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks).
* Determine the appropriate measure of central tendency for each Audio Feature and give evidence.
* Show plots displaying the change in each Audio Feature over time.

## In 2017, What is the Impact on Streams of Artists following their Deaths?

* Scrape the 2017 daily charts in the US from [Spotify Audio Features](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks) and use the deaths of these [artists](https://en.wikipedia.org/wiki/List_of_2017_deaths_in_rock_and_roll) to cross reference.
* Narrow the data frame to artists that hit the charts in 2017 and died in 2017.
* Compare the streams before death, on the day of death, and after death using line plots.

# How did we do it? (Spoilers)

## Scraping the data
* The work for this is done in [Daily 2017 US Charts](2017-daily-us-charts.ipynb) and [Weekly 2019 Charts by Region](2019-weekly-regional-charts.ipynb).
* This uses the requests library and Beautiful Soup to grab the html from [Spotify Charts](https://spotifycharts.com/regional) and converts the data into a large csv. We then open the csv as a data frame to analyze.

## How have Audio Features changed over time?

* The analysis for this question is in the [Features Over Time](metrics_over_time.ipynb) notebook.
* @Travis - please write up some findings in this bullet format - maybe a bullet for about 5 of the features

## In 2019, do Audio Features of charting songs correlate to a country's Happiness Score, Freedom to Make Life Choices Score, GDP per Capita?

* The analysis for this question is in the [Audio Features vs Country Metrics](CountryHappinessAnalysis.ipynb) notebook.
* @Connor - please write up some findings in this bullet format - 1 or 2 bullets for each metric  

![Artist Deaths](Resources/Images/FeatureByHappiness.png)

## In 2017, What is the Impact on Streams of Artists following their Deaths?
* The analysis for this question is in the [2017 Artist Deaths](2017DailyUSDF.ipynb) notebook.
* @Adam - please write up some findings in this bullet format - 4 or 5 bullets to summarize the whole Q

![Artist Deaths](Resources/Images/Artist%20Deaths.png)
