import sqlite3 as sql

conn = sql.Connection("database/nbadata.db")

cursor = conn.cursor()

sql_create_playerStatsTable = ("""CREATE TABLE "player_stats" (
	"Player"	VARCHAR(255),
	"POS"	VARCHAR(10),
	"AGE"	FLOAT,
	"G"	INT,
	"GS"	INT,
	"MP"	FLOAT,
	"FG"	FLOAT,
	"FGA"	FLOAT,
	"FG%"	FLOAT,
	"3P"	FLOAT,
	"3PA"	FLOAT,
	"3P%"	FLOAT,
	"2P"	FLOAT,
	"2PA"	FLOAT,
	"2P%"	FLOAT,
	"eFG%"	FLOAT,
	"FT"	FLOAT,
	"FTA"	FLOAT,
	"FT%"	FLOAT,
	"ORB"	FLOAT,
	"DRB"	FLOAT,
	"TRB"	FLOAT,
	"AST"	FLOAT,
	"STL"	FLOAT,
	"BLK"	FLOAT,
	"TOV"	FLOAT,
	"PF"	FLOAT,
	"PTS"	FLOAT,
	"TEAM"	VARCHAR(10),
	"SEASON"	VARCHAR(10),
	PRIMARY KEY("Player","SEASON","TEAM")
);""")

sql_create_playerGameLog = ("""CREATE TABLE "game_logs" (
	"Player"	VARCHAR(64),
	"Date"	DATE,
	"Age"	REAL,
	"Team"	VARCHAR(10),
	"Home/Away"	VARCHAR(10),
	"Opponent"	VARCHAR(10),
	"Result"	VARCHAR(10),
	"Gs"	INT,
	"MP"	INT,
	"FG"	INT,
	"FGA"	INT,
	"FG%"	FLOAT,
	"3P"	INT,
	"3PA"	INT,
	"3P%"	FLOAT,
	"FT"	INT,
	"FTA"	INT,
	"FT%"	FLOAT,
	"ORB"	INT,
	"DRB"	INT,
	"TRB"	INT,
	"AST"	INT,
	"STL"	INT,
	"BLK"	INT,
	"TOV"	INT,
	"PF"	INT,
	"PTS"	INT,
	"GAME_SCORE"	INTEGER,
	"+/-"	INT,
	PRIMARY KEY("Player","Date","Team")
);""")

cursor.execute(sql_create_playerStatsTable)
cursor.execute(sql_create_playerGameLog)

# Commit the transaction to save the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()