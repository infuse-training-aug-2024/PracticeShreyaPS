import os
import uuid
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueClient, BinaryBase64DecodePolicy, BinaryBase64EncodePolicy
from dotenv import load_dotenv

class AzureQueueManager:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def create_queue(self, queue_name):
        try:
            queue_client = QueueClient.from_connection_string(self.connection_string, queue_name)
            queue_client.create_queue()
            print(f"Queue '{queue_name}' created successfully.")
            return queue_client
        except Exception as ex:
            print(f"Exception during queue creation: {ex}")
            return None

    def send_message(self, queue_client, message):
        try:
            response = queue_client.send_message(message)
            print(f"Message '{message}' sent successfully.")
            return response
        except Exception as ex:
            print(f"Exception during message sending: {ex}")

    def peek_messages(self, queue_client, max_messages=5):
        try:
            peeked_messages = queue_client.peek_messages(max_messages=max_messages)
            for msg in peeked_messages:
                print(f"Peeked Message: {msg.content}")
            return peeked_messages
        except Exception as ex:
            print(f"Exception during peeking messages: {ex}")

    def receive_messages(self, queue_client, max_messages=5):
        try:
            messages = queue_client.receive_messages(max_messages=max_messages,visibility_timeout=30)
            for msg in messages:
                print(f"Received Message: {msg.content}")
                queue_client.delete_message(msg)
            return messages
        except Exception as ex:
            print(f"Exception during receiving messages: {ex}")

def main():
    load_dotenv()  
    connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    if not connection_string:
        print("Azure Storage connection string not found. Please check your environment variables.")
        return
    azure_manager = AzureQueueManager(connection_string)
    queue_name = f"queue-{uuid.uuid4()}"
    queue_client = azure_manager.create_queue(queue_name)
    if not queue_client:
        return  
    azure_manager.send_message(queue_client, "First message")
    azure_manager.send_message(queue_client, "Second message")
    azure_manager.send_message(queue_client, "Third message")
    print("\nPeeking at messages in the queue...")
    azure_manager.peek_messages(queue_client)
    print("\nReceiving messages from the queue...")
    azure_manager.receive_messages(queue_client)
    azure_manager.peek_messages(queue_client)
    azure_manager.send_message(queue_client, "after 1 to 3 are recieved message")
    azure_manager.peek_messages(queue_client)

if __name__ == "__main__":
    main()
