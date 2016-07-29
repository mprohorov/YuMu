import io
import json

import rauth as rauth
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator


def get_results(params):
    # Obtain these from Yelp's manage access page
    consumer_key = "aVn_cvZHTR0jtcjDRXRJwg"
    consumer_secret = "aTa6NM4DhPIMz-gUwM8Ho9A6iys"
    token = "PzLbagX1Jzpwx-k7Hk2Dbrpf36u13qmP"
    token_secret = "5zbM8XKYLTVDOrCkYbuN-ao5280"

    session = rauth.OAuth1Session(
        consumer_key=consumer_key
        , consumer_secret=consumer_secret
        , access_token=token
        , access_token_secret=token_secret)

    request = session.get("http://api.yelp.com/v2/search", params=params)

    # Transforms the JSON API response into a Python dictionary
    data = request.json()
    session.close()

    return data

params = {
    'term': 'food',
    'location': 'San Francisco',
    'lang': 'eng'
}
print(get_results(params))

"""
# read API keys
with open('config_secret.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)
"""