import pandas as pd
import time
import numpy as np
import basketball_reference_scraper.teams as teams
from SQLManager import insert_data
import utilities as utl

def get_team_roster(team_name, season):
    while True:
        try:
            df = teams.get_roster(team_name, season)
            df['TEAM'] = team_name
            df['TEAM'] = df['TEAM'].replace(utl.teams_dict_fullname_inverted)
            df['SEASON'] = season
            insert_data(df, 'team_roster')
            break
        except ConnectionError as e:
            print("Error obtaining data table for ",
                  team_name,
                  " season: ",
                  season,
                  ":",
                  e)
            print("Retrying request in 5 seconds...")
            time.sleep(5)

def get_team_roster_seasons():
    for season in utl.seasons:
        if(season < 2013):
            for team in utl.nba_teams_from_2008:
                get_team_roster(team, season)
        if(season == 2013):
            for team in utl.nba_teams_2012_2013:
                get_team_roster(team, season)
        if(season == 2014):
            for team in utl.nba_teams_2013_2014:
                get_team_roster(team, season)
        if(season > 2014):
            for team in utl.nba_teams_2014_today:
                get_team_roster(team, season)
                
get_team_roster_seasons()