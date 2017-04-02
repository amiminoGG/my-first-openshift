import os
import pymongo
import json
import pandas as pd

connection_string = os.environ['OPENSHIFT_MONGODB_DB_URL']

myMongo_client = pymongo.MongoClient(connection_string)

myMongo_YYC_client = myMongo_client.yyc30.London_Visitors

filepath = 'international-visitors-london-raw.csv'

my = pd.read_csv(filepath, dtype = None, skipinitialspace = True)

my_doc = json.loads(my.T.to_json()).values()

myMongo_YYC_client.drop()
myMongo_YYC_client.insert(my_doc)

test_query = myMongo_YYC_client.find({'year':'2002','purpose':'Business','mode':'Air','nights':{"$lte":1}})

for i, doc in enumerate(test_query):
    print(i+1)
    for attr, val in doc.iteritems():
        print('{}:{}'.format(attr,val))
    print('\n')

myMongo_client.close()
