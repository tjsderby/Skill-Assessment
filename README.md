# Data Engineering test 

We have IoT devices collecting some metrics across the world. We have experienced that a lot of devices are failing lately. We know that the devices are sensible to temperature, so we have downloaded some weather data from the locations of the devices.  

## Part 1. Data manipulation  

We have the list of the position of the devices in a json file like this `devices.json`:  

``` json
{'id': 15126, 'name': 'device-BE-17', 'lat': 35.7721, 'lon': -78.63861} 
{'id': 12526, 'name': 'device-US-11', 'lat': 36.7721, 'lon': -71.1561} 
... 
```

We have another dataset downloaded in json the of the weather data for the last week with hourly granularity for the positions of the devices (https://www.weatherbit.io/api/swaggerui/weather-api-v2#!/Hourly32Historical32Weather32Data/get_history_hourly_lat_lat_lon_lon). As we want you to have up to date data, we provide a python script that downloads the last month of data from the API, see at the end for instructions on how to use it. 

Apart from that, we have csv dataset with extra information about the weather stations that collect the weather. This csv has a column with a metric that contains the measurement reliability of each station. The data look like this:  

```csv
station_id,lat,lon,source,reports,country,measurement_reliability 
0011W82.82,15.16,madis,subhourly,SJ,0.5 
00000,17.03,-42.97,madis,subhourly,GF,0.56 
0001W,30.436,-84.122,madis,subhourly,US,0.93 
0002W,30.538,-84.224,madis,subhourly,US,0.85 
... 
```

We would like to gather all the relevant information in a single table and provide it to the device expert to enable them to find some insight on what the problem with the devices could be. 

Summarize the results to have daily granularity, use average to aggregate the measurements. This table would have the following schema:

```csv
device_id, device_name, lat, lon, date, avg_temp, meassurement_reliability_score
```

Take into consideration that each weather measurement can come from multiple stations (`source` field). When a measurement comes from multiple stations, use the (Harmonic mean)[https://en.wikipedia.org/wiki/Harmonic_mean].

We would normally use pandas, spark or pyspark to solve this task, but you can use any programing language or technology to complete it. Take into consideration that in a future iteration we might need to add more meassurements to the result table.

## Part 2. Retrieve data to enhance dataset  

We also know that the quality of the air can affect the measurement of our IoT devices. We have found an API that has the quality of the air for the last days.  

https://www.weatherbit.io/api/swaggerui/weather-api-v2#!/Historical32Air32Quality/get_history_airquality_lat_lat_lon_lon 

We would like to programmatically retrieve the data, so we can repeat this process every 3 days, to enhance the previous dataset with some measurement of the Air quality for the days that both datasets overlaps. 

Make a program/script to retrieve the data in the language that you want. 

Join this information to the previous data set to have the enhanced summarized table with pm10 and pm25. Use average to aggregate measurements if needed. The resulting table would have the columns:


```csv
device_id, device_name, lat, lon, date, avg_temp, meassurement_reliability_score, pm10, pm25
```
 

## Part 3. Upload the result to the cloud (Optional) 

We want to store the summarized table in the cloud so the expert of the organization can have a look at the data to provide some insight of the results. 

We have a storage account in Azure, we would like to upload the summarized result in the container stage2-de-test  

The connection string for the storage account is:  

DefaultEndpointsProtocol=https;AccountName=destage2test;AccountKey=DBoiqbP2ABNVM0OrpRwhfSB/RuNFwIA99DBjPrnxYj6XdVpEYjrfBk/e0sh4CfeEa4P/1CpI+w4NOzHxGE1d1w==;EndpointSuffix=core.windows.net 

Please look at the Microsoft documentation on storage account and upload the summarized result in a folder with your name within the given container. 

https://docs.microsoft.com/azure/storage/blobs/?toc=/azure/storage/blobs/toc.json 


## How to download updated weather data

The python script we provide in scripts will download 30 days of data. This is necessary for Part 2 to work as expected. You will need python to execute it.

To install the dependencies needed, just execute:

```
pip install -r requirements.txt
```

Then execute the script at from the same level of the `script` folder:

```
python script/download_weather.py
```