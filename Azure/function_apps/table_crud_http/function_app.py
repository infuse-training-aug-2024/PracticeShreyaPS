import logging
import os
import azure.functions as func
from azure.data.tables import TableServiceClient
from flask import Flask, request

# Initialize Flask app
app = Flask(__name__)

# Initialize the Table Service Client with the connection string from environment variables
connection_string = os.getenv("AzureWebJobsStorage")
table_service_client = TableServiceClient.from_connection_string(connection_string)
table_name = "mytable"  # Replace this with your actual table name

@app.route("/table_crud_func", methods=["GET", "POST", "PUT", "DELETE"])
def table_crud_func(req:func.HttpResponse ) -> func.HttpResponse:
    logging.info("Received request for Table Storage operations.")
    
    # Extract operation type and keys from query parameters
    operation = request.args.get("operation")
    partition_key = request.args.get("partitionKey")
    row_key = request.args.get("rowKey")
    
    # Ensure that required parameters are provided
    if not partition_key or not row_key:
        return func.HttpResponse("PartitionKey and RowKey must be provided.", status_code=400)

    # Get the table client for the specified table
    table_client = table_service_client.get_table_client(table_name)

    try:
        if operation == "create":
            # CREATE Operation
            entity = request.get_json()
            entity["PartitionKey"] = partition_key
            entity["RowKey"] = row_key
            table_client.create_entity(entity)
            return func.HttpResponse("Entity created successfully.", status_code=201)

        elif operation == "read":
            # READ Operation
            entity = table_client.get_entity(partition_key, row_key)
            return func.HttpResponse(f"Entity found: {entity}", status_code=200)

        elif operation == "update":
            # UPDATE Operation using replace
            entity = request.get_json()
            entity["PartitionKey"] = partition_key
            entity["RowKey"] = row_key
            # Replace the entire entity with the new data
            table_client.update_entity(entity, mode='replace')  # Use 'replace' as mode
            return func.HttpResponse("Entity updated successfully.", status_code=200)

        elif operation == "delete":
            # DELETE Operation
            table_client.delete_entity(partition_key, row_key)
            return func.HttpResponse("Entity deleted successfully.", status_code=200)

        else:
            return func.HttpResponse("Invalid operation specified.", status_code=400)

    except Exception as e:
        # Handle specific exceptions for clarity
        if "ResourceNotFound" in str(e):
            return func.HttpResponse(f"Entity not found: {str(e)}", status_code=404)
        else:
            return func.HttpResponse(f"An error occurred: {str(e)}", status_code=500)
