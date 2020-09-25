# kedastorqueue

**//This repo is still WIP//**
KEDA is a Kubernetes-based event-driven autoscaler. KEDA determines how any container in Kubernetes should be scaled based on the number of events that need to be processed. More information on KEDA here - https://keda.sh/ <br />
A video tutorial explaining the same is here - https://www.youtube.com/watch?v=-jOVplEzypY <br />
The current project is a simple PoC to understand and demo KEDA in action.

## Project code files
The project has three directories as follows: <br />
a. **client:** This directory has a file by the name **kedastorclient.py**. This file has the code to enqueue a pre defined number of messages to the Azure Storage Queue. The Azure Storage connection string, storage queue name and the number of messages to be enqueued need to be set in this file. <br />
<br />
b. **receiver:** This directory has a file by the name **kedastorreceiver.py**. This file has the code to dequeue **one** message from the Azure Storage Queue. There is an indefinite while loop in the code just to stop the code from exiting after dequeuing the message. The Azure Storage connection string need to be set in this file along with the queue name. <br /> 
The directory also has the Dockerfile to deploy the code as a container. <br />
<br />
Source code reference for **kedastorclient.py** and **kedastorreceiver.py** taken from here - https://docs.microsoft.com/en-us/azure/storage/queues/storage-quickstart-queues-python
<br />
c. **yaml:** This directory has the deployment yaml file by the name **kedastorreceiver-deployment.yaml** for the container created from **kedastorreceiver.py**. In this deployment file, the name of the image created from **kedastorreceiver.py** and the Azure Storage connection string should be entered. <br />
Another file in this directory is by the name **scaledobject.yaml**. More information here - https://keda.sh/docs/1.5/scalers/azure-storage-queue/. Care should be taken on the following points: <br />
1. The **deploymentName** property should be set to the deployment name used in **kedastorreceiver-deployment.yaml** <br />
2. The **connection** property should be set to the name of the key which is defined as an environment variable in **kedastorreceiver-deployment.yaml**. <br />
3. The namespace of both -- the scaledobject as well as the deployment should be the same. <br />
<br />

## Azure setup
The following services need to be provisioned in Azure: <br />
1. Azure Storage Queue: I have used the name of the queue as **kedatest**. <br />
2. Azure Container Registry: To store the Docker images for the container created from **kedastorreceiver.py**. <br />
3. AKS: AKS should have KEDA deployed. Steps for the same can be found at: https://www.thinktecture.com/en/kubernetes/serverless-workloads-with-keda/serverless-workloads-with-keda/ <br /> . The container created from **kedastorreceiver.py** will be deployed here. <br />
<br />

## Flow
Executing **kedastorclient.py** will enqueue predefined number of messages to the Azure Service Bus Queue. The Scaled Object defined using **scaledobject.yaml** will scale the pods created of **kedastorreceiver.py** in the AKS based in the messages enqueued in the Azure Service Bus queue. 


  

