from azure.core.exceptions import (
    ResourceExistsError,
    ResourceNotFoundError
)

from azure.storage.fileshare import (
    ShareServiceClient,
    ShareClient,
    ShareDirectoryClient,
    ShareFileClient
)
from dotenv import load_dotenv
import os

class AzureFileShareManager:
    def __init__(self, connection_string):
        self.service_client = ShareServiceClient.from_connection_string(connection_string)

    def create_file_share(self, connection_string, share_name):
        try:
            share_client = ShareClient.from_connection_string(
                connection_string, share_name)

            print("Creating share:", share_name)
            share_client.create_share()

        except ResourceExistsError as ex:
            print("ResourceExistsError:", ex.message)

    def create_directory(self, connection_string, share_name, dir_name):
        try:
            dir_client = ShareDirectoryClient.from_connection_string(
                connection_string, share_name, dir_name)
            print("Creating directory:", share_name + "/" + dir_name)
            dir_client.create_directory()

        except ResourceExistsError as ex:
            print("ResourceExistsError:", ex.message)

    def upload_local_file(self, connection_string, local_file_path, share_name, dest_file_path):
        try:
            source_file = open(local_file_path, "rb")
            data = source_file.read()
            file_client = ShareFileClient.from_connection_string(
                connection_string, share_name, dest_file_path)
            print("Uploading to:", share_name + "/" + dest_file_path)
            file_client.upload_file(data)

        except ResourceExistsError as ex:
            print("ResourceExistsError:", ex.message)

        except ResourceNotFoundError as ex:
            print("ResourceNotFoundError:", ex.message)

    def list_files_and_dirs(self, connection_string, share_name, dir_name):
        try:
            print(f"Listing files in share: '{share_name}' under directory: '{dir_name}'")
            share_client = ShareClient.from_connection_string(
                connection_string, share_name)
            items = list(share_client.list_directories_and_files(dir_name))
            if not items:
                print(f"No files or directories found in '{dir_name}'.")

            for item in items:
                if item["is_directory"]:
                    print("Directory:", item["name"])
                else:
                    print("File:", dir_name + "/" + item["name"])

        except ResourceNotFoundError as ex:
            print(f"ResourceNotFoundError: {ex.message}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


    def download_azure_file(self, connection_string, share_name, dir_name, file_name):
        try:
            source_file_path = dir_name + "/" + file_name
            dest_file_name = "DOWNLOADED-" + file_name
            file_client = ShareFileClient.from_connection_string(
                connection_string, share_name, source_file_path)
            print("Downloading to:", dest_file_name)
            with open(dest_file_name, "wb") as data:
                stream = file_client.download_file()
                data.write(stream.readall())

        except ResourceNotFoundError as ex:
            print("ResourceNotFoundError:", ex.message)

    def set_file_metadata(self, connection_string, share_name, dir_name, file_name, metadata):
        try:
            file_path = dir_name + "/" + file_name
            file_client = ShareFileClient.from_connection_string(
                connection_string, share_name, file_path)
            print(f"Setting metadata for file: {file_path}")
            file_client.set_file_metadata(metadata)

        except ResourceNotFoundError as ex:
            print(f"ResourceNotFoundError: {ex.message}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def main():
    load_dotenv()
    connection_string = os.getenv("FILE_CONNECTION_STRING")
    share_name = "myfilesshare"
    dir_name = "folder1"
    dest_file_path = "folder1/downloaded_file.txt"
    local_file_path = 'C:/Users/shreya.sawant/Desktop/index.txt'
    metadata = {"author": "Shreya", "description": "Sample file share for Azure demo"}
    file_name='index.txt'
    download_filename='downloaded_file.txt'

    azure_manager = AzureFileShareManager(connection_string)
    azure_manager.create_file_share(connection_string,share_name)
    azure_manager.create_directory(connection_string,share_name,dir_name)
    azure_manager.upload_local_file(connection_string,local_file_path,share_name,dest_file_path)
    azure_manager.list_files_and_dirs(connection_string,share_name,dir_name)
    azure_manager.download_azure_file(connection_string,share_name,dir_name,download_filename)
    azure_manager.set_file_metadata(connection_string, share_name, dir_name, download_filename, metadata)


if __name__ == "__main__":
    main()
