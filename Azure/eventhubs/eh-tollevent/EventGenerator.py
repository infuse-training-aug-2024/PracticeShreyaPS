import json
from datetime import datetime
import random

class TollEvent:
    def __init__(self, partition_id, 
                 event_processed_time, event_enqueued_time):
        
        # self.vehicleType =random.randint(1,2)
        self.vehicleType =5
        self.toll_amount = random.uniform(0.0,10.0)
        self.event_processed_time = event_processed_time
        self.partition_id = partition_id
        self.event_enqueued_time = event_enqueued_time

    def to_json(self):
        data = {
            "vehicleType":self.vehicleType,
            "tollAmount": self.toll_amount,
            "eventProcessedUtcTime": self.event_processed_time,
            "partitionId": self.partition_id,
            "eventEnqueuedUtcTime": self.event_enqueued_time
        }
        return json.dumps(data, indent=4)
 
    def to_dict(self):
        return {
            "vehicleType": self.vehicleType,
            "tollAmount": self.toll_amount,
            "eventProcessedUtcTime": self.event_processed_time,
            "partitionId": self.partition_id,
            "eventEnqueuedUtcTime": self.event_enqueued_time,
        }

