import asyncio
from dotenv import load_dotenv
import os
from azure.servicebus.aio import ServiceBusClient
from azure.servicebus import ServiceBusMessage
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
            message = ServiceBusMessage(message_text, time_to_live=timedelta(minutes=2))
            await sender.send_messages(message)
            print(f"Sent a single message: {message_text}")

    async def receive_and_process_messages(self, max_wait_time=5, max_message_count=2, retries=5):
        async with self.client.get_queue_receiver(queue_name=self.queue_name) as receiver:
            received_msgs = await receiver.receive_messages(max_wait_time=max_wait_time, max_message_count=max_message_count)
            for msg in received_msgs:
                retry_count = 0
                success = False

                while retry_count < retries:
                    try:
                        print(f"Processing message:{str(msg)}")
                        # Simulate message processing
                        if str(msg) == "success":
                            success = True
                            break
                        if str(msg)=="fail":  # Simulating failure for all but last retry
                            raise Exception(" processing failure")
                        
                    except Exception as e:
                        retry_count += 1
                        success=False
                        print(f"Error processing message. Retrying {retry_count}/{retries}. Error: {e}")

                if success:
                    await receiver.complete_message(msg)
                    print("Message processed and deleted from the queue.")
                else:
                    await receiver.dead_letter_message(msg, reason="ProcessingFailed", error_description="Max retries exceeded.")
                    print("Message moved to Dead-letter Queue (DLQ).")

async def main():
    load_dotenv()
    connection_str = os.getenv("connection_str")
    queue_name = os.getenv("queue_name")
    
    sb_manager = ServiceBusManager(connection_str, queue_name)

    # Sending messages for testing
    await sb_manager.send_single_message("fail")
    await sb_manager.send_single_message("success")

    # Receiving and processing messages
    await sb_manager.receive_and_process_messages()
    print("Done receiving and processing messages.")
    print("-----------------------")

    # Close the ServiceBusManager client
    await sb_manager.close()


asyncio.run(main())
