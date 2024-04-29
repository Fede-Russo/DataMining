from datetime import datetime

seasons = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]

nba_teams_2014_today = [
                        "ATL", "BOS", "BRK", "CHO", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", 
                        "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOP", "NYK", 
                        "OKC", "ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"
]
nba_teams_2013_2014 = [
                    "ATL", "BOS", "BRK", "CHA", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", 
                    "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOP", "NYK", 
                    "OKC", "ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"]

nba_teams_2012_2013 = [
                    "ATL", "BOS", "BRK", "CHA", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", 
                    "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOH", "NYK", 
                    "OKC", "ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"]

nba_teams_from_2008 = [
                    "ATL", "BOS", "NJN", "CHA", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", 
                    "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOH", "NYK", 
                    "OKC", "ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"
]

teams_dict_fullName = {
    "ATLANTA HAWKS": "ATL",
    "ST. LOUIS HAWKS": "SLH",
    "MILWAUKEE HAWKS": "MIL",
    "TRI-CITIES BLACKHAWKS": "TCB",
    "BOSTON CELTICS": "BOS",
    "BROOKLYN NETS": "BRK",
    "NEW JERSEY NETS": "NJN",
    "CHICAGO BULLS": "CHI",
    "CHARLOTTE HORNETS": "CHH",
    "CHARLOTTE HORNETS": "CHO",
    "CHARLOTTE BOBCATS": "CHA",
    "CLEVELAND CAVALIERS": "CLE",
    "DALLAS MAVERICKS": "DAL",
    "DENVER NUGGETS": "DEN",
    "DETROIT PISTONS": "DET",
    "FORT WAYNE PISTONS": "FWP",
    "GOLDEN STATE WARRIORS": "GSW",
    "SAN FRANCISCO WARRIORS": "SFW",
    "PHILADELPHIA WARRIORS": "PHI",
    "HOUSTON ROCKETS": "HOU",
    "INDIANA PACERS": "IND",
    "LOS ANGELES CLIPPERS": "LAC",
    "SAN DIEGO CLIPPERS": "SDC",
    "BUFFALO BRAVES": "BUF",
    "LOS ANGELES LAKERS": "LAL",
    "MINNEAPOLIS LAKERS": "MIN",
    "MEMPHIS GRIZZLIES": "MEM",
    "VANCOUVER GRIZZLIES": "VAN",
    "MIAMI HEAT": "MIA",
    "MILWAUKEE BUCKS": "MIL",
    "MINNESOTA TIMBERWOLVES": "MIN",
    "NEW ORLEANS PELICANS": "NOP",
    "NEW ORLEANS/OKLAHOMA CITY HORNETS": "NOK",
    "NEW ORLEANS HORNETS": "NOH",
    "NEW YORK KNICKS": "NYK",
    "OKLAHOMA CITY THUNDER": "OKC",
    "SEATTLE SUPERSONICS": "SEA",
    "ORLANDO MAGIC": "ORL",
    "PHILADELPHIA 76ERS": "PHI",
    "SYRACUSE NATIONALS": "SYR",
    "PHOENIX SUNS": "PHO",
    "PORTLAND TRAIL BLAZERS": "POR",
    "SACRAMENTO KINGS": "SAC",
    "KANSAS CITY KINGS": "KCK",
    "KANSAS CITY-OMAHA KINGS": "KCK",
    "CINCINNATI ROYALS": "CIN",
    "ROCHESTER ROYALS": "ROR",
    "SAN ANTONIO SPURS": "SAS",
    "TORONTO RAPTORS": "TOR",
    "UTAH JAZZ": "UTA",
    "NEW ORLEANS JAZZ": "NOJ",
    "WASHINGTON WIZARDS": "WAS",
}

teams_dict_name = {
    "Hawks": "ATL",
    "Celtics": "BOS",
    "Nets": "BRK",
    "Bulls": "CHI",
    "Hornets": "CHO",
    "Cavaliers": "CLE",
    "Mavericks": "DAL",
    "Nuggets": "DEN",
    "Pistons": "DET",
    "Warriors": "GSW",
    "Rockets": "HOU",
    "Pacers": "IND",
    "Clippers": "LAC",
    "Lakers": "LAL",
    "Grizzlies": "MEM",
    "Heat": "MIA",
    "Bucks": "MIL",
    "Timberwolves": "MIN",
    "Pelicans": "NOP",
    "Knicks": "NYK",
    "Thunder": "OKC",
    "Magic": "ORL",
    "76ers": "PHI",
    "Suns": "PHO",
    "Blazers": "POR",
    "Kings": "SAC",
    "Spurs": "SAS",
    "Raptors": "TOR",
    "Jazz": "UTA",
    "Wizards": "WAS",
}

def team_made_playoffs(team_name, season):
    playoff_teams = {
        2009: ['BOS', 'PHI', 'CLE', 'DET', 'ORL', 'ATL', 'MIA', 'CHI', 'DEN', 'POR', 'UTH', 'LAL', 'SAS', 'HOU', 'DAL', 'NOH'],
        2010: ['BOS', 'CLE', 'MIL', 'CHI', 'ORL', 'ATL', 'MIA', 'CHA', 'DEN', 'UTH', 'POR', 'OKC', 'LAL', 'PHO', 'DAL', 'SAS'],  
        2011: ['BOS', 'NYK', 'PHI', 'CHI', 'IND', 'MIA', 'ORL', 'ATL', 'OKC', 'DEN', 'POR', 'LAL', 'SAS', 'DAL', 'NOH', 'MEM'],
        2012: ['CHI', 'MIA', 'IND', 'BOS', 'ATL', 'ORL', 'PHI', 'NYK', 'SAS', 'OKC', 'LAL', 'MEM', 'LAC', 'DEN', 'DAL', 'UTA'],
        2013: ['NYK', 'BRK', 'BOS', 'IND', 'CHI', 'MIA', 'ATL', 'MIL', 'OKC', 'DEN', 'LAC', 'MEM', 'SAS', 'HOU', 'GSW', 'LAL'],
        2014: ['TOR', 'BRK', 'IND', 'CHI', 'MIA', 'WAS', 'CHA', 'ATL', 'OKC', 'POR', 'LAC', 'GSW', 'SAS', 'HOU', 'MEM', 'DAL'],
        2015: ['TOR', 'BOS', 'BRK', 'CLE', 'CHI', 'MIL', 'ATL', 'WAS', 'POR', 'HOU', 'MEM', 'SAS', 'DAL', 'NOP', 'GSW', 'LAC'],
        2016: ['CLE', 'TOR', 'MIA', 'ATL', 'BOS', 'CHO', 'IND', 'DET', 'GSW', 'SAS', 'OKC', 'LAC', 'POR', 'DAL', 'MEM', 'HOU'],
        2017: ['BOS', 'CLE', 'TOR', 'WAS', 'ATL', 'MIL', 'IND', 'CHI', 'GSW', 'SAS', 'HOU', 'LAC', 'UTA', 'OKC', 'MEM', 'POR'],
        2018: ['TOR', 'BOS', 'PHI', 'CLE', 'IND', 'MIA', 'MIL', 'WAS', 'HOU', 'GSW', 'POR', 'OKC', 'UTA', 'NOP', 'SAS', 'MIN'],
        2019: ['MIL', 'TOR', 'PHI', 'BOS', 'IND', 'BRK', 'ORL', 'DET', 'GSW', 'DEN', 'POR', 'HOU', 'UTA', 'OKC', 'SAS', 'LAC'],
        2020: ['MIL', 'TOR', 'BOS', 'IND', 'MIA', 'PHI', 'BRK', 'ORL', 'LAL', 'LAC', 'DEN', 'HOU', 'OKC', 'UTA', 'DAL', 'POR'],
        2021: ['PHI', 'BRK', 'MIL', 'NYK', 'ATL', 'MIA', 'BOS', 'WAS', 'UTA', 'PHO', 'DEN', 'LAC', 'DAL', 'POR', 'LAL', 'MEM'],
        2022: ['MIA', 'BOS', 'MIL', 'PHI', 'TOR', 'CHI', 'BRK', 'ATL', 'PHO', 'MEM', 'GSW', 'DAL', 'UTA', 'DEN', 'MIN', 'NOP'], 
        2023: ['MIL', 'BOS', 'PHI', 'CLE', 'NYK', 'BRK', 'MIA', 'ATL', 'DEN', 'MEM', 'SAC', 'PHO', 'LAC', 'GSW', 'LAL', 'MIN'],
        2024: []
    }

    # Verifica se il nome della squadra è presente nella lista delle squadre playoff per la stagione specificata
    return team_name in playoff_teams.get(season, [])

teams_dict_fullname_inverted = {v: k for k, v in teams_dict_fullName.items()}
teams_dict_name_inverted = {v: k for k, v in teams_dict_name.items()}

nba_regular_season_last_days = {
    2008: datetime(2008, 4, 16),
    2009: datetime(2009, 4, 15),
    2010: datetime(2010, 4, 14),
    2011: datetime(2011, 4, 13),
    2012: datetime(2012, 4, 26),
    2013: datetime(2013, 4, 17),
    2014: datetime(2014, 4, 16),
    2015: datetime(2015, 4, 15),
    2016: datetime(2016, 4, 13),
    2017: datetime(2017, 4, 12),
    2018: datetime(2018, 4, 11),
    2019: datetime(2019, 4, 10),
    2020: datetime(2020, 4, 15),
    2021: datetime(2021, 5, 16),
    2022: datetime(2022, 4, 10),
    2023: datetime(2023, 4, 16)
}

