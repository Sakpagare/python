# conveting dictionary file into json file

import json

sports = ['cricket','kabbadi','tennis','badminton']

data = dict(list(enumerate(sports,1)))
f = open('data.json','w')
json.dump(data,f)

f.close()
