from database import Database

import json


dataset = json.loads(open('dataset.json', 'r').read())

db = Database()

for key in dataset:
    docs = list()
    for data in dataset[key]:
        data.pop("id")
        docs.append(data)
    db.insertMany(key, docs)

