from .kite_manager import KiteManager
def initiate_trading():
    kite_manager = KiteManager()
    kite_manager.login()
