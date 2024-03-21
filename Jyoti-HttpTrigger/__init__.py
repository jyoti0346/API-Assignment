# import logging
# import azure.functions as func
# import pymongo

# MongoDB connection URI
MONGO_URI = "your_mongo_uri_here"
# Database and collection names
DB_NAME = "your_database_name"
COLLECTION_NAME = "your_collection_name"



# def create(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Creating a new resource.')

#     # Extract name from request body
#     try:
#         req_body = req.get_json()
#     except ValueError:
#         return func.HttpResponse("Invalid JSON format", status_code=400)

#     name = req_body.get('name')
#     if not name:
#         return func.HttpResponse("Name parameter is required for creating a resource", status_code=400)
       
      try:
        # Connect to MongoDB
        client = pymongo.MongoClient(MONGO_URI)
        database = client[DB_NAME]
        collection = database[COLLECTION_NAME]

        # Query MongoDB
        result = collection.find_one({"name": name})
        client.close()

#     # Here, you would have your logic for creating a new resource
#     # Replace the return statement with your actual creation logic
#     return func.HttpResponse(f"Resource {name} created successfully", status_code=201)


# def read(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Reading the resource.')

#     # Extract name from query parameters or request body
#     name = req.params.get('name')
#     if not name:
#         try:
#             req_body = req.get_json()
#         except ValueError:
#             pass
#         else:
#             name = req_body.get('name')

#     if not name:
#         return func.HttpResponse("Name parameter is required for reading a resource", status_code=400)

#     # Here, you would have your logic for reading the resource
#     # Replace the return statement with your actual read logic
#     return func.HttpResponse(f"Reading resource {name}", status_code=200)


# def update(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Updating the resource.')

#     # Extract name from request body
#     try:
#         req_body = req.get_json()
#     except ValueError:
#         return func.HttpResponse("Invalid JSON format", status_code=400)

#     name = req_body.get('name')
#     if not name:
#         return func.HttpResponse("Name parameter is required for updating a resource", status_code=400)

#     # Here, you would have your logic for updating the resource
#     # Replace the return statement with your actual update logic
#     return func.HttpResponse(f"Resource {name} updated successfully", status_code=200)


# def delete(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Deleting the resource.')

#     # Extract name from request body
#     try:
#         req_body = req.get_json()
#     except ValueError:
#         return func.HttpResponse("Invalid JSON format", status_code=400)

#     name = req_body.get('name')
#     if not name:
#         return func.HttpResponse("Name parameter is required for deleting a resource", status_code=400)

#     # Here, you would have your logic for deleting the resource
#     # Replace the return statement with your actual delete logic
#     return func.HttpResponse(f"Resource {name} deleted successfully", status_code=200)


# def main(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')

#     # Route requests based on HTTP method
#     if req.method == 'POST':
#         return create(req)
#     elif req.method == 'GET':
#         return read(req)
#     elif req.method == 'PUT':
#         return update(req)
#     elif req.method == 'DELETE':
#         return delete(req)
#     else:
#         return func.HttpResponse("Method not allowed", status_code=405)

import logging
import azure.functions as func
import pymongo

# MongoDB connection URI
MONGO_URI = "your_mongo_uri_here"
# Database and collection names
DB_NAME = "your_database_name"
COLLECTION_NAME = "your_collection_name"


def create(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Creating a new resource.')

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON format", status_code=400)

    name = req_body.get('name')
    if not name:
        return func.HttpResponse("Name parameter is required for creating a resource", status_code=400)

    try:
        # Connect to MongoDB
        client = pymongo.MongoClient(MONGO_URI)
        database = client[DB_NAME]
        collection = database[COLLECTION_NAME]

        # Insert data into MongoDB
        new_resource = {"name": name}
        result = collection.insert_one(new_resource)

        client.close()
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return func.HttpResponse("Internal Server Error", status_code=500)

    return func.HttpResponse(f"Resource {name} created successfully", status_code=201)


def read(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Reading the resource.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if not name:
        return func.HttpResponse("Name parameter is required for reading a resource", status_code=400)

    try:
        # Connect to MongoDB
        client = pymongo.MongoClient(MONGO_URI)
        database = client[DB_NAME]
        collection = database[COLLECTION_NAME]

        # Query MongoDB
        result = collection.find_one({"name": name})
        client.close()
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return func.HttpResponse("Internal Server Error", status_code=500)

    if result:
        return func.HttpResponse(f"Reading resource {name}", status_code=200)
    else:
        return func.HttpResponse(f"Resource {name} not found", status_code=404)


def update(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Updating the resource.')

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON format", status_code=400)

    name = req_body.get('name')
    if not name:
        return func.HttpResponse("Name parameter is required for updating a resource", status_code=400)

    try:
        # Connect to MongoDB
        client = pymongo.MongoClient(mongodb+srv://jahanvimehta46034:NKxkrn7whDgPQf7b@jyoti-cluster.jh2vgbu.mongodb.net/?retryWrites=true&w=majority&appName=Jyoti-Cluster)
        database = client[jyoti-database]
        collection = database[jyoti-collection]

        # Update MongoDB document
        result = collection.update_one({"name": name}, {"$set": {"updated_field": "updated_value"}})
        client.close()
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return func.HttpResponse("Internal Server Error", status_code=500)

    if result.modified_count > 0:
        return func.HttpResponse(f"Resource {name} updated successfully", status_code=200)
    else:
        return func.HttpResponse(f"Resource {name} not found", status_code=404)


def delete(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Deleting the resource.')

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON format", status_code=400)

    name = req_body.get('name')
    if not name:
        return func.HttpResponse("Name parameter is required for deleting a resource", status_code=400)

    try:
        # Connect to MongoDB
        client = pymongo.MongoClient(MONGO_URI)
        database = client[DB_NAME]
        collection = database[COLLECTION_NAME]

        # Delete MongoDB document
        result = collection.delete_one({"name": name})
        client.close()
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return func.HttpResponse("Internal Server Error", status_code=500)

    if result.deleted_count > 0:
        return func.HttpResponse(f"Resource {name} deleted successfully", status_code=200)
    else:
        return func.HttpResponse(f"Resource {name} not found", status_code=404)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if req.method == 'POST':
        return create(req)
    elif req.method == 'GET':
        return read(req)
    elif req.method == 'PUT':
        return update(req)
    elif req.method == 'DELETE':
        return delete(req)
    else:
        return func.HttpResponse("Method not allowed", status_code=405)

