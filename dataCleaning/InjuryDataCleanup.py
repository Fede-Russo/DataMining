import pandas as pd
import numpy as np
import sqlite3 as sql

conn_raw = sql.connect('database/nbadata.db')
conn_clean = sql.connect('database/nbadata_clean.db')
        
def get_injury_report_raw_data():
    try:
        data = pd.read_sql('SELECT * FROM injury_report', conn_raw)
        print("Data read successfully")
        return data
    except Exception as e:
        print("Error:", e)

def get_player_stats_raw_data():
    try:
        data = pd.read_sql('SELECT * FROM player_stats', conn_raw)
        print("Data read successfully")
        return data
    except Exception as e:
        print("Error:", e)
        
def insert_clean_report_data(data):
    try:
        data.to_sql('injury_report', conn_clean, if_exists='append', index=False)
        conn_clean.commit()
        print("Data inserted successfully")
    except Exception as e:
        print("Error:", e)
        
#------Get Injury Raw Data From DB-----

raw_data = get_injury_report_raw_data()

#------Clean DataFrame Structure------

raw_data = raw_data.drop(columns = ['InjuryID'])
raw_data['Date'] = pd.to_datetime(raw_data['Date'])  # Convert 'Date' column to datetime type

#------Clean Team Name-------

#change team name for special cases:    
#   - CHARLOTTE: CHA from 2008 to 2013, CHO from 2014
#   - NETS: NJN from 2008 to 2012, BRK from 2013
#   - PELICANS: NOH form 2008 to 2013, NOP from 2014
raw_data.loc[((raw_data['Team'] == 'CHO') & (raw_data['Date'] < pd.to_datetime('2014-06-18'))), 'Team'] = 'CHA'
raw_data.loc[((raw_data['Team'] == 'BRK') & (raw_data['Date'] < pd.to_datetime('2013-06-18'))), 'Team'] = 'NJN'
raw_data.loc[((raw_data['Team'] == 'NOP') & (raw_data['Date'] < pd.to_datetime('2014-06-18'))), 'Team'] = 'NOH'

#------Clean Player Name------

#Drop rows where both Acquired and Relinquished columns are empty
no_player_data = raw_data.loc[((raw_data['Acquired'].isnull()) & (raw_data['Relinquished'].isnull()))]
raw_data.drop(no_player_data.index, inplace = True)

#Separate out player names (some players have multiple names, each separated by a "/")
all_injury_names = raw_data['Acquired'].fillna('') + raw_data['Relinquished'].fillna('')

player_injury_name_df = all_injury_names.str.split(pat = '/', expand = True)
player_injury_name_df.columns = ['Player', 'Alt_name_1', 'Alt_name_2'] 

#Remove any strings in parentheses in player names (removes parentheses and the string within the parentheses)
player_injury_name_df.replace(regex = ['\(.*?\)'], value = '', inplace = True)

#Remove suffixes on player names
player_injury_name_df.replace(regex = ['Jr\.'], value = '', inplace = True)
player_injury_name_df.replace(regex = ['III'], value = '', inplace = True)
player_injury_name_df.replace(regex = ['IV'], value = '', inplace = True)

#Remove periods in player names
player_injury_name_df['Player'].replace('\.', '', regex=True, inplace = True)
player_injury_name_df['Alt_name_1'].replace('\.', '', regex=True, inplace = True)
player_injury_name_df['Alt_name_2'].replace('\.', '', regex=True, inplace = True)

#Remove extra white spaces at the start or end of player names
player_injury_name_df['Player']= player_injury_name_df['Player'].str.strip()
player_injury_name_df['Alt_name_1']= player_injury_name_df['Alt_name_1'].str.strip()
player_injury_name_df['Alt_name_2']= player_injury_name_df['Alt_name_2'].str.strip()

player_stats = get_player_stats_raw_data()
player_stats_name_df = player_stats['Player']
unique_player_stats_name = player_stats_name_df.unique()
unique_injury_name = player_injury_name_df.stack().unique()

name_mapping = {}

for name_in_injury in unique_injury_name:
    # Find the corresponding name in the player stats dataframe
    corresponding_name_in_stats = np.where(unique_player_stats_name == name_in_injury)[0]
    if corresponding_name_in_stats:
        name_mapping[name_in_injury] = unique_player_stats_name[corresponding_name_in_stats[0]]
        
raw_data[['Player', 'Alt_name_1', 'Alt_name_2']] = player_injury_name_df
raw_data['Player'] = raw_data['Player'].replace(name_mapping)
raw_data = raw_data.drop(columns = 'Alt_name_1')
raw_data = raw_data.drop(columns = 'Alt_name_2')
print(raw_data)

insert_clean_report_data(raw_data)
