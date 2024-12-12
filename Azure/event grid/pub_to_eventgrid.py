from azure.eventgrid import EventGridPublisherClient
from azure.core.credentials import AzureKeyCredential
from datetime import datetime
import uuid  
import datetime
import os

TOPIC_ENDPOINT = "https://mytopic-shreya.uksouth-1.eventgrid.azure.net/api/events"
ACCESS_KEY = "6pipeeFJAnFhA5JfTaBhefiAYU3vl63a14xC9YkYA8UrGotToB1JJQQJ99ALACmepeSXJ3w3AAABAZEGWH03"

client = EventGridPublisherClient(TOPIC_ENDPOINT, AzureKeyCredential(ACCESS_KEY))

unique_id = str(uuid.uuid4())

order_created_event_payload =     {
        "id": unique_id,  
        "eventType": "OrderCreated", 
        "subject": "/orders/123",  
        "data": {  
            "orderId": "123",
            "product": "Laptop",
            "quantity": 1,
            "severity": "High"  
        },
        "eventTime": datetime.datetime.now(datetime.UTC), 
        "dataVersion": "1.0"  
    }

order_delivered_event_payload =     {
        "id": unique_id, 
        "eventType": "OrderCreated", 
        "subject": "/delivery/123",  
        "data": { 
            "orderId": "456",
            "product": "Laptop",
            "quantity": 1,
            "severity": "normal"  
        },
        "eventTime": datetime.datetime.now(datetime.UTC), 
        "dataVersion": "1.0"  
    }

urgent_order_created_event_payload = [
    {
        "id": unique_id, 
        "eventType": "OrderCreated",  
        "subject": "/orders/123",  
        "data": { 
            "orderId": "456",
            "product": "Laptop",
            "quantity": 1,
            "severity": "High"  
        },
        "eventTime": datetime.datetime.now(datetime.UTC), 
        "dataVersion": "1.0" 
    }
]
order_cancelled_event_payload = [
    {
        "id": unique_id, 
        "eventType": "OrderCancelled",  
        "subject": "/orders/123",  
        "data": { 
            "orderId": "789",
            "product": "Laptop",
            "quantity": 1,
            "severity": "normal"  
        },
        "eventTime": datetime.datetime.now(datetime.UTC),  
        "dataVersion": "1.0"  
    }
]

# Publish the event
try:
    client.send(order_created_event_payload)
    client.send(order_delivered_event_payload)
    client.send(order_cancelled_event_payload)
    client.send(urgent_order_created_event_payload)
    print("Events published successfully with ID:")
except Exception as e:
    print(f"An error occurred: {e}")
