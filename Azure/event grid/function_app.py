import logging
import azure.functions as func
from azure.data.tables import TableServiceClient, TableEntity
import uuid 
import os


app = func.FunctionApp()


@app.event_grid_trigger(arg_name="azeventgrid")
def EventGridTrigger(azeventgrid: func.EventGridEvent):
    CONNECTION_STRING = "BlobEndpoint=https://sashrey.blob.core.windows.net/;QueueEndpoint=https://sashrey.queue.core.windows.net/;FileEndpoint=https://sashrey.file.core.windows.net/;TableEndpoint=https://sashrey.table.core.windows.net/;SharedAccessSignature=sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2024-12-11T13:59:13Z&st=2024-12-11T05:59:13Z&spr=https&sig=au97thlpV%2FWUg0dbVa%2FYRKpvUc%2FF48a1fvCy3ouUYfQ%3D"
    TABLE_NAME = "dataTable"
    table_service_client = TableServiceClient.from_connection_string(CONNECTION_STRING)
    
    logging.info('Python EventGrid trigger processed an event')

    event_data = azeventgrid.get_json()
    
    logging.info(f"Received event: {event_data}")
    
    # Accessing event data
    order_id = str(event_data.get("orderId"))
    product = str(event_data.get("product"))
    quantity = str(event_data.get("quantity"))
    severity = str(event_data.get("severity", "normal"))
    
    # Log event data
    logging.info(f"OrderId: {order_id}")
    logging.info(f"Product: {product}")
    logging.info(f"Quantity: {quantity}")
    logging.info(f"Severity: {severity}")

    table_client = table_service_client.get_table_client(TABLE_NAME)


    entity = {
        'PartitionKey':str(uuid.uuid4()),  
        'RowKey':str(uuid.uuid4()),            
        'OrderId': order_id,
        'Product': product,
        'Quantity':quantity,
        'Severity': severity
    }


    try:
        table_client.create_entity(entity=entity)
        logging.info('Entity inserted successfully.')
    except Exception as e:
        logging.error(f'Error inserting entity: {str(e)}')


