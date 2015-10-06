import binascii
import os
import time
import hmac
import hashlib
import base64


def generate_hmac(api_key, api_secret, token, payload):
    if not payload:
        raise ValueError('Payload value cannot be empty or None')

    # Cryptographically strong random number
    nonce = str(int(binascii.hexlify(os.urandom(16)), 16))

    # Epoch timestamp in milli seconds
    timestamp = str(int(round(time.time() * 1000)))

    data = api_key + nonce + timestamp + token + payload
    # Make sure the HMAC hash is in hex
    hmac_in_hex = hmac.new(api_secret.encode(), msg=data.encode(), digestmod=hashlib.sha256).hexdigest()

    # Authorization : base64 of hmac hash
    authorization = base64.b64encode(hmac_in_hex.encode('ascii'))

    return authorization, nonce, timestamp
