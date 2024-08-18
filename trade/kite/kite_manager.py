from ..webdriver_manager import WebdriverManager
from .credential_manager import CredentialManager
from .kite_auto_login import auto_login
import yaml
import json
from ..opex.logging import logger
from .instruments import InstrumentsManager
logger_prefix = "KiteManager: "
class KiteManager():

    __instance = None

    def __init__(self) -> None:
        self.cred_manager = CredentialManager()
        self.manager = WebdriverManager.get_instance()
        self.kite = auto_login(cred_manager=self.cred_manager, manager=self.manager)
        self.kite.set_access_token(self.cred_manager.get_access_token_data().access_token)
        self.instrument_manager = InstrumentsManager(self.kite)
        if(KiteManager.__instance == None):
            KiteManager.__instance = self.kite
        
        
    
    def fetch_and_save_instruments(self):
        self.instrument_manager.fetch_instruments()
        logger.info(self.instrument_manager.get_instrument('SBIN'))

    def get_historical_data(self, instrument_token: str): 
        token = self.instrument_manager.get_instrument('SBIN')['instrument_token']
        hist = self.kite.historical_data(instrument_token=token, from_date='2024-08-01 00:00:00', interval='day', to_date='2024-08-15 00:00:00')
        print(hist)

    @staticmethod
    def get_kite_instance():
        return KiteManager.kite

        
        
     

