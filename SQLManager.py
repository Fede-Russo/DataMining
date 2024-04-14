import sqlite3 as sql
import pandas as pd
import numpy as np

conn = sql.connect('database/nbadata.db')

def insertPlayerStats(data):
    try:
        data.to_sql('player_stats', conn, if_exists='append', index=False)
        conn.commit()
        print("Data inserted successfully")
    except Exception as e:
        print("Error:", e)

def insertPlayerGameLog(data):
    try:
        data.to_sql('game_logs', conn, if_exists='append', index=False)
        conn.commit()
        print("Data inserted successfully")
    except Exception as e:
        print("Error:", e)

