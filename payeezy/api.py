import json
from payeezy import transactions
from payeezy.__make_request_bodies import *


def process_authorization(transaction_total,
                          card_type,
                          card_number,
                          card_expiry,
                          card_cvv,
                          cardholder_name,
                          merchant_reference=''):

    request_body = make_request_body_for_authorization(transaction_total, card_type, card_number, card_expiry, card_cvv,
                                                       cardholder_name, merchant_reference)
    payload = json.dumps(request_body)

    authorization = transactions.Transaction(payload)
    authorization.run_transaction(authorization.API_KEY, authorization.TOKEN)

    return authorization


def process_purchase(transaction_total,
                     card_type,
                     card_number,
                     card_expiry,
                     card_cvv,
                     cardholder_name,
                     merchant_reference=''):

    request_body = make_request_body_for_purchase(transaction_total, card_type, card_number, card_expiry, card_cvv,
                                                  cardholder_name, merchant_reference)
    payload = json.dumps(request_body)

    purchase = transactions.Transaction(payload)
    purchase.run_transaction(purchase.API_KEY, purchase.TOKEN)

    return purchase
