import azure.functions as func
import pymongo
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    #print("Get into the funciton with ", req.params['data'])
    request = req.get_json()
    #print ('json part of your request is: ',request)
    if request:
        try:
            url = os.environ['myMongoDbconnectionString']
            client = pymongo.MongoClient(url)
            database = client['neighborlydB']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))  #no need to use eval as json can be imported

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )