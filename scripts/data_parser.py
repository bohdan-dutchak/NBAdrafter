from bs4 import BeautifulSoup, Comment
import pandas as pd
import requests
import time

import config


def get_teams_urls(year):
    '''
    Returns links of team's stats pages due to the season.
    '''
    url = config.season_url + str(year) + '.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    table = soup.find('table', {'id':'totals-team'})
    urls = []
    for a in table.find_all('a', href=True):
        urls.append(a['href'])
    return urls


def get_column_names(table):
    '''
    Returns columns names of the table
    '''
    headers = []
    thead = table.find('thead')
    for header in thead.find_all('th'):
        title = header.text
        headers.append(title)
    headers[1] = 'Player' #Here we rename the name on 2nd element, since it is unnamed in the table
    return headers[1:]


def get_per_game(url):
    """
    Collects the data from the 'Per game' table
    for particular team on particular season
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    table = soup.find('table', {'id':'per_game'})
    headers = get_column_names(table)
    season = pd.DataFrame(columns=headers)
    for row in table.find_all('tr'):
        data = row.find_all('td')
        row_data = [td.text.strip() for td in data]
        if len(row_data) != 0:
            season.loc[len(season)] = row_data
    return season


def get_roster(url):
    """
    Collects the data from the 'Roster' table
    for particular team on particular season
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    table = soup.find('table', {'id':'roster'})
    headers = get_column_names(table)
    roster = pd.DataFrame(columns=headers)
    for row in table.find_all('tr'):
        data = row.find_all('td')
        row_data = [td.text.strip() for td in data]
        if len(row_data) != 0:
            roster.loc[len(roster)] = row_data
    return roster


def process_data(df : pd.DataFrame, year):
    """
    Arbitrary data processing i.e. dropping unneccessary columns
    and tiny feature engineering
    """
    df = df.drop(columns=['Birth Date', 'College'])
    df = df.drop(df.columns[4], axis=1)
    df['Ht'] = df['Ht'].apply(lambda x: x.split('-'))
    df['Ht'] = df['Ht'].apply(lambda x: round(int(x[0])*30.48+int(x[1])*2.54), 2)
    df['Wt'] = df['Wt'].apply(lambda x: round(int(x) * 0.45359237), 2)
    
    df['Exp'] = df['Exp'].apply(lambda x: x.replace('R', '0'))
    df['Season'] = year
    return df


def append_data(season_data, team):
    """
    Concatenating teams data into one season table
    """
    if season_data is None:
        season_data = team
    else:
        season_data = season_data.append(team)
    return season_data


def main():
    start = time.time()
    print(f"Collecting data from seasons {config.start_year} - {config.end_year}")
    player_counter = 0
    
    for year in range(config.start_year, config.end_year + 1):
        season_data = None
        team_urls = get_teams_urls(year)
        
        for team in team_urls:
            url = config.url+team
            #print(url)
            
            roster = get_roster(url)
            per_game = get_per_game(url)
            
            result = roster.merge(per_game, on='Player', how='inner')
            season_data = append_data(season_data, process_data(result, year))

        season_data.to_csv(f'data/s_{year-1}-{year}.csv', index=False)
        print(f"Season {year} is completed!\nNumber of teams: {len(team_urls)}\nUnique players: {len(season_data)}\n")
        player_counter += len(season_data)
    
    end = time.time()
    print(f"Done!\nTotal number of observations: {player_counter}")
    print(f"Execution time: {round(end-start, 2)}sec.")
    

if __name__ == '__main__':
    main()