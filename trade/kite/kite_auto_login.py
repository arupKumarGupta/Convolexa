from kiteconnect import KiteConnect
from .credential_manager import CredentialManager
from selenium.webdriver.chrome.webdriver import WebDriver
from .dom_element_manager import dom_manager
from pyotp import  TOTP
import time
from urllib.parse import urlparse, parse_qs

def auto_login(cred_manager: CredentialManager, manager: WebDriver) -> KiteConnect:
    creds = cred_manager.get_creds()
    kite = KiteConnect(creds.api_key)
    manager.get(kite.login_url())
    manager.implicitly_wait(10)
    username = dom_manager.find_user_id_input(manager)
    username.send_keys(creds.username)
    pwd = dom_manager.find_pwd(manager)
    pwd.send_keys(creds.password)
    login_btn = dom_manager.find_login_button(manager)
    login_btn.click()
    totp = TOTP(creds.totp_key)
    token = totp.now()
    totp_inp = dom_manager.find_totp_input(manager)
    totp_inp.send_keys(token)
    try:
        auth_btn = dom_manager.find_authorize_button(manager)
        if auth_btn != None:
            auth_btn.click()
    except:
        # must be already done
        pass
    time.sleep(10)
    parsed_url = urlparse(manager.current_url)
    qs = parse_qs(parsed_url.query)
    request_token = (qs['request_token'][0])
    kite_auth_response = kite.generate_session(request_token, api_secret=creds.api_secret)
    cred_manager.save_access_token_response(kite_auth_response)
    return kite
    