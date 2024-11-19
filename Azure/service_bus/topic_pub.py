import asyncio
from dotenv import load_dotenv
import os
from azure.servicebus.aio import ServiceBusClient
from azure.servicebus import ServiceBusMessage

async def send_blue_msg(sender):
    # Create a Service Bus message
    message = ServiceBusMessage("blue10 msg",application_properties={"color": "blue", "quantity":10})
    # send the message to the topic
    await sender.send_messages(message)
    print("Sent a single message")

async def send_red_msg(sender):
    # Create a Service Bus message
    message = ServiceBusMessage("red msg",application_properties={"color": "red"})
    # send the message to the topic
    await sender.send_messages(message)
    print("Sent a single message")

async def send_single_pass_msg(sender):
    # Create a Service Bus message
    message = ServiceBusMessage("single pass msg",subject="single-pass")
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
            await send_blue_msg(sender)
            await send_red_msg(sender)
            await send_single_pass_msg(sender)

asyncio.run(run())
print("Done sending messages")
print("-----------------------")