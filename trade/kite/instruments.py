import json
from ..opex.logging import logger
from kiteconnect import KiteConnect
from ..types import Instruments
logger_prefix = 'Instruments: '
class InstrumentsManager():
    def __init__(self, kiteconnect:KiteConnect):
        self.kite = kiteconnect
        self.instruments: list[Instruments] = []
        

    def fetch_instruments(self):
        instruments = self.kite.instruments(exchange='NSE')
        with open("instruments.json", "w") as file:
            try:
                # yaml.safe_dump(instruments, file, default_flow_style=False)
                self.instruments = list(instruments)
                json.dump(instruments,file,indent=2, default=str)
                logger.info(f"{logger_prefix}saved instruments sucessfully")
            except json.JSONDecodeError as ex:
                logger.error(f"{logger_prefix}:failed to load instruments", ex)

    def get_instrument(self, trading_symbol: str):
        return list(filter(lambda x: x['tradingsymbol'] == trading_symbol, self.instruments))[0]

    def get_all_instruments(self):
        pass