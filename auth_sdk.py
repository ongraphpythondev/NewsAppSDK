import requests
from requests_oauthlib import OAuth2Session

class AuthSDK:
    """
    A Python SDK for interacting with an API using OAuth 2.0 client credentials grant.

    Args:
        client_id (str): The client ID for the OAuth application.
        client_secret (str): The client secret for the OAuth application.
        base_url (str, optional): The base URL of the API. Defaults to "https://api.example.com".
    """
    def __init__(self, client_id, client_secret, base_url="https://api.crene.com/"):
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = base_url
        self.token = None

    def authenticate(self):
        """
        Obtains an OAuth 2.0 access token using client credentials grant.
        """
        client = OAuth2Session(self.client_id, scope=["api"])
        token = client.fetch_token(
            token_url="https://api.crene.com/token",
            client_secret=self.client_secret,
            client_id=self.client_id
        )
        self.token = token

    def request(self, method, endpoint, data=None, params=None, headers=None):
        if not self.token:
            self.authenticate()

        url = f"{self.base_url}/{endpoint}"
        client = OAuth2Session(self.client_id, token=self.token)
        response = client.request(method, url, json=data, params=params, headers=headers)

        if response.status_code >= 400:
            raise Exception(f"API Error: {response.text}")

        return response.json()

    def get(self, endpoint, params=None, headers=None, timeout=None):
        """
        Sends a GET request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint path.
            params (dict, optional): Query parameters. Defaults to None.
            headers (dict, optional): Custom headers. Defaults to None.
            timeout (float, optional): Request timeout in seconds. Defaults to None.

        Returns:
            dict: The JSON response from the API.

        Raises:
            Exception: If the API request fails or returns an error.
        """
        return self.request("GET", endpoint, params=params, headers=headers, timeout=timeout)

    def post(self, endpoint, data=None, json=None, headers=None, timeout=None):
        """
        Sends a POST request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint path.
            data (dict or bytes, optional): Data to be sent in the request body. Defaults to None.
            json (dict, optional): JSON data to be sent in the request body. Defaults to None.
            headers (dict, optional): Custom headers. Defaults to None.
            timeout (float, optional): Request timeout in seconds. Defaults to None.

        Returns:
            dict: The JSON response from the API.

        Raises:
            Exception: If the API request fails or returns an error.
        """
        return self.request("POST", endpoint, data=data, json=json, headers=headers, timeout=timeout)
