import unittest
from payeezy.__make_headers import *


class TestMakeHeadersWithEmptyOrNoneData(unittest.TestCase):
    dummy_api_key = 'dummy_api_key'
    dummy_token = 'dummy_token'
    dummy_authorization = 'dummy_authorization'
    dummy_nonce = 'dummy_nonce'
    dummy_timestamp = 'dummy_timestamp'

    def test_make_headers_with_good_data(self):
        expected_headers = {
            'apikey': self.dummy_api_key,
            'token': self.dummy_token,
            'Content-type': 'application/json',
            'Authorization': self.dummy_authorization,
            'nonce': self.dummy_nonce,
            'timestamp': self.dummy_timestamp
        }

        headers = make_headers(self.dummy_api_key, self.dummy_token, self.dummy_authorization, self.dummy_nonce,
                               self.dummy_timestamp)
        self.assertEqual(headers, expected_headers)

    def test_make_headers_with_empty_or_none_api_key(self):
        bad_api_keys = ['', None]

        for bad_api_key in bad_api_keys:
            with self.assertRaises(ValueError) as cm:
                make_headers(bad_api_key, self.dummy_token, self.dummy_authorization, self.dummy_nonce,
                             self.dummy_timestamp)

            raised_message = str(cm.exception)
            expected_message = 'API Key cannot be empty or None'
            self.assertEqual(raised_message, expected_message)

    def test_make_headers_with_empty_or_none_token(self):
        bad_tokens = ['', None]

        for bad_token in bad_tokens:
            with self.assertRaises(ValueError) as cm:
                make_headers(self.dummy_api_key, bad_token, self.dummy_authorization, self.dummy_nonce,
                             self.dummy_timestamp)

            raised_message = str(cm.exception)
            expected_message = 'Token cannot be empty or None'
            self.assertEqual(raised_message, expected_message)

    def test_make_headers_with_empty_or_none_authorization(self):
        bad_authorizations = ['', None]

        for bad_authorization in bad_authorizations:
            with self.assertRaises(ValueError) as cm:
                make_headers(self.dummy_api_key, self.dummy_token, bad_authorization, self.dummy_nonce,
                             self.dummy_timestamp)

            raised_message = str(cm.exception)
            expected_message = 'Authorization value cannot be empty or None'
            self.assertEqual(raised_message, expected_message)

    def test_make_headers_with_empty_or_none_nonce(self):
        bad_nonces = ['', None]

        for bad_nonce in bad_nonces:
            with self.assertRaises(ValueError) as cm:
                make_headers(self.dummy_api_key, self.dummy_token, self.dummy_authorization, bad_nonce,
                             self.dummy_timestamp)

            raised_message = str(cm.exception)
            expected_message = 'Nonce value cannot be empty or None'
            self.assertEqual(raised_message, expected_message)

    def test_make_headers_with_empty_or_none_timestamp(self):
        bad_timestamps = ['', None]

        for bad_timestamp in bad_timestamps:
            with self.assertRaises(ValueError) as cm:
                make_headers(self.dummy_api_key, self.dummy_token, self.dummy_authorization, self.dummy_nonce,
                             bad_timestamp)

            raised_message = str(cm.exception)
            expected_message = 'Timestamp value cannot be empty or None'
            self.assertEqual(raised_message, expected_message)


class TestMakeHeadersIfDictHasTypeStringValues(unittest.TestCase):
    dummy_api_key = 2345
    dummy_token = 34567
    dummy_authorization = 456789
    dummy_nonce = 6789012
    dummy_timestamp = 7890123

    def test_make_headers_if_dict_has_type_string_values(self):
        expected_headers = {
            'apikey': str(self.dummy_api_key),
            'token': str(self.dummy_token),
            'Content-type': 'application/json',
            'Authorization': str(self.dummy_authorization),
            'nonce': str(self.dummy_nonce),
            'timestamp': str(self.dummy_timestamp)
        }

        headers = make_headers(self.dummy_api_key, self.dummy_token, self.dummy_authorization, self.dummy_nonce,
                               self.dummy_timestamp)
        self.assertEqual(headers, expected_headers)
        self.assertIsInstance(headers['apikey'], str)
        self.assertIsInstance(headers['token'], str)
        self.assertIsInstance(headers['Content-type'], str)
        self.assertIsInstance(headers['Authorization'], str)
        self.assertIsInstance(headers['nonce'], str)
        self.assertIsInstance(headers['timestamp'], str)


if __name__ == '__main__':
    unittest.main()
