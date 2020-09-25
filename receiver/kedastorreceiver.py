import os, uuid
from azure.storage.queue import QueueServiceClient, QueueClient, QueueMessage

#Storage connection string
storconnstring = "<>"
queue_name = "kedatest"

queue_client = QueueClient.from_connection_string(storconnstring, queue_name)

messages = queue_client.receive_messages()

for msg in messages:
  print("Message is: ", flush=True)
  print(msg.content, flush=True)
  queue_client.delete_message(msg)
  break

while True:
  aa = 999



