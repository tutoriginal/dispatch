import os
from authlib.integrations.requests_client import OAuth2Session
import requests

session = OAuth2Session(
    client_id=os.getenv('API42_ID'),
    client_secret=os.getenv('API42_SECRET'),
    token_endpoint='https://api.intra.42.fr/oauth/token',
    token_endpoint_auth_method='client_secret_post',
    scope='public',
    grant_type='client_credentials',
    token={'access_token': None, 'expires_in': -100},
)


def get_subscribed(slug):
    response = session.get("https://api.intra.42.fr/v2/projects/c-piscine-final-exam/projects_users?filter[campus]=12&filter[marked]=false&page[size]=100")
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        return (None, err)

    projets_users = response.json()
    users = [pu['user']['login'] for pu in projets_users if not pu['user']['staff?']]

    return (users, None)