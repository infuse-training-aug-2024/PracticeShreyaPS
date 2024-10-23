from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, StandardBlobTier
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
import os

class AzureBlobManager:
    def __init__(self, account_name, account_key):
        connection_string = (
            f"DefaultEndpointsProtocol=https;"
            f"AccountName={account_name};"
            f"AccountKey={account_key};"
            f"EndpointSuffix=core.windows.net"
        )
        self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    def create_container(self, container_name):
        try:
            container_client = self.blob_service_client.create_container(container_name)
            print(f"Container '{container_name}' created successfully.")
            return container_client
        except Exception as e:
            print(f"Container creation failed: {e}")
            return None

    def upload_blob(self, container_name, blob_name, content):
        try:
            blob_client = self.blob_service_client.get_blob_client(container=container_name, blob=blob_name)
            blob_client.upload_blob(content, overwrite=True)
            print(f"Blob '{blob_name}' uploaded successfully.")
        except Exception as e:
            print(f"Blob upload failed: {e}")

    def upload_image_blob(self, container_name, blob_name, local_img_path):
        try:
            blob_client = self.blob_service_client.get_blob_client(container=container_name, blob=blob_name)
            with open(local_img_path, "rb") as data:
                blob_client.upload_blob(data)
            print(f"Image '{local_img_path}' uploaded to blob '{blob_name}' successfully.")
        except Exception as e:
            print(f"Failed to upload image: {e}")

    def list_blobs(self, container_name):
        try:
            container_client = self.blob_service_client.get_container_client(container_name)
            print(f"Listing blobs in container '{container_name}':")
            for blob in container_client.list_blobs():
                print(f"- {blob.name}")
        except Exception as e:
            print(f"Blob listing failed: {e}")

    def download_blob(self, container_name, blob_name, download_file_path):
        try:
            blob_client = self.blob_service_client.get_blob_client(container=container_name, blob=blob_name)
            with open(download_file_path, "wb") as download_file:
                download_file.write(blob_client.download_blob().readall())
            print(f"Blob '{blob_name}' downloaded to '{download_file_path}'.")
        except Exception as e:
            print(f"Blob download failed: {e}")

    def set_blob_metadata(self, container_name, blob_name, metadata):
        try:
            blob_client = self.blob_service_client.get_blob_client(container=container_name, blob=blob_name)
            blob_client.set_blob_metadata(metadata)
            properties = blob_client.get_blob_properties()
            print(f"Metadata added to blob '{blob_name}': {properties.metadata}")
        except Exception as e:
            print(f"Metadata operation failed: {e}")

    def set_blob_access_tier(self, container_name, blob_name, tier=StandardBlobTier.COOL):
        try:
            blob_client = self.blob_service_client.get_blob_client(container=container_name, blob=blob_name)
            blob_client.set_standard_blob_tier(tier)
            print(f"Blob '{blob_name}' access tier updated to {tier.name.lower()} successfully.")
        except Exception as e:
            print(f"Failed to update access tier: {e}")

def main():
    load_dotenv()
    account_name = os.getenv("AZURE_ACCOUNT_NAME")
    account_key = os.getenv("AZURE_ACCOUNT_KEY")
    container_name = "pythoncontainer"
    text_blob_name = "myblob.txt"
    image_blob_name = "pic"
    text_blob_content = b"Hello, this is a sample blob!"
    download_file_path = "downloaded_blob.txt"
    local_img_path = 'C:/Users/shreya.sawant/Pictures/Screenshots/Screenshot (13).png'
    metadata = {"author": "Shreya", "description": "Sample blob for Azure demo"}

    azure_manager = AzureBlobManager(account_name, account_key)
    azure_manager.create_container(container_name)
    azure_manager.upload_blob(container_name, text_blob_name, text_blob_content)
    azure_manager.upload_image_blob(container_name, image_blob_name, local_img_path)
    azure_manager.list_blobs(container_name)
    azure_manager.download_blob(container_name, text_blob_name, download_file_path)
    azure_manager.set_blob_metadata(container_name, text_blob_name, metadata)
    azure_manager.set_blob_access_tier(container_name, image_blob_name)

if __name__ == "__main__":
    main()
