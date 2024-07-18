### AuthSDK for News APP Project - Python API Client

# Description:

This Python SDK streamlines authentication and interaction with an API using OAuth 2.0 client credentials grant. It simplifies sending GET, POST requests and handles JSON data serialization.

# Installation:

Clone this repository or download the source code.
Install dependencies using pip install requests requests-oauthlib.
Usage:

# Import the AuthSDK class:

from mysdk import MySDK

# Initialize the SDK with your client ID and secret:


client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"

sdk = AuthSDK(client_id, client_secret)


### Use the provided methods to interact with the API:

# Get data from an endpoint
data = sdk.get("/users")

# Send data to an endpoint
data = {"name": "John Doe"}
response = sdk.post("/users", data=data)
