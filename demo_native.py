from auth_native import *
import requests
import os

auth = Authentication()

def get_account_extensions(access_token):
    endpoint = "/restapi/v1.0/account/~/extension";
    url = os.getenv("RC_SERVER_URL") + endpoint
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + access_token
        }

    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        print res._content
    else:
        print res.status_code

try:
    access_token = auth.get_token()
    get_account_extensions(access_token)
except Exception as e:
    print (e)
