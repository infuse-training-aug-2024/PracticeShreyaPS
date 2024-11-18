import asyncio
from dotenv import load_dotenv
import os
from azure.servicebus.aio import ServiceBusClient

SUBSCRIPTION_NAME = "panjim"

async def run():
    load_dotenv()
    # create a Service Bus client using the connection string
    async with ServiceBusClient.from_connection_string(
        conn_str=os.getenv("NAMESPACE_CONNECTION_STR"),
        logging_enable=True) as servicebus_client:

        async with servicebus_client:
            # get the Subscription Receiver object for the subscription
            receiver = servicebus_client.get_subscription_receiver(topic_name=os.getenv("TOPIC_NAME"), 
            subscription_name=SUBSCRIPTION_NAME, max_wait_time=5)
            async with receiver:
                received_msgs = await receiver.receive_messages(max_wait_time=5, max_message_count=20)
                for msg in received_msgs:
                    print("Received: " + str(msg))
                    # complete the message so that the message is removed from the subscription
                    await receiver.complete_message(msg)

asyncio.run(run())