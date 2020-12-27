import azure.functions as func
import pymongo
import os
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = os.environ['myMongoDbconnectionString']
            client = pymongo.MongoClient(url)
            database = client['neighborlydB']
            collection = database['advertisements']
    
    
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query) # note: the id is real oid
            if result is None:
                query = {'_id':id}
                result = collection.delete_one(query) # note: the id is just a string in db due to import

            if (result.deleted_count >0):
                return func.HttpResponse("Successfuly deleted Ad with ID "+id, status_code=200)
            else:
                return func.HttpResponse("id not found "+id, status_code=400)

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
