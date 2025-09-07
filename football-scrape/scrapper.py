"""
The goals:
 - Scrape the season details for each team starting at 2010
 - Organize the data so that analysis can be performed
    - As an added bonus, export this data. Each time the script starts, import
        the dataset and add to it if necessary.
 - Create several plots/charts to show how the Bears are doing vs Green Bay
 - Ensure that this script can be executed at anytime and will pick up the delta & sync
"""
import os.path
import time
import pandas as pd
from bs4 import BeautifulSoup
from seleniumbase import Driver

SEASON_RESULTS_DICT = {'WildCard':1, 'Division':2, 'Conference':3, 'SuperBowl':4 }

COLUMNS = ['season', 'team', 'conf', 'region', 'wins', 'losses', 'win_percent', 'pts_scored', 'pts_allowed', 'pts_diff', 'season_result', 'season_result_int']
SLEEP_TIME = 5  # seconds
OUTPUT_DIR = '~/Code/python-portfolio/football-scrape/generated' #'/Users/komil/Code/python-portfolio/football-scrape/generated'

final_df = pd.DataFrame(columns=COLUMNS)

# driver = Driver(headless=True)
driver = Driver(headless=True, uc=True, disable_gpu=True, no_sandbox=True, page_load_strategy='none')
driver.set_page_load_timeout(10)
driver.set_window_size(300, 300)
driver.set_script_timeout(10)

# Get the seasonal data for each team & season
def scrapeForSeasonalData(year):
  URL = f'https://www.pro-football-reference.com/years/{year}/'

  print(f'\nStart scraping for {year}.')

  driver.get(URL)

  soup = BeautifulSoup(driver.get_page_source(), 'html.parser')

  stats_tables = soup.select('table#AFC > tbody, table#NFC > tbody')
  playoff_result_rows = soup.select('table#playoff_results > tbody > tr')

  # extract playoff results
  print(f'Extracting playoff results ...')

  playoff_table_df = pd.DataFrame(columns=['result_str', 'result_int', 'team'])
  playoff_df = pd.DataFrame(columns=['result_str', 'result_int', 'team'])

  for row in playoff_result_rows:
    result_str = row.select('th')[0].get_text()
    result_int = SEASON_RESULTS_DICT.get(result_str)
    winning_team = row.select('td[data-stat=winner]')[0].get_text()
    losing_team = row.select('td[data-stat=loser]')[0].get_text()

    playoff_table_df.loc[len(playoff_table_df)] = {'result_str': result_str, 'result_int': result_int, 'team': winning_team}
    playoff_table_df.loc[len(playoff_table_df)] = {'result_str': result_str, 'result_int': result_int, 'team': losing_team}

  # create a new dataframe with the highest result value for each team
  for team in playoff_table_df['team'].unique():
    playoff_df.loc[len(playoff_df)] = playoff_table_df[playoff_table_df['team'] == team].sort_values(by=['team', 'result_int'], ignore_index=True, ascending=[True, False]).loc[0]

  print(f'Done extracting playoff results!')
  # print(playoff_df.info())
  # print(playoff_df)
  # print('-----------------------------------------')

  # return
  # -----------------------------------

  # extract the stats
  print(f'Extracting stats ...')
  for row in stats_tables:
    content_rows = row.select('tr')
    conf, region = '', ''
    for r in content_rows:
      th = r.select_one('th')
      tds = r.select('td:not([data-stat=ties])')

      if len(tds) == 1:
        t = tds[0].text.strip().split(' ')
        conf = t[0].strip()
        region = t[1].strip()
      else:
        team_replacement = str.maketrans({'*':'', '+':''})
        team = th.get_text().translate(team_replacement)
        season_status = 'Regular' if playoff_df.loc[playoff_df['team']==team].empty else playoff_df[playoff_df['team']==team].values[0,0]
        season_status_int = 0 if playoff_df[playoff_df['team']==team].empty else playoff_df[playoff_df['team']==team].values[0,1]
        wins = int(tds[0].get_text())
        losses = int(tds[1].get_text())
        win_pct = float(tds[2].get_text())
        pts_scored = int(tds[3].get_text())
        pts_allowed = int(tds[4].get_text())
        pts_diff = int(tds[5].get_text())

        new_row = {
          'season': year,
          'team': team,
          'conf': conf,
          'region': region,
          'wins': wins,
          'losses': losses,
          'win_percent': win_pct,
          'pts_scored': pts_scored,
          'pts_allowed': pts_allowed,
          'pts_diff': pts_diff,
          'season_result': season_status,
          'season_result_int': season_status_int
        }
        final_df.loc[len(final_df)] = new_row
        print(new_row)

  print(f'Done extracting stats!')

  print(f'Finished scraping for {year}.')
  print(f'>>> sleeping for {SLEEP_TIME}.\n\n')
  time.sleep(SLEEP_TIME)


# scrape for all the years
for year in range(2000, 2003):
  scrapeForSeasonalData(year)

driver.close()
driver.quit()

# export the dataframe to csv
final_df.to_csv(os.path.join(OUTPUT_DIR,'seasonal-data-sm.csv'), index=False, columns=COLUMNS)


print('All done!')