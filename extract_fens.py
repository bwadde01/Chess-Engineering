import pandas as pd
import requests

forks = pd.read_csv('all_mate_in_one.csv')

forks['fen'] = forks['url'].apply(lambda x: str(requests.get(x).content).split('fen=')[1].split('&')[0])

forks.to_csv('all_mate_in_one_w_fens.csv')