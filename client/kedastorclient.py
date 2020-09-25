import os, uuid
from azure.storage.queue import QueueServiceClient, QueueClient, QueueMessage

# Storage connection string
storconnstring = "<>"
queue_name = "kedatest"

#Number of messages to be enqueued in the storage queue
msgcnt = 3

queue_client = QueueClient.from_connection_string(storconnstring, queue_name)

# Send a test message to the queue
for ctr in range(msgcnt):
  msg = "Keda Test Message "+ str(ctr)
  queue_client.send_message(msg)

