'''Questo script permette di prelevare dati dal sito 
    https://www.basketball-reference.com/
    I dati che vogliamo prelevare sono le medie 
    statistiche e le statistiche avanzate di ciascun giocatore sia per 
    la regular season sia per i playoff 
    per le stagioni dal 2008-2009 al 2023-2024. 
    Per fare cio' si utilizza la libreria python 
    'basketball_reference_scraper' nello specifico
    la function del package 'teams' 
    'teams.get_roster_stats(teams_name, season, stats, playoff)' che restituisce
    per il team indicato, le medie statistiche di ogni giocatore a roster.
    Alla fine otterremo un DataFrame della forma:

    (per le statistiche per game o per minuto)
    +---------------+-----+----+----+------+------+------+------+-----+------+------+-----+-----+------+------+-----+-----+------+-----+-----+-----+-----+-----+-----+-----+-----+------+
    |    PLAYER     | AGE | G  | GS |  MP  |  FG  | FGA  | FG%  | 3P  | 3PA  | 3P%  | 2P  | 2PA | 2P%  | eFG% | FT  | FTA | FT%  | ORB | DRB | TRB | AST | STL | BLK | TOV | PF  | PTS  |
    +---------------+-----+----+----+------+------+------+------+-----+------+------+-----+-----+------+------+-----+-----+------+-----+-----+-----+-----+-----+-----+-----+-----+------+
    | Stephen Curry |  27 | 79 | 79 | 34.2 | 10.2 | 20.2 | .504 | 5.1 | 11.2 | .454 | 5.1 | 9.0 | .566 | .630 | 4.6 | 5.1 | .908 | 0.9 | 4.6 | 5.4 | 6.7 | 2.1 | 0.2 | 3.3 | 2.0 | 30.1 |
    +---------------+-----+----+----+------+------+------+------+-----+------+------+-----+-----+------+------+-----+-----+------+-----+-----+-----+-----+-----+-----+-----+-----+------+

    (per le statistiche avanzate)
    +---------------+------+----+-----+------+-------+-------+-------+------+------+------+------+------+------+------+------+-----+-----+-----+-------+------+------+-----+------+
    |    PLAYER     |  AGE | G  | MP  | PER  |  TS%  | 3PAr  |  FTr  | ORB% | DRB% | TRB% | AST% | STL% | BLK% | TOV% | USG% | OWS | DWS | WS  | WS/48 | OBPM | DBPM | BPM | VORP |
    +---------------+------+----+-----+------+-------+-------+-------+------+------+------+------+------+------+------+------+-----+-----+-----+-------+------+------+-----+------+
    | Stephen Curry |   24 | 12 | 497 | 20.5 | 0.558 | 0.451 | 0.162 |  1.2 |  8.8 |  5.2 | 33.3 |  2.1 |  0.3 | 13.7 | 26.2 | 1.3 | 0.3 | 1.7 | 0.161 |  4.5 |  0.2 | 4.7 |  0.8 |
    +---------------+------+----+-----+------+-------+-------+-------+------+------+------+------+------+------+------+------+-----+-----+-----+-------+------+------+-----+------+
    
    A cui aggiungiamo gia' ora una colonna per il nome del team 'TEAM'
    e una colonna per indicare la season 'SEASON'.
    Per le season si usa la convenzione di indicare la season con l'anno in cui termina,
    quindi per la stagione 2008-2009 si usa il numero 2009.
    Questo processo di aggiungere le colonne, che va a rientrare nel processo di DataCleaning
    viene svolto gia' in fase di Scraping perche' successivamente sarebbe infattibile.
'''

import pandas as pd
import time
import numpy as np
import basketball_reference_scraper.teams as teams
import basketball_reference_scraper.players as players
import basketball_reference_scraper.seasons as season
from SQLManager import insert_data
import utilities as utl

def get_roster_stats_season(team_name, season, stats, table1, table2):
    while True:
        try:
            df = teams.get_roster_stats(team_name, season, stats)
            if(stats == 'ADVANCED'):
                df = df.drop(df.columns[16], axis=1)
                df = df.drop(df.columns[20], axis=1)
            df['TEAM'] = team_name
            df['SEASON'] = season
            df['TEAM'] = df['TEAM'].replace(utl.teams_dict_fullname_inverted)
            insert_data(df, table1)
            print("Inseriti i dati della regular season:",team_name, season)
            if utl.team_made_playoffs(team_name, season):
                df = teams.get_roster_stats(team_name, season, stats, True)
                if(stats == 'ADVANCED'):
                    df = df.drop(df.columns[16], axis=1)
                    df = df.drop(df.columns[20], axis=1)
                df['TEAM'] = team_name
                df['SEASON'] = season
                df['TEAM'] = df['TEAM'].replace(utl.teams_dict_fullname_inverted)
                insert_data(df, table2)
                print("Inseriti i dati dei playoff:",team_name, season)
            break  # Break the loop if the request succeeds
        except ConnectionError as e:
            print("Error obtaining data table for ", team_name, " season: ", season, ":", e)
            print("Retrying request in 5 seconds...")
            time.sleep(5)
            
def load_roster_stats(stats, table1, table2):
    for season in utl.seasons:
        if(season < 2013):
            for team in utl.nba_teams_from_2008:
                get_roster_stats_season(team, season, stats, table1, table2)
        if(season == 2013):
            for team in utl.nba_teams_2012_2013:
                get_roster_stats_season(team, season, stats, table1, table2)
        if(season == 2014):
            for team in utl.nba_teams_2013_2014:
                get_roster_stats_season(team, season, stats, table1, table2)
        if(season > 2014):
            for team in utl.nba_teams_2014_today:
                get_roster_stats_season(team, season, stats, table1, table2)
                
                
#load_roster_stats('PER_GAME', 'player_rs_stats_pergame', 'player_po_stats_pergame')
#load_roster_stats('PER_MINUTE', 'player_rs_stats_perminute', 'player_po_stats_perminute')
#load_roster_stats('ADVANCED', 'player_rs_stats_advanced', 'player_po_stats_advanced')