import asyncio
from azure.servicebus.aio import ServiceBusClient
from dotenv import load_dotenv
import os

# Azure Service Bus configuration
load_dotenv()
CONNECTION_STRING = os.getenv("connection_str")
QUEUE_NAME = os.getenv("queue_name")

async def show_msg_props_without_deleting():
    async with ServiceBusClient.from_connection_string(conn_str=CONNECTION_STRING) as servicebus_client:
        
        async with servicebus_client.get_queue_receiver(queue_name=QUEUE_NAME) as receiver:
            
            messages = await receiver.peek_messages(max_message_count=10)  
            
            for message in messages:
                print(f"Message ID: {message.message_id}")
                print(f"Content: {message.body.decode() if hasattr(message.body, 'decode') else message.body}")
                print(f"Properties: {message.application_properties}")
                print("-" * 30)

if __name__ == "__main__":
    asyncio.run(show_msg_props_without_deleting())
