import binascii
import os
import time
import hmac
import hashlib
import base64
import json
import requests


class Transaction(object):
    API_KEY = ''
    API_SECRET = ''
    TOKEN = ''
    URL = 'https://api-cert.payeezy.com/v1/transactions'

    def __init__(self):
        self.transaction_response = None

    def get_transaction_response(self):
        return self.transaction_response

    def set_transaction_response(self, response_value):
        self.transaction_response = response_value

    def generate_hmac(self, payload):
        # Cryptographically strong random number
        nonce = str(int(binascii.hexlify(os.urandom(16)), 16))

        # Epoch timestamp in milli seconds
        timestamp = str(int(round(time.time() * 1000)))

        data = self.API_KEY + nonce + timestamp + self.TOKEN + payload
        # Make sure the HMAC hash is in hex
        hmac_in_hex = hmac.new(self.API_SECRET.encode(), msg=data.encode(), digestmod=hashlib.sha256).hexdigest()

        # Authorization : base64 of hmac hash
        authorization = base64.b64encode(hmac_in_hex.encode('ascii'))

        return authorization, nonce, timestamp

    def generate_headers(self, payload):
        authorization, nonce, timestamp = self.generate_hmac(payload)

        headers = {
            'apikey': self.API_KEY,
            'token': self.TOKEN,
            'Content-type': 'application/json',
            'Authorization': authorization,
            'nonce': nonce,
            'timestamp': timestamp
        }
        return headers

    def process_authorization(self,
                              transaction_total,
                              card_type,
                              card_number,
                              card_expiry,
                              card_cvv,
                              cardholder_name,
                              merchant_reference=''):

        request_body = {
            "merchant_ref": merchant_reference,
            "transaction_type": "authorize",
            "method": "credit_card",
            "amount": transaction_total,
            "currency_code": "USD",
            "credit_card": {
                "type": card_type,
                "cardholder_name": cardholder_name,
                "card_number": card_number,
                "exp_date": card_expiry,
                "cvv": card_cvv
            }
        }

        payload = json.dumps(request_body)
        headers = self.generate_headers(payload)
        response = requests.post(url=self.URL, data=payload, headers=headers)
        self.set_transaction_response(response)

    def process_purchase(self,
                         transaction_total,
                         card_type,
                         card_number,
                         card_expiry,
                         card_cvv,
                         cardholder_name,
                         merchant_reference=''):

        request_body = {
            "merchant_ref": merchant_reference,
            "transaction_type": "purchase",
            "method": "credit_card",
            "amount": transaction_total,
            "partial_redemption": "false",
            "currency_code": "USD",
            "credit_card": {
                "type":  card_type,
                "cardholder_name": cardholder_name,
                "card_number": card_number,
                "exp_date": card_expiry,
                "cvv": card_cvv
            }
        }

        payload = json.dumps(request_body)
        headers = self.generate_headers(payload)
        response = requests.post(url=self.URL, data=payload, headers=headers)
        self.set_transaction_response(response)

    def is_transaction_approved(self):
        """
        Returns True if transaction approved and False otherwise.

        The gateway_resp_code will always be “00” for a successful transaction, indicating that there were no errors
        attempting to process the transaction. The bank_resp_code will vary based on the response from the issuing bank.

        Complete list of bank response codes:
        https://support.payeezy.com/hc/en-us/articles/203730509-First-Data-Payeezy-Gateway-Bank-Response-Codes
        """
        # TODO find humane way to manage the codes
        VALID_HTTP_STATUS_CODES = [200, 201, 202]
        VALID_BANK_RESPONSE_CODES = ['100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111',
                                     '164']

        response = self.get_transaction_response()

        # get response status code
        http_status_code = response.status_code

        if http_status_code in VALID_HTTP_STATUS_CODES:
            # get response data
            response_data = response.json()

            # get gateway_resp_code
            gateway_response_code = response_data['gateway_resp_code']

            # compare gate_way_resp code to '00'
            gateway_response_is_valid = False
            if gateway_response_code == '00':
                gateway_response_is_valid = True

            # get bank_resp_code
            bank_response_code = response_data['bank_resp_code']

            # compare bank_resp_code to valid(successful) codes
            bank_response_is_valid = False
            if bank_response_code in VALID_BANK_RESPONSE_CODES:
                bank_response_is_valid = True

            # transaction approved if BOTH gateway_resp_code and bank_resp_code are valid(successful) codes:
            if gateway_response_is_valid and bank_response_is_valid:
                return True

        # transaction failed
        return False

    def report_transaction_error_messages(self):
        """
        Gets error messages from response to HTTP request for invalid transactions.
        Returns list.
        """
        response = self.get_transaction_response()

        # get response data from response object
        response_data = response.json()

        # get error messages
        response_error = response_data['Error']
        response_error_messages = response_error['messages']

        # add all error messages to the report
        error_messages_to_report = []
        for response_error_message in response_error_messages:
            error_description = response_error_message['description']
            error_messages_to_report.append(error_description)

        return error_messages_to_report
