import yaml
from os import path
from trade.types import Credentials, AccessTokenResponse
class CredentialManager():
    access_data: AccessTokenResponse = None
    def __init__(self) -> None:
        with open(path.join(path.dirname(path.abspath(__file__)),'secret.yaml'), 'r') as file:
            try:
                self.credentials = Credentials(yaml.safe_load(file))
            except yaml.YAMLError as exc:
                print(exc)


    def get_creds(self) -> Credentials:
        return self.credentials
    
    def save_access_token_response(self, token_response)->None:
        self.access_data = AccessTokenResponse(token_response)
    
    def get_access_token_data(self):
        return self.access_data
    

    
