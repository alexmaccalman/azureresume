# back_end

## steps
consider switchin to COR SQL  

create a function with an HTTPtrigger
connect Azure CosmosDB to the function
    inside of the local.settings.json we should add the connection string to CosmosDB, under values write:
        "AzureREsumeConnectionString":"paste in primary connection string here"
    now add binding to code  
        add a python class to decribe the counter object.     
        import json  
        create a counbter class with an id as a string and a counter as an int  
        JSON should have the follwoing key:value pairs  
            "id": string value of the id  
            "count": int value of the count   
        make sure that the key value names match what is inside the CosmosDB counter container, Item   

now add the CosmosDB binding to the azure function
```
[CosmosDB(databaseName"resumedb", collectionName: "counter", ConnectionStringSetting = "AzureResumeConnectionString")], Id = "1", PartitionKey = "1"} Counter counter, ILogger log)
```
add the output bindings for the updated counter
```
[CosmosDB(databaseName"resumedb", collectionName: "counter", ConnectionStringSetting = "AzureResumeConnectionString")], Id = "1", PartitionKey = "1"} out Counter updatedcounter, ILogger log)
```
note this is what we saved in the local.settings.json file  
ID is the item we want to retrieve  
Counter is where we will store it

write code to update the counter  
```python
updatedCounter = counter;
updatedCounter.Count += 1;

jsonToReturn "some code"
```
write some python to update the json object. The return the counter object in json format


After we get the function running locally and view in browser, now we will hook up the front end with the back end  

the main.js update the api url with function local url then run locally

To run locally, inside local.settings.json, add
```
"Host":
{
        "CORS": "*"
}
```  
we can grab the local url and see it in a browser

Inside the main.js, paste the local url  

Now let's deploy the azure function  
In Azure tool , use advance tools to create an azure function in cloud in VS code
Inside the function app, go to configuration, add a new application setting, add teh follwoing:
    Name: AzureResumeConnectionString
    Value: paste connection string here
The configuration is the local.setting.json but in cloud
We need to use azure key vault to do this
Inside the azure function click Get Function URL at the top and paste this url inside the main.js. create a const variable. You can also create a local function api constant. 

Now we have to enable CORS. in portal, inside teh function app on left select COR and enable access-control-allow-credentials 
We can check the url in a browser, got to Get Function URL and paste into browser  







1. write the main.js
2. create function app locally with personal computer, see if vs code works
3. 
