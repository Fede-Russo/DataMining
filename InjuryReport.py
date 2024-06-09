'''Questo script permette di prelevare i dati dal sito https://www.prosportstransactions.com
    I dati che vogliamo prelevare sono tutti quelli riguardanti gli infortuni dei giocatori
    nelle stagioni dal 2008-2009 al 2023-2024. Per fare questo utilizziamo il web-scraping per
    analizzare la pagina html ottenuta dalla ricerca e preleviamo i dati rilevanti.
    Le richieste di ricerca dei dati sul sito sono di due tipi:
        -  Movement to/from injured/inactive list (IL): per gli infortuni piu' gravi solitamente;
        -  Missed games due to injury: per assenza di uno/due game;
    Alla fine otterremo un DataFrame della forma:

        +-------------+---------+-------------------+---------------------+-----------------------------+
        |    Date     |  Team   |     Acquired      |    Relinquished     |            Notes            |
        +-------------+---------+-------------------+---------------------+-----------------------------+
        | 2008-11-25  | Nets    |                   | • Eduardo Najera    | placed on IL with sore back |
        | 2008-11-25  | Nets    | • Stromile Swift  |                     | activated from IL           |
        | 2008-11-25  | Pacers  |                   | • Travis Diener     | sore left foot (DNP)        |
        | 2008-11-25  | Suns    |                   | • Shaquille O'Neal  | hip injury (DNP)            |
        +-------------+---------+-------------------+---------------------+-----------------------------+
        
    Il DataFrame viene poi salvato in un database "nbadata"; dal momento che i risultati sono tanti, 
    questi verranno salvati a ogni iterazione e non alla fine del processo
    '''
import requests
import pandas as pd
import time
from bs4 import BeautifulSoup
import utilities as utl
import SQLManager as sql

def get_injury_report_from_team():
    #URL to scrape from
    url = "https://www.prosportstransactions.com/basketball/Search/SearchResults.php?Player=&Team=&BeginDate=2008-08-01&EndDate=&ILChkBx=yes&InjuriesChkBx=yes&Submit=Searc&start=0"
    
    print(url)
    #-------------Scrape web page----------------------------

    #Get URL HTML
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    print(response) # Response [200] means it went through

    #Parse HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the table in the HTML using BeautifulSoup
    table = soup.find('table', class_='datatable')

    # Extract table rows
    rows = table.find_all('tr')

    # Initialize lists to hold the data
    data = []

    # Loop through rows and extract data
    for row in rows[1:]:  # Skip the header row
        # Extract table data cells
        cells = row.find_all('td')
        # Extract text from each cell and append to the data list
        row_data = [cell.get_text(strip=True) for cell in cells]
        # Append row data to the main data list
        data.append(row_data)

    # Create DataFrame from the data
    df_total = pd.DataFrame(data, columns=['Date', 'Team', 'Acquired', 'Relinquished', 'Notes'])
    
    # Convert 'Date' column to datetime type
    df_total['Date'] = pd.to_datetime(df_total['Date'])
    
    # Save to the database the first data
    sql.insert_injury_report(df_total)

    #------------Scrape data from other pages linked at the bottom of the first page------------
    # Loop over links (skipping the first 4 (not data) and last 4 ("Next" and other webpage links))
    for i in range(5,len(soup.findAll('a'))-3): #'a' tags are for links
    
        #find all links on webpage and select the i-th link
        one_a_tag = soup.findAll('a')[i]
        link = one_a_tag['href']
        
        #Add in the rest of the url
        download_url = 'https://www.prosportstransactions.com/basketball/Search/'+ link
        print(download_url)
        response = requests.get(download_url, headers=headers)
        
        #Parse HTML with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find the table in the HTML using BeautifulSoup
        table = soup.find('table', class_='datatable')

        # Extract table rows
        rows = table.find_all('tr')

        # Initialize lists to hold the data
        data = []

        # Loop through rows and extract data
        for row in rows[1:]:  # Skip the header row
            # Extract table data cells
            cells = row.find_all('td')
            # Extract text from each cell and append to the data list
            row_data = [cell.get_text(strip=True) for cell in cells]
            # Append row data to the main data list
            data.append(row_data)

        # Create DataFrame from the data
        df = pd.DataFrame(data, columns=['Date', 'Team', 'Acquired', 'Relinquished', 'Notes']) 
        
        # Save to the database the data obtained at each iteration
        df['Date'] = pd.to_datetime(df['Date'])
        sql.insert_injury_report(df)
         
        #Append data frame 
        df_total=pd.concat([df_total,df], ignore_index=True)
        
        #Add a pause to keep web server happy
        time.sleep(3)
        
get_injury_report_from_team()