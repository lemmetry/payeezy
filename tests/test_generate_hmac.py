import unittest
from payeezy.__generate_hmac import generate_hmac


class TestGenerateHmacReturnsNonEmptyValues(unittest.TestCase):
    dummy_api_key = 'dummy_api_key'
    dummy_api_secret = 'dummy_api_secret'
    dummy_token = 'dummy_token'

    def test_generate_hmac_returns_non_empty_values(self):
        dummy_payload = '{"credit_card": {"card_number": "card_number", "exp_date": "card_expiry"}}'
        authorization, nonce, timestamp = generate_hmac(self.dummy_api_key, self.dummy_api_secret, self.dummy_token,
                                                        dummy_payload)
        self.assertIsNotNone(authorization)
        self.assertIsNotNone(nonce)
        self.assertIsNotNone(timestamp)

    def test_generate_hmac_with_empty_or_none_payload(self):
        bad_payloads = ['', None]

        for bad_payload in bad_payloads:
            with self.assertRaises(ValueError) as cm:
                generate_hmac(self.dummy_api_key, self.dummy_api_secret, self.dummy_token, bad_payload)

            raised_message = str(cm.exception)
            expected_message = 'Payload value cannot be empty or None'
            self.assertEqual(raised_message, expected_message)

if __name__ == '__main__':
    unittest.main()
