import sqlite3 as sql
import pandas as pd
import numpy as np

conn = sql.connect('database/nbadata.db')

def insert_data(data, table):
    try:
        data.to_sql(table, conn, if_exists='append', index=False)
        conn.commit()
        print("Data inserted successfully in ", table)
    except Exception as e:
        print("Error:", e)

def insert_player_stats(data):
    try:
        data.to_sql('player_stats', conn, if_exists='append', index=False)
        conn.commit()
        print("Data inserted successfully")
    except Exception as e:
        print("Error:", e)

def insert_player_gameLog(data):
    try:
        data.to_sql('game_logs', conn, if_exists='append', index=False)
        conn.commit()
        print("Data inserted successfully")
    except Exception as e:
        print("Error:", e)

def insert_injury_report(data):
    try:
        data.to_sql('injury_report', conn, if_exists='append', index=False)
        conn.commit()
        print("Data inserted successfully")
    except Exception as e:
        print("Error:", e)

def insert_team_games(data):
    try:
        data.to_sql('played_games', conn, if_exists='append', index=False)
        conn.commit()
        print("Data inserted successfully")
    except Exception as e:
        print("Error:", e)