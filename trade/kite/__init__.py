from .kite_manager import KiteManager
def initiate_trading():
    kite_manager = KiteManager()
    kite_manager.fetch_and_save_instruments()
    kite_manager.get_historical_data('SBIN')
