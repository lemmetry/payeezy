

def make_headers(api_key, token, authorization, nonce, timestamp):

    if not api_key:
        raise ValueError('API Key cannot be empty or None')
    api_key = str(api_key)

    if not token:
        raise ValueError('Token cannot be empty or None')
    token = str(token)

    if not authorization:
        raise ValueError('Authorization value cannot be empty or None')
    authorization = str(authorization)

    if not nonce:
        raise ValueError('Nonce value cannot be empty or None')
    nonce = str(nonce)

    if not timestamp:
        raise ValueError('Timestamp value cannot be empty or None')
    timestamp = str(timestamp)

    headers = {
        'apikey': api_key,
        'token': token,
        'Content-type': 'application/json',
        'Authorization': authorization,
        'nonce': nonce,
        'timestamp': timestamp
    }

    return headers
