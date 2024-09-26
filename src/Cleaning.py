#Cleaning the data

import pandas as pd

df = pd.read_csv('processed_data.csv')

df.isnull().sum()

df = df.drop(['weather_1_id','weather_1_main','weather_1_description',
              'weather_1_icon','message','wind_gust'],axis=1)

