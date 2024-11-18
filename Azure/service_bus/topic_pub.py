import asyncio
from dotenv import load_dotenv
import os
from azure.servicebus.aio import ServiceBusClient
from azure.servicebus import ServiceBusMessage

async def send_single_pass_message(sender):
    # Create a Service Bus message
    message = ServiceBusMessage("Single-pass msg",subject="single-pass")
    # send the message to the topic
    await sender.send_messages(message)
    print("Sent a single message")

async def send_double_pass_message(sender):
    # Create a Service Bus message
    message = ServiceBusMessage("double-pass msg",subject="double-pass")
    # send the message to the topic
    await sender.send_messages(message)
    print("Sent a single message")

async def run():
    load_dotenv()
    # create a Service Bus client using the connection string
    async with ServiceBusClient.from_connection_string(
        conn_str=os.getenv("NAMESPACE_CONNECTION_STR"),
        logging_enable=True) as servicebus_client:
        # Get a Topic Sender object to send messages to the topic
        sender = servicebus_client.get_topic_sender(topic_name=os.getenv("TOPIC_NAME"))
        async with sender:
            # Send one message
            await send_single_pass_message(sender)
            await send_double_pass_message(sender)

asyncio.run(run())
print("Done sending messages")
print("-----------------------")