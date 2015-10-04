import json
from payeezy import transactions


def process_authorization(transaction_total,
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

    authorization = transactions.Transaction(payload)
    authorization.run_transaction()

    return authorization


def process_purchase(transaction_total,
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

    purchase = transactions.Transaction(payload)
    purchase.run_transaction()

    return purchase
