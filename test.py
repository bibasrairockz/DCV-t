import pandas as pd

data = [
    {"Name": "Bibas", "Age": "90", "Sex": "Karva do"},
    {"Name": "Nono", "Age": "43", "Sex": "Nahi"},
    {"Name": "Yesyes", "Age": "23", "Sex": "lol"},
    {"Name": "AchaAcha", "Age": "1", "Sex": "bhakk"}   
]

Data = pd.DataFrame(data)

Data.to_csv("data/data.csv", index = False)