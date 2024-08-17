from ..webdriver_manager import WebdriverManager
from .credential_manager import CredentialManager
from .kite_auto_login import auto_login

class KiteManager():

    def __init__(self) -> None:
        self.cred_manager = CredentialManager()
        self.manager = WebdriverManager.get_instance()
        self.kite = None
        
    
    def login(self):
        self.kite = auto_login(cred_manager=self.cred_manager, manager=self.manager)
        self.kite.set_access_token(self.cred_manager.get_access_token_data().access_token)
        print("Kite login success")
        # print(str(self.kite.instruments()))
        
        
     

