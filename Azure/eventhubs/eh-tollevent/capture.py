import os
import string
import json
import uuid
import avro.schema
from dotenv import load_dotenv

from azure.storage.blob import ContainerClient, BlobClient
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

def processBlob2(filename):
    reader= DataFileReader(open(filename, 'rb'),DatumReader())
    dict ={}
    for reading in reader:
        schema = reader.datum_reader.writer_schema
        print(f"Debug: Avro Schema: {schema}")

        parsed_json=json.loads(reading["Body"])
        if not 'id' in parsed_json:
            return
        if not parsed_json['id'] in dict:
            list=[]
            dict[parsed_json['id']]=list
        else:
            list=dict[parsed_json['id']]
            list.append(parsed_json)
    reader.close()
    for device in dict.keys():
        filename=os.getcwd() + '\\' + str(device) + '.csv'
        deviceFile=open(filename,"a")
        for r in dict[device]:
            deviceFile.write(", ".join([str(r[x]) for x in r.keys()])+'\n')


def startProcessing():
    load_dotenv()
    blob_storage_conn_str=os.getenv("BLOB_STORAGE_CONNECTION_STR")
    capture_container=os.getenv("capture_container")
    print("Processor started using path:" + os.getcwd())
    container =ContainerClient.from_connection_string(blob_storage_conn_str,container_name=capture_container)
    blob_list=container.list_blobs()
    for blob in blob_list:
        if blob.size>508:
            print("downloaded a non empty blob: "+blob.name)
            blob_client= ContainerClient.get_blob_client(container,blob=blob.name)
            cleanName =str.replace(blob.name,'/','_')
            cleanName= os.getcwd() + '\\' +cleanName
            with open(cleanName,"wb+") as my_file:
                my_file.write(blob_client.download_blob().readall())
            processBlob2(cleanName)
            os.remove(cleanName)
            container.delete_blob(blob.name)





startProcessing()