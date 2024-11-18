import asyncio
from azure.servicebus.aio import ServiceBusClient
from azure.servicebus.management import ServiceBusAdministrationClient
from dotenv import load_dotenv
import os

class ServiceBusManager:
    def __init__(self, connection_str, queue_name):
        self.connection_str = connection_str
        self.queue_name = queue_name

        # Management client for administrative tasks
        self.admin_client = ServiceBusAdministrationClient.from_connection_string(connection_str)

        # Update queue lock duration
        queue_properties = self.admin_client.get_queue(queue_name)
        queue_properties.lock_duration = "PT2M"  # Set lock duration to 2 minutes
        self.admin_client.update_queue(queue_properties)

        # Async client for receiving messages
        self.client = ServiceBusClient.from_connection_string(connection_str)

    async def close(self):
        # Clean up resources
        await self.client.close()

    async def peek_and_delete_message(self, max_wait_time=5):
        async with self.client.get_queue_receiver(queue_name=self.queue_name) as receiver:
            # Receive a single message in PeekLock mode
            received_msgs = await receiver.receive_messages(max_wait_time=max_wait_time, max_message_count=1)
            
            for msg in received_msgs:
                print("Peeked message content:", str(msg))
                print("Message properties:", msg.application_properties)
                
                # Simulate processing the message
                print("Processing message...")
                await receiver.complete_message(msg)
                print("Message deleted from the queue.")

async def main():
    load_dotenv()
    connection_str = os.getenv("connection_str")
    queue_name = os.getenv("queue_name")

    sb_manager = ServiceBusManager(connection_str, queue_name)
    await sb_manager.peek_and_delete_message()
    await sb_manager.close()

asyncio.run(main())
