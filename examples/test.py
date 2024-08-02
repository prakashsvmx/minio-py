from minio import Minio

client = Minio(
    access_key="minio",
    secret_key="minio123",
    secure=False,
    endpoint="localhost:9000"
)

objectList =client.list_objects("test-v-bucket" ,recursive=True )
for obj in objectList:
    print("object----")
    print(obj)


