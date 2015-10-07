import json
from payeezy import transactions
from payeezy.__make_request_bodies import make_request_body_for_authorization
from payeezy.__make_request_bodies import make_request_body_for_purchase

class API(object):
    def __init__(self, api_key, api_secret, token, url):
        if not api_key:
            raise ValueError()
        self.api_key = api_key

        if not api_secret:
            raise ValueError
        self.api_secret = api_secret

        if not token:
            raise ValueError
        self.token = token

        if not url:
            raise ValueError
        self.url = url

    def process_authorization(self,
                              transaction_total,
                              card_type,
                              card_number,
                              card_expiry,
                              card_cvv,
                              cardholder_name,
                              merchant_reference=''):

        request_body = make_request_body_for_authorization(transaction_total, card_type, card_number, card_expiry, card_cvv,
                                                           cardholder_name, merchant_reference)
        payload = json.dumps(request_body)

        authorization = transactions.Transaction(self.api_key, self.api_secret, self.token, self.url, payload)
        authorization.run_transaction()

        return authorization

    def process_purchase(self,
                         transaction_total,
                         card_type,
                         card_number,
                         card_expiry,
                         card_cvv,
                         cardholder_name,
                         merchant_reference=''):

        request_body = make_request_body_for_purchase(transaction_total, card_type, card_number, card_expiry, card_cvv,
                                                      cardholder_name, merchant_reference)
        payload = json.dumps(request_body)

        purchase = transactions.Transaction(self.api_key, self.api_secret, self.token, self.url, payload)
        purchase.run_transaction()

        return purchase
