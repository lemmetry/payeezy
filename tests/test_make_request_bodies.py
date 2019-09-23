import unittest
from payeezy.__make_request_bodies import make_request_body_for_purchase


class TestMakeRequestBodyForPurchases(unittest.TestCase):
    def test_request_body_without_reference(self):
        request_body = make_request_body_for_purchase('2499', 'visa', '4005519200000004', '1019', '123',
                                                      'Donald Duck')
        expected_request_body = {
            "merchant_ref": '',
            "transaction_type": "purchase",
            "method": "credit_card",
            "amount": '2499',
            "partial_redemption": "false",
            "currency_code": "USD",
            "credit_card": {
                "type":  'visa',
                "cardholder_name": 'Donald Duck',
                "card_number": '4005519200000004',
                "exp_date": '1019',
                "cvv": '123'
            },
            "billing_address": {
                "city": '',
                "country": '',
                "email": '',
                "phone": {
                    "number": '',
                    "type": ''
                },
                "state_province": '',
                "street": '',
                "zip_postal_code": ''
            }
        }

        self.assertDictEqual(request_body, expected_request_body)

    def test_request_body_with_reference(self):
        request_body = make_request_body_for_purchase('2500', 'discover', '6510000000001248', '1020', '234',
                                                      'Daisy Duck', 'Sale ref')

        expected_request_body = {
            "merchant_ref": 'Sale ref',
            "transaction_type": "purchase",
            "method": "credit_card",
            "amount": '2500',
            "partial_redemption": "false",
            "currency_code": "USD",
            "credit_card": {
                "type":  'discover',
                "cardholder_name": 'Daisy Duck',
                "card_number": '6510000000001248',
                "exp_date": '1020',
                "cvv": '234'
            },
            "billing_address": {
                "city": '',
                "country": '',
                "email": '',
                "phone": {
                    "number": '',
                    "type": ''
                },
                "state_province": '',
                "street": '',
                "zip_postal_code": ''
            }
        }

        self.assertDictEqual(request_body, expected_request_body)

    def test_request_body_with_reference_and_billing_address(self):
        request_body = make_request_body_for_purchase('2500', 'discover', '6510000000001248', '1020', '234',
                                                      'Daisy Duck', 'Sale ref', billing_address_street='123 Main St.',
                                                      billing_address_city='Washington',
                                                      billing_address_state_province='DC',
                                                      billing_address_country='USA',
                                                      billing_address_zip_postal_code='20005',
                                                      billing_address_email='noemail@noemail.com',
                                                      billing_address_phone_type='Cell',
                                                      billing_address_phone_number='8001234567'
                                                      )

        expected_request_body = {
            "merchant_ref": 'Sale ref',
            "transaction_type": "purchase",
            "method": "credit_card",
            "amount": '2500',
            "partial_redemption": "false",
            "currency_code": "USD",
            "credit_card": {
                "type":  'discover',
                "cardholder_name": 'Daisy Duck',
                "card_number": '6510000000001248',
                "exp_date": '1020',
                "cvv": '234'
            },
            "billing_address": {
                "city": 'Washington',
                "country": 'USA',
                "email": 'noemail@noemail.com',
                "phone": {
                    "number": '8001234567',
                    "type": 'Cell'
                },
                "state_province": 'DC',
                "street": '123 Main St.',
                "zip_postal_code": '20005'
            }
        }

        self.assertDictEqual(request_body, expected_request_body)


if __name__ == '__main__':
    unittest.main()
