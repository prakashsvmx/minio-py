# -*- coding: utf-8 -*-
# MinIO Python Library for Amazon S3 Compatible Cloud Storage,
# (C) 2015 MinIO, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import io

from minio import Minio
from minio.commonconfig import Tags

client = Minio(
    'localhost:22000',
    access_key='minio',
    secret_key='minio123',
    secure=False,
)

# if client.bucket_exists("my-bucket"):
#     print("my-bucket exists")
# else:
#     client.make_bucket("my-bucket")
#     print("my-bucket created")
#
# objectList =client.list_objects("my-bucket" ,recursive=True )
# for obj in objectList:
#     print("object----")
#     print(vars(obj))
#

# Upload data.
tags = Tags(for_object=True)
tags["User"] = "jsmith"
result = client.put_object(
    "public-bucket", "2.txt", io.BytesIO(b"hello"), 5,
    tags=tags,
)



print(
    "created {0} object; etag: {1}, version-id: {2}".format(
        result.object_name, result.etag, result.version_id,
    ),
)
