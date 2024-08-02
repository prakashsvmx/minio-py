from minio import Minio
import urllib3
from minio.credentials.providers import CertificateIdentityProvider

import ssl
context = ssl._create_unverified_context()


httpSClient = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs='/home/prakash/tmpwork/certs/public.crt')

httpCClient = urllib3.PoolManager(
    cert_file="/home/prakash/tmpwork/python-test-certs/client.crt",
    cert_reqs="CERT_REQUIRED",
    key_file="/home/prakash/tmpwork/python-test-certs/client.key",
    key_password=""
)

# STS endpoint usually point to MinIO server.
sts_endpoint = "https://localhost:22000/"

# client certificate file
cert_file = "/home/prakash/tmpwork/python-test-certs/client.crt"

# client private key
key_file = "/home/prakash/tmpwork/python-test-certs/client.key"

provider = CertificateIdentityProvider(
    sts_endpoint, cert_file=cert_file, key_file=key_file,
    http_client=httpCClient
)

client = Minio("localhost:22000", credentials=provider,  secure=True,
               cert_check=False,)

# Get information of an object.
# List objects information.
objects = client.list_objects("test-bucket")
for obj in objects:
    print(obj)