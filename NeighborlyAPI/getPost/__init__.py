import azure.functions as func
import pymongo
import json
import os
from bson.json_util import dumps
from bson.objectid import ObjectId

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            # Update with appropriate MongoDB connection information
            url = os.environ["MongoDBConnection"]  
            client = pymongo.MongoClient(url)
            database = client[os.environ["MongoDBDatabase"]]
            collection = database['posts']

            query = {'_id': ObjectId(id)}
            result = collection.find_one(query)
            result = dumps(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)