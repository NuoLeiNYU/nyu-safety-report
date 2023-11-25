# %%
import os

folder_path = './data'

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Loop through the files and delete each one
for file in files:
    file_path = os.path.join(folder_path, file)
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted: {file_path}")
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")

# %%
import pandas as pd
daily_crime_url = 'https://www.nyu.edu/life/safety-health-wellness/campus-safety/crime-log.html'
tables = pd.read_html(daily_crime_url) 
tables[0].to_csv("./data/current_month_crime.csv", index = False)

# %%
from datetime import datetime, timedelta
base_url = 'https://www.nyu.edu/life/safety-health-wellness/campus-safety/crime-log/annual-detail/'
current_date = datetime.now()
past_crime_url_list = []
for i in range(1, 13):
    target_date = current_date - timedelta(days=i * 30)
    formatted_date = target_date.strftime('%B-%Y').lower()
    url = f'{base_url}{formatted_date}.html'
    past_crime_url_list.append((formatted_date, url))

# %%
past_data_list = []
for date, past_crime_url in past_crime_url_list:
    tables = pd.read_html(past_crime_url) 
    past_data_list.append(tables[0])

past_data = pd.concat(past_data_list)
past_data.to_csv('./data/past_year_crime.csv'.format(date), index = False)


