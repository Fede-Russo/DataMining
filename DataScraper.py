import pandas as pd
import time
import numpy as np
import basketball_reference_scraper.teams as teams
import basketball_reference_scraper.players as players
import basketball_reference_scraper.box_scores as boxScore
import basketball_reference_scraper.injury_report as injury
from SQLManager import insertPlayerStats, insertPlayerGameLog

#seasons = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
seasons = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

nba_teams_2014_today = [
    "ATL", "BOS", "BRK", "CHO", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", 
    "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOP", "NYK", 
    "OKC", "ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"
]
nba_teams_2013_2014 = ["ATL", "BOS", "BRK", "CHA", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", 
    "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOP", "NYK", 
    "OKC", "ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"]

nba_teams_2012_2013 = ["ATL", "BOS", "BRK", "CHA", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", 
    "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOH", "NYK", 
    "OKC", "ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"]

nba_teams_from_2008 = [
    "ATL", "BOS", "NJN", "CHA", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", 
    "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOH", "NYK", 
    "OKC", "ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"
]


#gsw = teams.get_roster('GSW', season)

def get_player_logs(player_name, season):
    df = players.get_game_logs(player_name, season)
    df['Player'] = player_name
    insertPlayerGameLog(df)

def get_player_stats(player_name):
    df = players.get_stats(player_name)
    df['Player'] = player_name
    insertPlayerStats(df)

def get_roster_stats_season(team_name, season):
    while True:
        try:
            time.sleep(0.1)
            df = teams.get_roster_stats(team_name, season)
            df['Team'] = team_name
            df['Season'] = season
            insertPlayerStats(df)
            break  # Break the loop if the request succeeds
        except ConnectionError as e:
            print("Error obtaining data table for ", team_name, " season: ", season, ":", e)
            print("Retrying request in 5 seconds...")
            time.sleep(5)
            
def load_roster_stats():
    for season in seasons:
        if(season < 2013):
            for team in nba_teams_from_2008:
                get_roster_stats_season(team, season)
        if(season == 2013):
            for team in nba_teams_2012_2013:
                get_roster_stats_season(team, season)
        if(season == 2014):
            for team in nba_teams_2013_2014:
                get_roster_stats_season(team, season)
        if(season > 2014):
            for team in nba_teams_2014_today:
                get_roster_stats_season(team, season)

load_roster_stats()

    