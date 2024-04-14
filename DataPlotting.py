import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import sqlite3 as sql

conn = sql.connect('database/nbadata.db')

df = pd.read_sql("SELECT SEASON, PTS FROM player_stats WHERE Player = \"Stephen Curry\"", conn)
print(df)
df.plot(kind = 'scatter', x = 'SEASON', y = 'PTS')
plt.show()