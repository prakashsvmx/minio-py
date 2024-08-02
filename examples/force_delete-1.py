import urllib3
import sys
import asyncio
from minio.deleteobjects import DeleteObject
from minio import Minio



# setattr(Minio, "force_delete", force_delete)
#httpClient = urllib3.PoolManager(cert_reqs="CERT_NONE")
minioClient = Minio(
    'localhost:22000',
    access_key='test-user',
    secret_key='minio123',
    secure=False,
    # http_client=httpClient
)
bucket="test-bucket"
prefix=""

object_instances = minioClient.list_objects(bucket, '/', include_version=True)
arr = [item async for item in object_instances]
print(arr)
