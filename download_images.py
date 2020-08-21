import pandas as pd
import requests
import urllib.request

forks = pd.read_csv(r'C:\Users\bwaddell\Desktop\Learning\MachineLearning\ChessTacticIdentifier\all_mate_in_one_w_fens.csv')

def dl_jpg(url,file_path,file_name):
    full_path = file_path + str(file_name) + ".jpg"
    urllib.request.urlretrieve(url,full_path)
    return

for index, row in forks.iterrows():
    print(index)
    url = 'http://www.fen-to-image.com/image/{}.png'.format(row['fen'])
    dl_jpg(url,r'C:\Users\bwaddell\Desktop\Learning\MachineLearning\ChessTacticIdentifier\MateInOneImages\MateInOne',row['ID'])