

def make_request_body_for_purchase(transaction_total,
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

    return request_body


def make_request_body_for_authorization(transaction_total,
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

    return request_body
