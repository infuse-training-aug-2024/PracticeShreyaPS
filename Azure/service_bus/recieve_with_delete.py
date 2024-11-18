import asyncio
from azure.servicebus.aio import ServiceBusClient
from azure.servicebus import ServiceBusReceiveMode
from dotenv import load_dotenv
import os

class ServiceBusManager:
    def __init__(self, connection_str, queue_name):
        self.connection_str = connection_str
        self.queue_name = queue_name
        self.client = ServiceBusClient.from_connection_string(connection_str)

    async def close(self):
        # Clean up resources
        await self.client.close()

    async def receive_and_delete_message(self, max_wait_time=5):
        async with self.client.get_queue_receiver(
            queue_name=self.queue_name,
            receive_mode=ServiceBusReceiveMode.RECEIVE_AND_DELETE
        ) as receiver:
            # Receive messages and automatically delete them from the queue
            received_msgs = await receiver.receive_messages(max_wait_time=max_wait_time, max_message_count=1)
            
            for msg in received_msgs:
                print("Received message content:", str(msg))
                print("Message properties:", msg.application_properties)
                # No need to call complete_message; it's already deleted

async def main():
    load_dotenv()
    connection_str = os.getenv("connection_str")
    queue_name = os.getenv("queue_name")

    sb_manager = ServiceBusManager(connection_str, queue_name)
    await sb_manager.receive_and_delete_message()  # Call the method
    await sb_manager.close()

asyncio.run(main())
