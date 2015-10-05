import unittest
from payeezy.__make_request_bodies import *


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
            }
        }

        self.assertEqual(request_body, expected_request_body)

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
            }
        }

        self.assertEqual(request_body, expected_request_body)


if __name__ == '__main__':
    unittest.main()
