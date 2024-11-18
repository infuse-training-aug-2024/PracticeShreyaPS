import asyncio
from dotenv import load_dotenv
import os
from azure.servicebus.aio import ServiceBusClient
from azure.servicebus import ServiceBusMessage
from azure.servicebus import ServiceBusReceiveMode  # Correct import for ReceiveMode
from datetime import timedelta

class ServiceBusManager:
    def __init__(self, connection_str, queue_name):
        self.connection_str = connection_str
        self.queue_name = queue_name
        self.client = ServiceBusClient.from_connection_string(connection_str)

    async def close(self):
        # Clean up resources
        await self.client.close()

    async def send_single_message(self, message_text):
        async with self.client.get_queue_sender(queue_name=self.queue_name) as sender:
            message = ServiceBusMessage(message_text, time_to_live=timedelta(minutes=10))
            await sender.send_messages(message)
            print(f"Sent a single message: {message_text}")

    async def send_list_of_messages(self, messages_text):
        async with self.client.get_queue_sender(queue_name=self.queue_name) as sender:
            messages = [ServiceBusMessage(text, time_to_live=timedelta(seconds=20)) for text in messages_text]
            await sender.send_messages(messages)
            print(f"Sent a list of {len(messages)} messages")

    async def send_batch_message(self, message_text, count):
        async with self.client.get_queue_sender(queue_name=self.queue_name) as sender:
            batch_message = await sender.create_message_batch()
            for _ in range(count):
                try:
                    batch_message.add_message(ServiceBusMessage(message_text, time_to_live=timedelta(minutes=2)))
                except ValueError:
                    break
            await sender.send_messages(batch_message)
            print(f"Sent a batch of {count} messages")


async def receive_and_delete_message(self, max_wait_time=5):
    async with self.client.get_queue_receiver(
        queue_name=self.queue_name, 
        receive_mode=ServiceBusReceiveMode.RECEIVE_AND_DELETE
    ) as receiver:
        # Receive messages and automatically delete them from the queue
        received_msgs = await receiver.receive_messages(max_wait_time=max_wait_time, max_message_count=3)
        
        for msg in received_msgs:
            print("Received message content:", str(msg))
            print("Message properties:", msg.application_properties)


async def main():
    load_dotenv()
    connection_str = os.getenv("connection_str")
    queue_name = os.getenv("queue_name")
    
    sb_manager = ServiceBusManager(connection_str, queue_name)

    # Sending messages
    await sb_manager.send_single_message("message 1")
    await sb_manager.send_single_message("message2")
    await sb_manager.send_single_message("message3")
    await sb_manager.send_single_message("message 1")
    await sb_manager.send_single_message("message2")
    await sb_manager.send_single_message("message3")
    await sb_manager.send_single_message("message 33")
    await sb_manager.send_list_of_messages(["Message in list"] * 5)
    await sb_manager.send_batch_message("Message inside a ServiceBusMessageBatch", 6)
    print("Done sending messages")
    print("-----------------------")

    # Receiving messages
    await sb_manager.receive_and_delete_message()
    print("Done receiving messages")
    print("-----------------------")

    # Close the ServiceBusManager client
    await sb_manager.close()


asyncio.run(main())
