from azure.cosmos import CosmosClient
from django.conf import settings

client = CosmosClient(settings.COSMOS_ENDPOINT, credential=settings.COSMOS_KEY)
database = client.get_database_client(settings.COSMOS_DATABASE_NAME)
container = database.get_container_client(settings.COSMOS_CONTAINER_NAME)
