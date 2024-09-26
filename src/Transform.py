import json
import pandas as pd


#reading the data from the extract.py file (weather_data.json)
with open('weather_data.json', 'r')as f:
    weather_information = json.load(f)


#weather_information contains the dict, nested dicts so making the flatten_dict for all the keys as cols
def flatten_dict(d,parent_key='',sep='_'):
  items = []
  for k,v in d.items():
    new_key = f"{parent_key}{sep}{k}" if parent_key else k
    if isinstance(v, dict):
      items.extend(flatten_dict(v, new_key, sep=sep).items())
    elif isinstance(v,list) and v and isinstance(v[0], dict):
      for idx, item in enumerate(v):
        items.extend(flatten_dict(item, f"{new_key}{sep}{idx}", sep=sep).items())
    
    else:
      items.append((new_key, v))
  return dict(items)


# processing the each record of the weather_information
def process_all_weather_data(weather_records):
  processed_data = []
  for data in weather_records:
    flat_data = flatten_dict(data)
    processed_data.append(flat_data)
  return processed_data


processed_data = process_all_weather_data(weather_information)

#transform the data into DataFrame

df = pd.DataFrame(processed_data)

# Assuming processed_data is already prepared and used to create DataFrame
df.to_csv('processed_data.csv', index=False)
