from ringcentral import SDK
import json
import os
from dotenv import Dotenv

dotenv = Dotenv(".env")
os.environ.update(dotenv)

if os.getenv("ENVIRONMENT") == "sandbox":
    dotenv = Dotenv("./environment/.env-sandbox")
    tokens_file = "tokens_sb.txt"
else:
    dotenv = Dotenv("./environment/.env-production")
    tokens_file = "tokens_pd.txt"
os.environ.update(dotenv)

class RC_Authentication(object):
    def get_sdk(self):
        sdk = SDK(os.getenv("RC_CLIENT_ID"), os.getenv("RC_CLIENT_SECRET"), os.getenv("RC_SERVER_URL"))
        return sdk

    def get_platform(self):
        sdk = self.get_sdk()
        try:
            platform = sdk.platform()
            if os.path.isfile(tokens_file):
                file = open(tokens_file, 'r')
                tokenObj = json.loads(file.read())
                file.close()
                platform.auth().set_data(tokenObj)
                if platform.logged_in():
                    print ("already loggedin.")
                    return platform
            print ("login/relogin")
            platform.login(os.getenv("RC_USERNAME"), os.getenv("RC_EXTENSION"), os.getenv("RC_PASSWORD"))
            file = open(tokens_file,'w')
            file.write(json.dumps(platform.auth().data()))
            file.close()
            return platform
        except Exception as e:
            raise ValueError(e)
