# To enable ssh & remote debugging on app service change the base image to the one below
# FROM mcr.microsoft.com/azure-functions/python:2.0-python3.6-appservice
FROM mcr.microsoft.com/azure-functions/python:2.0-python3.6

ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true

ENV myMongoDbconnectionString=mongodb://cosmosdbneighborly:L46FpRk7Wy2FBSgSHluBRoObcNbVUE8FjvoWNbVfdJKTrSsevKWasB2jpY4mEb7TGrO4oBJAz0mqnFmZnZTE4w==@cosmosdbneighborly.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@cosmosdbneighborly@


COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY . /home/site/wwwroot