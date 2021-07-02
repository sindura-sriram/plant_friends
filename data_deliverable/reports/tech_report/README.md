# Tech Report

## Data Source ##
The data of yield of crops is from Iizumi, Toshichika (2019): Global dataset of historical yields v1.2 and v1.3 aligned version. PANGAEA, https://doi.org/10.1594/PANGAEA.909132. The data of global average temperature is from NASA, https://climate.nasa.gov/vital-signs/global-temperature/.  We have collected data organized by longitude and latitude from U-Delaware for temperature.

We collected our data from database by downloading them, and did preprocessing on them to make up a new data file, which is helpful for us to investigate in the relationship between global warming and the yield of crops.

Both data sources are reputable. PANGAEA is a professional data publisher for earth and environment science. NASA is The National Aeronautics and Space Administration.

We transform nc4 file to csv file, and calculate the global average yield of each crop. Then, we combine the calculated data with the temperature of that year into the new data file. Lastly, we have first 10 data point in the sample. It is comparably small (around 29%). It is not obvious in the trend, because it only represents a decade of data.

When collecting our data, we considered that the data needed to be continuous in time, so that we can analyze the relationship and find out the trend. The data of yield of crops and the data of temperature need to be compatible in time and location.

## Data Cleaning ##
There are totally 37,324,800 in the raw data. After processing, there are 36 records of data for each year globally. We only have one group of data to care about, so that all of the data is in this group. It is enough to perform our analysis later on, because 36 years is a very long period of time, and the climate change in these 36 years is huge, for example, the average temperature is above 0.8 degree celsius from 1981 to 2016 while the one is above 0.39 degree celsius from 1881 to 1981.

There is no missing values. Our data is complete for us to do analysis.

There is no duplicate, because our data is collected for each year. In this case, the data of each year is unique.

The yield of crops has an increasing trend along the timeline, while the temperature also has an increasing trend along the timeline. There is no obvious outlier, so that the data can be interpreted by a linear regression. The min value of global average temperature is 0.14, and the max value is 1.02.

There is no data type issues. Because all the data we are working on is either int or float.

We will not throw any data away. All of our data is usable and significant to our analysis later on.

## Challenge and Future ##
### Challenge in gathering weather data: ###
Gathering data from that website is not a trivial task. Because the website is displayed as an interactive global map, and the only way to get data of a single weather station is to manually click on the map. Based on that, we have to spend a lot of time on manually collecting data, or we have to build a complex crawler to deal with the logic. Because of those difficulties, we had to find a workaround for collecting weather data. We would like to find weather data for a larger scale, instead of data from each weather station, so we wouldn’t need to manually group them. Although we can also order dataset by submit an inquiry, the amount of data we might need is exceeded the max size of data available through an inquiry. Therefore, getting data from the NCDC website probably won’t work before the deadline of data deliverable.

### Next Step: ###

In the following time, we will finish the preprocessing of our data. We will also consider about adding more specific data like the yield of crops in the USA, and the average temperature of the USA. Our data collection make us be able to do hypothesis testing with the hypothesis, 'global warming decrease the yield of crops'. We can also do a prediction of the yield of crops in the future with the temperature continuing increasing.
