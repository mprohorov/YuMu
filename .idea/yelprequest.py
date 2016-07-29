from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

auth = Oauth1Authenticator(
    consumer_key= aVn_cvZHTR0jtcjDRXRJwg,
    consumer_secret= aTa6NM4DhPIMz-gUwM8Ho9A6iys,
    token= PzLbagX1Jzpwx-k7Hk2Dbrpf36u13qmP,
    token_secret= zbM8XKYLTVDOrCkYbuN-ao5280
)

client = Client(auth)