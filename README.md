# DataMining
Progetto di Data Mining per l'Università di Pisa a cura di Federico Russo.

## Descrizione del Progetto
Questo progetto ha l'obiettivo di raccogliere, analizzare e studiare i dati statistici e gli infortuni dei giocatori della NBA (National Basketball Association) nel periodo che va dalla stagione 2008-2009 alla 2023-2024. Il workflow del progetto si divide in due fasi principali:

1. **Raccolta dei Dati e Data Cleaning**: Vengono eseguiti degli script Python per effettuare web scraping da siti di riferimento (tra cui *basketball-reference.com* e *prosportstransactions.com*) al fine di ottenere statistiche e report sugli infortuni. I dati ottenuti vengono formattati e caricati all'interno di un database SQLite locale.
2. **Data Exploration & Mining**: L'analisi, l'esplorazione e la modellazione dei dati raccolti, interamente sviluppata all'interno del Jupyter Notebook principale.

## Componenti del Progetto e File

### 1. Notebook e Documentazione
- **`Data Mining Project.ipynb`**: È il cuore del progetto. Contiene l'intero studio di data mining, inclusa l'esplorazione visiva dei dati, la loro normalizzazione e lo sviluppo dei modelli analitici (es. clustering o predizione).
- **`Glossary.md` / `Glossary.pdf`**: Contengono il glossario delle sigle e degli acronimi statistici riferiti ai dati e utilizzati nel notebook per analizzare le metriche dei giocatori (es. AST, TRB, TOV, ecc.).
- **`README.md`**: File di panoramica del progetto.

### 2. Script di Web Scraping
Questi script estraggono i dati grezzi da internet e li preparano per l'inserimento nel database:
- **`PlayerStats.py`**: Esegue lo scraping delle statistiche associate a ciascun giocatore a roster per tutte le squadre NBA (medie classiche per partita, per minuto e statistiche avanzate) analizzando anche la Regular Season e i Playoff separatamente.
- **`TeamRoster.py`**: Estrae i dati relativi ai roster (la composizione della squadra) per le diverse stagioni NBA dal 2008 in avanti.
- **`InjuryReport.py`**: Interroga e fa il parsing delle informazioni inerenti gli infortuni e l'inattività dei giocatori, incluse le date, i nomi dei giocatori e i relativi motivi di assenza.
- **`playerGameLog.py`**: Recupera il registro storico delle prestazioni nei singoli match giocatori.

### 3. Gestione Database
Per immagazzinare i dati strutturati, il progetto si appoggia a un database locale SQLite, il cui file risiede solitamente nella cartella `database` (`nbadata.db`).
- **`SQLDatabaseCreator.py`**: Script per configurare la struttura DDL del database, imposta e genera le tabelle necessarie (stats regolari, stats avanzate, log partite e injury report).
- **`SQLManager.py`**: Modulo con funzioni di utility per la connessione al database e la semplificazione delle query di INSERT (tramite batching dei dataframe) verso il database.
- **`database/`**: Cartella di storage destinata a ospitare il file system SQLite (`nbadata.db`). *(Nota: I file non funzionali all'analisi presenti nella cartella originali vengono ignorati)*.

### 4. Utility
- **`utilities.py`**: Script contenente liste di costanti (come liste esplicite delle stagioni dal 2008 a oggi e dizionari di conversione per i nomi o le abbreviazioni delle squadre) e altre operazioni di calcolo comuni riutilizzabili.
