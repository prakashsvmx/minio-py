import io

import urllib3
import sys

from urllib3.exceptions import ResponseError

from minio.deleteobjects import DeleteObject

from minio import Minio

# setattr(Minio, "force_delete", force_delete)
# httpClient = urllib3.PoolManager(cert_reqs="CERT_NONE")
minio_client = Minio(
    'localhost:22000',
    access_key='minio',
    secret_key='minio123',
    region="us-west-1",
    secure=False,
    # http_client=httpClient
)
bucket_name = "test-bucket"
prefix = ""

result = minio_client.put_object(
    "test-bucket", "py-object", io.BytesIO(b"hello"), 5,
)

"""
# List objects and versions
objects_versions = minio_client.list_objects(bucket_name, prefix, include_version=True, recursive=True)

for obj in objects_versions:
    print(obj.object_name, obj.version_id, obj.size, obj.last_modified)
"""
# Construct delete_object_list with DeleteObject instances
"""
delete_object_list = [
    DeleteObject(obj.object_name, obj.version_id)
    for obj in objects_versions
]
# Delete objects
errors = minio_client.remove_objects(bucket_name, delete_object_list)
print("Deleted objects successfully:")
for error in errors:
    print("error occurred when deleting object", error)
"""

#delete_object_list = map(
#    lambda x: DeleteObject(x.object_name, x.version_id),
#    minio_client.list_objects(bucket_name, prefix, include_version=True, recursive=True),
#)
#
## Delete objects
#errors = minio_client.remove_objects(bucket_name, delete_object_list)
#print("Deleted objects successfully:")
#for error in errors:
#    print("error occurred when deleting object", error)
