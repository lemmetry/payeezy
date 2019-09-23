import json
from payeezy import transactions
from payeezy.__make_request_bodies import make_request_body_for_authorization
from payeezy.__make_request_bodies import make_request_body_for_purchase


class API(object):
    def __init__(self, api_key, api_secret, token, url):
        if not api_key:
            raise ValueError('API Key cannot be empty or None')
        self.api_key = api_key

        if not api_secret:
            raise ValueError('API Secret cannot be empty or None')
        self.api_secret = api_secret

        if not token:
            raise ValueError('Token cannot be empty or None')
        self.token = token

        if not url:
            raise ValueError('Url cannot be empty or None')
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
                         merchant_reference='',
                         billing_address_street='',
                         billing_address_city='',
                         billing_address_state_province='',
                         billing_address_country='',
                         billing_address_zip_postal_code='',
                         billing_address_email='',
                         billing_address_phone_type='',
                         billing_address_phone_number=''):
        # billing_address* parameters are optional for Payeezy API, however merchants who have turned on AVS check,
        # would require to provide "billing_address" object in the request payload.

        request_body = make_request_body_for_purchase(transaction_total, card_type, card_number, card_expiry, card_cvv,
                                                      cardholder_name, merchant_reference, billing_address_street,
                                                      billing_address_city, billing_address_state_province,
                                                      billing_address_country, billing_address_zip_postal_code,
                                                      billing_address_email, billing_address_phone_type,
                                                      billing_address_phone_number)
        payload = json.dumps(request_body)
        # According to Payeezy Sandbox, response would contain "avs & token object" fields only if the merchant has
        # enabled AVS check and Token based services with Payeezy.
        # TODO How do we test it?

        purchase = transactions.Transaction(self.api_key, self.api_secret, self.token, self.url, payload)
        purchase.run_transaction()

        return purchase
