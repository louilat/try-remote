from web3 import Web3
import boto3
import pandas as pd
from requests import get
import io
import os

print("Hello World !!")
print("Starting job...")

ACCESS_KEY = os.environ["ACCESS_KEY"]
SECRET_KEY = os.environ["SECRET_KEY"]
TOKEN = os.environ["TOKEN"]
IP_ADDRESS = os.environ["IPA"]

print(IP_ADDRESS)

# w3 = Web3(Web3.HTTPProvider(IP_ADDRESS))

# print("Is connected: ", w3.is_connected())

# block_number = w3.eth.get_block_number()

# df = pd.DataFrame({
#     "col1": [block_number]
# })

# buffer = io.StringIO()

# df.to_csv(buffer, index=False)

# s3_client = boto3.client(
#     "s3",
#     endpoint_url = 'https://'+'minio.lab.sspcloud.fr',
#     aws_access_key_id=ACCESS_KEY,
#     aws_secret_access_key=SECRET_KEY,
#     aws_session_token=TOKEN,
# )

# s3_client.put_object(
#     Body=buffer.getvalue(),
#     Bucket="llatournerie",
#     Key="exp-remote/data.csv"
# )


# ip = get('https://api.ipify.org').content.decode('utf8')
# print('My public IP address is: {}'.format(ip))

# print("Success")