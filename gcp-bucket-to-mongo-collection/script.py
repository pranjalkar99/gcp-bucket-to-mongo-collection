from google.cloud import storage
from pymongo import MongoClient
import json

def transfer_json_to_mongodb(bucket_name, gcs_credentials_path, mongo_uri, mongo_db_name, mongo_collection_name):
    """
    Transfers JSON files from Google Cloud Storage to MongoDB.

    Args:
        bucket_name (str): The name of the Google Cloud Storage bucket.
        gcs_credentials_path (str): The path to the JSON file containing the Google Cloud Storage credentials.
        mongo_uri (str): The URI for connecting to the MongoDB database.
        mongo_db_name (str): The name of the MongoDB database.
        mongo_collection_name (str): The name of the MongoDB collection.

    Returns:
        None

    Raises:
        SpecificException: If a specific error occurs.
        AnotherSpecificException: If another specific error occurs.
        Exception: If a general error occurs.
    """


    # Initialize Google Cloud Storage client with credentials
    storage_client = storage.Client.from_service_account_json(gcs_credentials_path)

    # Get the GCS bucket
    bucket = storage_client.get_bucket(bucket_name)

    # List all JSON files in the bucket
    blobs = list(bucket.list_blobs())
    print(blobs)

    # Initialize MongoDB client and database
    mongo_client = MongoClient(mongo_uri)
    db = mongo_client[mongo_db_name]
    collection = db[mongo_collection_name]

    # Loop through each JSON file and transfer to MongoDB
    for blob in blobs:
        try:
            if blob.name.endswith(".json"):
                json_text = blob.download_as_text()
                json_data = json.loads(json_text)
                f=open("demo.json","w+")
                f.write(json.dumps(json_data))
                f.close()

                for key in json_data:
                    if isinstance(json_data[key], str) and "does not answer" in json_data[key].lower():
                        json_data[key] = ""
                collection.insert_one(json_data)
                print(f"Data from {blob.name} inserted into MongoDB.")

        
        except Exception as e:
            print(f"General Error: {e}")

    print("All data inserted into MongoDB successfully.")

#transfer_json_to_mongodb("compfox-pipeline-website-v2", "compfox-367313-c9759906c8b0.json", "mongodb+srv://compfox_app:5LwScVxeywOaSLF2@compfox.baxjg.mongodb.net/compfox-db-staging?retryWrites=true&w=majority", "compfox-db", "cases-new")