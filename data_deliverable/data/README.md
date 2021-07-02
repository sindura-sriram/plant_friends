# Data Spec
<<<<<<< HEAD
The data in this file is for Plant Friend project. In the data, there are records of yields of multiple kinds of crops from 1981 to 2016, including maize, rice, soybean, and wheat. For maize, rice, wheat, there are three kinds of data, which are yield of the whole year, yield of the major season, and yield of the secondary season. This project is investigating the relationship between global warming and the yield of crops, so that there is data of global average temperature from 1981 to 2016.

## Data Format
### Raw data
For yield of crops, in the raw data, each file includes the yield of each area (based on latitude and longitude) of a specified year (e.g. 1981).

Each line in the file contains one record. Below is an example:
lat=12.75 lon=273.25 var=1.7054316

1. lat - float

   the latitude of the area

2. lon - float

   the longitude of the area

3. var - float

   the average yield of the area (t/ha)

For temperature, in the raw data, the file includes all data.

Each line in the file contains one record. Below is an example:
Year=1981 No_Smoothing=0.32

1. Year - int

   the year of the average temperature

2. No_Smoothing - float

   the average temperature

### Preprocessed data
The data is preprocessed, the global average yield of each crop is calculated, and combined with the global average temperature.

After preprocessing, each line in the file contains one record. Below is an example:
year=1981, maize=5.843444, rice=4.543453, soybean=1.380803, wheat=1.7054316, temp=0.32

1. year - int

   the year

2. maize - float

   the average yield of maize

3. rice - float

   the average yield of rice

4. soybean - float

   the average yield of soybean

5. wheat - float

   the average yield of wheat

6. temp - float

   the average temperature

## Data Relationship
The project is to investigate the relationship between temp and maize, rice, soybean, wheat.

## Additional Data
There is also a temperature data with geography information added to our dataset.

Each line in the temperature csv contains a data point, which looks like:
longitude: 0.25, latitude = -89.75, jan = 1.0, feb = 2.2, mar = 9.0, apr = 11.2, may = 12.5, jun = 15.0, jul = 17.8, aug = 21.4, sep = 16.2, oct = 12.0, nov = 5.2, dec = 3.2, average_temp = 6.0
1. longitude: a number ranging from 0 to 360
2. latitude: a number ranging from -90 to 90
3. jan - dec: a number representing the average temperature during that respective month
4. average_temp: a number representing the average temperature over the year
