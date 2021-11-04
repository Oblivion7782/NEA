
#import pandas as pd
import csv


dataing2 = """
Username, Password, Score
Oblivion, Fo0tba!l8, 0
"""

with open('UsePassData.csv', mode='w') as UserData:
    UserDataset = csv.writer(UserData, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #UserDataset.writerow(['Paddy123', 'hello'])
    Data = UserData.read()
    print(Data)
    UserDataset.writerow