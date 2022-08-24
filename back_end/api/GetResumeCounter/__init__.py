from email.headerregistry import ContentTypeHeader
from importlib.util import resolve_name
import json
import logging

import azure.functions as func


def main(req: func.HttpRequest, readdb: func.DocumentList, updatedb: func.Out[func.Document]) -> func.HttpResponse:
    # logging.info('Python HTTP trigger function processed a request.')
    # if not azureresume:
    #     logging.warning("azureresume item not found")
    # else:
    #     logging.info("Found count item, Description=%s", azureresume[0]['count'])
    currentrow = readdb[0].data
    print(type(readdb[0].data))
    currentrow['count'] = currentrow['count'] + 1
    #response['count'] = newcount
    print("about to print")
    print(currentrow)
    # write to the cosmos DB the new count
    # new commet new
    response = func.HttpResponse(
        body=json.dumps(currentrow),
        status_code=200,
        headers={'Content-Type':'application/json'}
    )   

    updatedb.set(func.Document.from_dict(currentrow))

    return response

 


# create an input binding to retrieve the count from the CosmosDB, id="1"
# create an input binding to retrieve the count from the CosmosDB, id="1"
# equate updatedCounter = counter
# equate updatedCount.Count += 1
# structure json
# return an func.HttpResponse that shows the new json
# after running the function, the local host should show the json and increment the count each time refreshed

    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')

    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )
