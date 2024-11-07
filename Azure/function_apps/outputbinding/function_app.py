import azure.functions as func
import logging
import json
from datetime import datetime

app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", path="mycontainer", connection="sablobappshreya_STORAGE")
@app.table_output(arg_name="outputTable", table_name="mytable", connection="sablobappshreya_STORAGE")
def blob_to_table(myblob: func.InputStream, outputTable: func.Out[str]):
    blob_data = myblob.read()  # Read entire blob content
    blob_size = len(blob_data)
    logging.info(f"Processing blob with Name: {myblob.name}, Size: {blob_size} kiB")

    # Define the row data as a dictionary for Table Storage
    row = {
        "PartitionKey": "BlobPartition",
        "RowKey": datetime.utcnow().isoformat(),  # Unique RowKey based on timestamp
        "BlobName": myblob.name,
        "BlobSize": blob_size
    }

    # Convert the row dictionary to a JSON string and set it as the output
    outputTable.set(json.dumps(row))

    logging.info(f"Blob trigger function processed blob: {myblob.name}")
