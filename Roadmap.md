# Obiettivi
Cosa voglio valutare?
Idee:
- Classificare i giocatori nei vari ruoli secondo caratteristiche comuni? (fase di data reduction per capire quali sono le statistiche correlate con ogni ruolo)
- Trovare gli outliner per ogni ruolo?
- Predire chi vincerà il titolo di MVP o comunque valutare una statistica composto per calcolarlo? (paper)
- Analisi degli infortuni? (data merging tra i due database, analisi delle frasi per carpire gli infortuni piu' frequenti, correlazione tra eta', altezza, peso, n partire in back to back)

# RoadMap
## Data Acquisition
Ottenere i dati relativi alle statistiche regionali dei vari giocatori negli ultimi x anni (x in questo caso e' 15).
- Data Scraping da Basketball reference per le statistiche e i rooster degli ultimi x anni.
- Data Scraping da ProSportsTransaction per ottenere i dati relativi agli infortuni.

## Data Cleaning
- Rimuovere tutti i giocatori non coinvolti nell'analisi (tutti quelli che hanno giocato meno di x partite o meno di x minuti per partita);
- Aggiustare i valori NULL nelle statistiche (principalmente derivanti da percentuali al tiro mancanti);
- Rimuovere dati inutili (ad esempio il collage di provenienza);
- Integrare i due dataset ottenuti da Basketball reference e prosportstransaction (il nome dei giocatori non corrisponde);
