class Credentials():
    def __init__(self, cred_dict) -> None:
        self.password = cred_dict['password']
        self.api_key = cred_dict['api_key']
        self.api_secret = cred_dict['api_secret']
        self.username = cred_dict['username']
        self.totp_key = cred_dict['totp_key']

class AccessTokenResponse():
    def __init__(self, response: dict) -> None:
        self.access_token:str = response['access_token']
        self.api_key:str = response['api_key']
        self.broker:str = response['broker']
        self.email:str= response['email']
        self.exchanges: list = response['exchanges']
        self.login_time: str = response['login_time']
        self.order_types: list = response['order_types']
        self.products: list = response['products']

class Instruments():
    def __init__(self) -> None:
        self.instrument_token: str= None,
        self.exchange_token: str= None,
        self.tradingsymbol: str= None,
        self.name: str= None,
        self.last_price: float= 0.0,
        self.expiry: str= None,
        self.strike: float= 0.0,
        self.tick_size: float= 0.0,
        self.lot_size: int= 0,
        self.instrument_type: str= None,
        self.segment: str= None,
        self.exchange: str= None