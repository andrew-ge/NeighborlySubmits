import azure.functions as func
import pymongo
import os
from bson.objectid import ObjectId

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')
    request = req.get_json()

    if request:
        try:
            url = os.environ['myMongoDbconnectionString']
            client = pymongo.MongoClient(url)
            database = client['neighborlydB']
            collection = database['advertisements']
            
            filter_query = {'_id': ObjectId(id)}
            update_query = {"$set": eval(request)} #not able to use eval
            rec_id1 = collection.update_one(filter_query, update_query)
            if (rec_id1.modified_count!=1):
                filter_query = {'_id': id}
                rec_id1 = collection.update_one(filter_query, update_query)
            
            if (rec_id1.modified_count==1):
                return func.HttpResponse("updated Advertisement with id: "+id, status_code=200)
            else:
                return func.HttpResponse("Failed to updated Advertisement with id: "+id+" not found in DB", status_code=400)
            
        except:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)
    else:
        return func.HttpResponse('Please pass name in the body', status_code=400)

