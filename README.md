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
1. For each year aggregate the music metrics over all songs released that year.
2. This will be a line plot
* Travis is converting to data frame for question 1 already


## In 2017 What is the Impact on Streams of Artists following their Deaths?
1. XXXTENTACION dead
2. guy from linkedin park
3. Joos WRLD

* Adam - List of 2017 artists
* Joe - Daily Us for 2017
* total streams in top 200 each day leading up and after death
