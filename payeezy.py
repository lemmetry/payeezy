import binascii
import os
import time
import hmac
import hashlib
import base64
import json


API_KEY = 'y6pWAJNyJyjGv66IsVuWnklkKUPFbb0a'
API_SECRET = '86fbae7030253af3cd15faef2a1f4b67353e41fb6799f576b5093ae52901e6f7'
TOKEN = 'fdoa-a480ce8951daa73262734cf102641994c1e55e7cdf4c02b6'


def generate_hmac(request_body):
    # get payload
    payload = json.dumps(request_body)

    # Cryptographically strong random number
    nonce = str(int(binascii.hexlify(os.urandom(16)), 16))

    # Epoch timestamp in milli seconds
    timestamp = str(int(round(time.time() * 1000)))

    data = API_KEY + nonce + timestamp + TOKEN + payload
    # Make sure the HMAC hash is in hex
    hmac_in_hex = hmac.new(API_SECRET.encode(), msg=data.encode(), digestmod=hashlib.sha256).hexdigest()

    # Authorization : base64 of hmac hash
    authorization = base64.b64encode(hmac_in_hex.encode('ascii'))

    return authorization, nonce, timestamp