from rc_authenticate import *

auth = RC_Authentication()

def get_account_extensions():
    endpoint = "/restapi/v1.0/account/~/extension";
    try:
        platform = auth.get_platform()
        res = platform.get(endpoint, {})
        print res.response()._content
    except Exception as e:
        print (e)

get_account_extensions()
