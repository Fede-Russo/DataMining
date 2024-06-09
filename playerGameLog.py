import pandas as pd
import basketball_reference_scraper.players as players
from SQLManager import insert_data, get_player_name
import utilities as utl

seasons = [2024]

# Ottenere la lista dei giocatori
players_list = get_player_name()
players_list = players_list.sort_values('PLAYER')

# Iterare attraverso le stagioni
for season in seasons:
    # Iterare attraverso i giocatori
    for player in players_list['PLAYER']:
        try:
            # Ottenere i log delle partite per il giocatore nella stagione corrente
            df = players.get_game_logs(player, season, False)
            df['PLAYER'] = player
            # Inserire i dati nel database
            insert_data(df, 'player_game_logs')
            print(f"Dati inseriti per la stagione {season} e il giocatore {player}")
        except Exception as e:
            print(f"Errore durante l'ottenimento dei log delle partite per il giocatore {player} nella stagione {season}: {e}")
