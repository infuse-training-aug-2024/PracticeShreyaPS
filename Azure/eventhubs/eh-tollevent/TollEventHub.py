import asyncio
import os
import json
from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient, EventHubConsumerClient
from azure.eventhub.extensions.checkpointstoreblobaio import BlobCheckpointStore
from dotenv import load_dotenv
from azure.storage.blob.aio import BlobServiceClient
from datetime import datetime
from EventGenerator import TollEvent  

class EventHubHandler:
    def __init__(self):
        load_dotenv()
        self.connection_str = os.getenv("EVENT_HUB_CONNECTION_STR")
        self.event_hub_name = os.getenv("EVENT_HUB_NAME")
        self.blob_storage_conn_str = os.getenv("BLOB_STORAGE_CONNECTION_STR")
        self.blob_container_name = os.getenv("BLOB_CONTAINER_NAME")
        self.type_1_checkpointstore=os.getenv("type_1_checkpointstore")
        self.type_2_checkpointstore=os.getenv("type_2_checkpointstore")
        self.type_1_vehicle_storage=os.getenv("type_1_vehicle_storage")
        self.type_2_vehicle_storage=os.getenv("type_2_vehicle_storage")

        self.producer = EventHubProducerClient.from_connection_string(
            conn_str=self.connection_str, eventhub_name=self.event_hub_name
        )

        self.checkpoint_store1 = BlobCheckpointStore.from_connection_string(
            self.blob_storage_conn_str, self.type_1_checkpointstore
        )
        self.checkpoint_store2 = BlobCheckpointStore.from_connection_string(
            self.blob_storage_conn_str, self.type_2_checkpointstore
        )

        self.consumer_group = "$Default"
        self.consumer1 = self._create_consumer(self.consumer_group, self.checkpoint_store1)
        self.consumer2 = self._create_consumer(self.consumer_group, self.checkpoint_store2)

    def _create_consumer(self, consumer_group, consumer_checkpoint_store):
        return EventHubConsumerClient.from_connection_string(
            self.connection_str,
            consumer_group=consumer_group,
            eventhub_name=self.event_hub_name,
            checkpoint_store=consumer_checkpoint_store,
        )

    async def send_event(self, toll_event: TollEvent, partition_key: str):
        async with self.producer:
            event_data_json = toll_event.to_json()
            event_data_batch = await self.producer.create_batch(partition_key=partition_key)
            event_data_batch.add(EventData(event_data_json))
            await self.producer.send_batch(event_data_batch)
            print(f"Event '{event_data_json}' sent to partition with key '{partition_key}'")

    async def _process_event(self, partition_context, event, partition_id):
        event_data = event.body_as_str(encoding="UTF-8")
        print(f"Received event: '{event_data}' from partition: '{partition_context.partition_id}'")

        toll_event_data = json.loads(event_data)
        toll_event = TollEvent(
            partition_id=partition_context.partition_id,
            event_processed_time=toll_event_data["eventProcessedUtcTime"],
            event_enqueued_time=toll_event_data["eventEnqueuedUtcTime"],
        )
        toll_event.vehicleType = toll_event_data["vehicleType"]
        toll_event.toll_amount = toll_event_data["tollAmount"]

        await self._save_event_to_blob_storage(toll_event, partition_context, event)

        await partition_context.update_checkpoint(event)
        print(f"Processed event: {toll_event.to_json()}")

    async def _save_event_to_blob_storage(self, toll_event, partition_context, event):
        if partition_context.partition_id in ["2"]:
            blob_service_client = BlobServiceClient.from_connection_string(self.blob_storage_conn_str)
            blob_client = blob_service_client.get_blob_client(
                container=self.type_1_vehicle_storage,
                blob=f"partition-{partition_context.partition_id}-event-{event.sequence_number}.json"
            )
            await blob_client.upload_blob(json.dumps(toll_event.to_dict()).encode("utf-8"), overwrite=True)
            print(f"Event from partition {partition_context.partition_id} saved to blob storage.")

        if partition_context.partition_id in ["3"]:
            blob_service_client = BlobServiceClient.from_connection_string(self.blob_storage_conn_str)
            blob_client = blob_service_client.get_blob_client(
                container=self.type_2_vehicle_storage,
                blob=f"partition-{partition_context.partition_id}-event-{event.sequence_number}.json"
            )
            await blob_client.upload_blob(json.dumps(toll_event.to_dict()).encode("utf-8"), overwrite=True)
            print(f"Event from partition {partition_context.partition_id} saved to blob storage.")

    async def on_event_consumer1(self, partition_context, event):
        await self._process_event(partition_context, event, "2")

    async def on_event_consumer2(self, partition_context, event):
        await self._process_event(partition_context, event, "3")

    async def receive_events(self):
        print("hiiii recieving now")

        async with self.consumer2:
            print("Starting to receive events...")
            await self.consumer2.receive(
                on_event=self.on_event_consumer2,
                starting_position="-1",
            )

        async with self.consumer1:
            print("Starting to receive events...")
            await self.consumer2.receive(
                on_event=self.on_event_consumer1,
                starting_position="-1",
            )

    async def run(self):
        toll_event1 = TollEvent(
            partition_id="2",
            event_processed_time=datetime.utcnow().isoformat(),
            event_enqueued_time=datetime.utcnow().isoformat()
        )
        toll_event2 = TollEvent(
            partition_id="3",
            event_processed_time=datetime.utcnow().isoformat(),
            event_enqueued_time=datetime.utcnow().isoformat()
        )

        # Send events
        await self.send_event(toll_event1, partition_key="type1")
        await self.send_event(toll_event2, partition_key="type2")

        # Start receiving events
        await self.receive_events()


if __name__ == "__main__":
    handler = EventHubHandler()
    asyncio.run(handler.run())
