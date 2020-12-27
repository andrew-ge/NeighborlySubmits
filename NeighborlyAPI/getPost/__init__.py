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
            url = os.environ['myMongoDbconnectionString']
            client = pymongo.MongoClient(url)
            database = client['neighborlydB']
            collection = database['posts']

            query = {'_id': ObjectId(id)}
            result = collection.find_one(query) # note: the id is real oid
            if result is None:
                query = {'_id':id}
                result = collection.find_one(query) # note: the id is just a string in db due to import

            result = dumps(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)