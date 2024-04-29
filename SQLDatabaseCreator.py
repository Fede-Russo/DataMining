'''File usato per creare il database e le tabelle per conservare i raw data
	ottenuti tramite scraping
'''


import sqlite3 as sql

conn = sql.Connection("database/nbadata.db")

cursor = conn.cursor()

sql_create_player_rs_stats_pergame_table = ("""CREATE TABLE "player_rs_stats_pergame" (
	"PLAYER"	VARCHAR(255),
	"AGE"	INTEGER,
	"G"	    INT,
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
	"TEAM"	VARCHAR(255),
	"SEASON"	INTEGER
);""")

sql_create_player_po_stats_perminute_table = (""" CREATE TABLE "player_po_stats_perminute" (
	"PLAYER"	VARCHAR(255),
	"AGE"	INTEGER,
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
	"TEAM"	VARCHAR(255),
	"SEASON"	INTEGER
);""")

sql_create_player_po_stats_pergame_table = ("""CREATE TABLE "player_po_stats_pergame" (
	"PLAYER"	VARCHAR(255),
	"AGE"	INTEGER,
	"G"	    INT,
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
	"TEAM"	VARCHAR(255),
	"SEASON"	INTEGER
);""")

sql_create_player_rs_stats_perminute_table = ("""CREATE TABLE "player_rs_stats_perminute" (
	"PLAYER"	VARCHAR(255),
	"AGE"	INTEGER,
	"G"	    INT,
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
	"TEAM"	VARCHAR(255),
	"SEASON"	INTEGER
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

sql_create_player_rs_stats_advanced_table = ("""CREATE TABLE player_rs_stats_advanced (
    PLAYER VARCHAR(255),
    AGE INT,
    G INT,
    MP INT,
    PER FLOAT,
    "TS%" FLOAT,
    "3PAr" FLOAT,
    FTr FLOAT,
    "ORB%" FLOAT,
    "DRB%" FLOAT,
    "TRB%" FLOAT,
    "AST%" FLOAT,
    "STL%" FLOAT,
    "BLK%" FLOAT,
    "TOV%" FLOAT,
    "USG%" FLOAT,
    OWS FLOAT,
    DWS FLOAT,
    WS FLOAT,
    "WS/48" FLOAT,
    OBPM FLOAT,
    DBPM FLOAT,
    BPM FLOAT,
    VORP FLOAT,
    TEAM VARCHAR(255),
    SEASON INT
);""")

sql_create_player_po_stats_advanced_table = ("""CREATE TABLE player_po_stats_advanced (
    PLAYER VARCHAR(255),
    AGE INT,
    G INT,
    MP INT,
    PER FLOAT,
    "TS%" FLOAT,
    "3PAr" FLOAT,
    FTr FLOAT,
    "ORB%" FLOAT,
    "DRB%" FLOAT,
    "TRB%" FLOAT,
    "AST%" FLOAT,
    "STL%" FLOAT,
    "BLK%" FLOAT,
    "TOV%" FLOAT,
    "USG%" FLOAT,
    OWS FLOAT,
    DWS FLOAT,
    WS FLOAT,
    "WS/48" FLOAT,
    OBPM FLOAT,
    DBPM FLOAT,
    BPM FLOAT,
    VORP FLOAT,
    TEAM VARCHAR(255),
    SEASON INT
);""")

sql_create_game_table = ("""CREATE TABLE "played_games" (
	"Date"	DATE,
	"Visitor"	VARCHAR(255),
	"Visitor_pts"	INTEGER,
	"Home"	VARCHAR(255),
	"Home_pts"	INTEGER,
	PRIMARY KEY("Date", "Visitor", "Home")
);""")

sql_create_injury_report = ("""CREATE TABLE "injury_report" (
	"Date"	DATE,
	"Team"	VARCHAR(255),
	"Acquired"	VARCHAR(255),
	"Relinquished"	VARCHAR(255),
	"Notes"	TEXT,
	"InjuryID"	INTEGER NOT NULL,
	PRIMARY KEY("InjuryID" AUTOINCREMENT)
);""")

#cursor.execute("DROP TABLE player_rs_stats_advanced;")
#cursor.execute(sql_create_player_rs_stats_perminute_table)
#cursor.execute(sql_create_player_po_stats_perminute_table)
cursor.execute(sql_create_player_rs_stats_advanced_table)
cursor.execute(sql_create_player_po_stats_advanced_table)
#cursor.execute("DROP TABLE player_rs_stats_pergame;")
#cursor.execute(sql_create_player_rs_stats_pergame_table)
#cursor.execute("DELETE FROM player_rs_stats_pergame;")
#cursor.execute("DROP TABLE player_po_stats_pergame;")
#cursor.execute(sql_create_player_po_stats_pergame_table)
#cursor.execute("DELETE FROM player_po_stats_pergame;")
#cursor.execute("DROP TABLE injury_report;")
#cursor.execute(sql_create_injury_report)
#cursor.execute("DELETE FROM injury_report;")

# Commit the transaction to save the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()