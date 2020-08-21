import requests
import pandas as pd

compiled_forks = pd.DataFrame()

for i in range(1,616):
    url = 'https://www.chess.com/puzzles/problems?tagId=14&page={}'.format(i)
    html = requests.get(url).content
    df_list = pd.read_html(html)
    df = df_list[-1]
    compiled_forks = pd.concat([compiled_forks,df])
    print(i)

compiled_forks.to_csv('all_mate_in_one.csv')