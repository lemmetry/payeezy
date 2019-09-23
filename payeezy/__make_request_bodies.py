

def make_request_body_for_purchase(transaction_total,
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

    transaction_total = str(transaction_total)
    card_type = str(card_type)
    card_number = str(card_number)
    card_expiry = str(card_expiry)
    card_cvv = str(card_cvv)
    cardholder_name = str(cardholder_name)

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
        },
        "billing_address": {
            "city": billing_address_city,
            "country": billing_address_country,
            "email": billing_address_email,
            "phone": {
                "type": billing_address_phone_type,
                "number": billing_address_phone_number
            },
            "street": billing_address_street,
            "state_province": billing_address_state_province,
            "zip_postal_code": billing_address_zip_postal_code
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
