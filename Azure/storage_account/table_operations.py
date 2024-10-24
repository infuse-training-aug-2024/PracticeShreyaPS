from azure.data.tables import TableServiceClient, TableClient, UpdateMode
from azure.core.exceptions import ResourceExistsError, ResourceNotFoundError
import os
from dotenv import load_dotenv

class AzureTableManager:
    def __init__(self, sas_token, account_name):
        # Construct the service URL using account name and SAS token
        self.service_client = TableServiceClient(
            endpoint=f"https://{account_name}.table.core.windows.net",
            credential=sas_token
        )

    def create_table(self, table_name):
        try:
            print(f"Creating table: {table_name}")
            table_client = self.service_client.create_table(table_name)
            print(f"Table '{table_name}' created successfully.")
            return table_client
        except ResourceExistsError:
            print(f"Table '{table_name}' already exists.")

    def insert_entity(self, table_name, entity):
        try:
            table_client = self.service_client.get_table_client(table_name)
            table_client.create_entity(entity)
            print(f"Entity inserted into '{table_name}': {entity}")
        except Exception as e:
            print(f"Failed to insert entity: {e}")

    def query_entities(self, table_name, filter_query=None):
        try:
            table_client = self.service_client.get_table_client(table_name)
            print(f"Querying entities from table '{table_name}':")
            entities = table_client.list_entities(filter=filter_query)
            for entity in entities:
                print(entity)
        except Exception as e:
            print(f"Failed to query entities: {e}")

    def update_entity(self, table_name, entity):
        try:
            table_client = self.service_client.get_table_client(table_name)
            table_client.update_entity(entity, mode=UpdateMode.REPLACE)
            print(f"Entity updated in '{table_name}': {entity}")
        except ResourceNotFoundError:
            print("Entity not found.")
        except Exception as e:
            print(f"Failed to update entity: {e}")

    def delete_entity(self, table_name, partition_key, row_key):
        try:
            table_client = self.service_client.get_table_client(table_name)
            table_client.delete_entity(partition_key, row_key)
            print(f"Entity with PartitionKey='{partition_key}' and RowKey='{row_key}' deleted.")
        except ResourceNotFoundError:
            print("Entity not found.")
        except Exception as e:
            print(f"Failed to delete entity: {e}")

    def delete_table(self, table_name):
        try:
            print(f"Deleting table: {table_name}")
            self.service_client.delete_table(table_name)
            print(f"Table '{table_name}' deleted successfully.")
        except ResourceNotFoundError:
            print("Table not found.")
        except Exception as e:
            print(f"Failed to delete table: {e}")

def main():
    # Load environment variables
    load_dotenv()
    sas_token = os.getenv("TABLE_SAS_TOKEN")
    account_name = os.getenv("AZURE_ACCOUNT_NAME")
    
    table_name = "SampleTable"
    partition_key = "pk1"
    row_key = "rk1"

    # Define a sample entity
    entity = {
        "PartitionKey": partition_key,
        "RowKey": row_key,
        "Name": "Shreya",
        "Age": 25,
        "Location": "India"
    }

    # Initialize the Azure Table Manager
    azure_table_manager = AzureTableManager(sas_token, account_name)

    # Perform CRUD operations
    azure_table_manager.create_table(table_name)
    azure_table_manager.insert_entity(table_name, entity)
    azure_table_manager.query_entities(table_name)
    
    # Update the entity
    entity["Age"] = 26
    azure_table_manager.update_entity(table_name, entity)
    
    # Query again to verify update
    azure_table_manager.query_entities(table_name)

    # Delete the entity
    azure_table_manager.delete_entity(table_name, partition_key, row_key)

    # Delete the table
    azure_table_manager.delete_table(table_name)

if __name__ == "__main__":
    main()
