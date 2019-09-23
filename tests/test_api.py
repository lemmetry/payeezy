import unittest
from payeezy import api


API_KEY = 'y6pWAJNyJyjGv66IsVuWnklkKUPFbb0a'
API_SECRET = '86fbae7030253af3cd15faef2a1f4b67353e41fb6799f576b5093ae52901e6f7'
TOKEN = 'fdoa-a480ce8951daa73262734cf102641994c1e55e7cdf4c02b6'
URL = 'https://api-cert.payeezy.com/v1/transactions'

payeezy = api.API(API_KEY, API_SECRET, TOKEN, URL)


class BadSecretValues(unittest.TestCase):

    def test_bad_api_key(self):
        bad_api_keys = ['', None]

        for bad_api_key in bad_api_keys:
            with self.assertRaises(ValueError) as cm:
                api.API(bad_api_key, API_SECRET, TOKEN, URL)

            raised_message = str(cm.exception)
            expected_message = 'API Key cannot be empty or None'
            self.assertEqual(raised_message, expected_message)

    def test_bad_api_secret(self):
        bad_api_secrets = ['', None]

        for bad_api_secret in bad_api_secrets:
            with self.assertRaises(ValueError) as cm:
                api.API(API_KEY, bad_api_secret, TOKEN, URL)

            raised_message = str(cm.exception)
            expected_message = 'API Secret cannot be empty or None'
            self.assertEqual(raised_message, expected_message)

    def test_bad_token(self):
        bad_tokens = ['', None]

        for bad_token in bad_tokens:
            with self.assertRaises(ValueError) as cm:
                api.API(API_KEY, API_SECRET, bad_token, URL)

            raised_message = str(cm.exception)
            expected_message = 'Token cannot be empty or None'
            self.assertEqual(raised_message, expected_message)

    def test_bad_url(self):
        bad_urls = ['', None]

        for bad_url in bad_urls:
            with self.assertRaises(ValueError) as cm:
                api.API(API_KEY, API_SECRET, TOKEN, bad_url)

            raised_message = str(cm.exception)
            expected_message = 'Url cannot be empty or None'
            self.assertEqual(raised_message, expected_message)


class OverallTestCase(unittest.TestCase):

    def test_authorization(self):
        transaction = payeezy.process_authorization('2499', 'visa', '4005519200000004', '1019', '123', 'Donald Duck')
        transaction_approved = transaction.is_transaction_approved()
        self.assertTrue(transaction_approved)


class ProcessPaymentTestCase(unittest.TestCase):

    def test_payment_with_clean_data(self):
        cards_to_test = [
            ['Visa', '4012000033330026'],
            ['Visa', '4005519200000004'],
            ['Mastercard', '5424180279791732'],
            ['Mastercard', '5526399000648568'],
            ['Mastercard', '5405010100000016'],
            ['American Express', '373953192351004'],
            ['American Express', '341111597241002'],
            ['Discover', '6510000000001248'],
        ]

        for card_to_test in cards_to_test:
            card_type = card_to_test[0]
            card_number = card_to_test[1]

            transaction = payeezy.process_purchase('2499', card_type, card_number, '1019', '123', 'Donald Duck')
            transaction_approved = transaction.is_transaction_approved()
            self.assertTrue(transaction_approved)

    def test_payment_without_transaction_total(self):
        transaction = payeezy.process_purchase('', 'visa', '4005519200000004', '1019', '123', 'Donald Duck')

        transaction_approved = transaction.is_transaction_approved()
        self.assertFalse(transaction_approved)

        transaction_error_messages = transaction.report_transaction_error_messages()
        # according to payeezy sample, expected error message may ALSO be:
        # 'The amount provided is invalid'
        expected_error_messages = ['The amount is missing']
        self.assertEqual(transaction_error_messages, expected_error_messages)

    def test_payment_without_card_type(self):
        transaction = payeezy.process_purchase('2499', '', '4005519200000004', '1019', '123', 'Donald Duck')

        transaction_approved = transaction.is_transaction_approved()
        self.assertFalse(transaction_approved)

        transaction_error_messages = transaction.report_transaction_error_messages()
        # according to payeezy sample, expected error message may ALSO be:
        # 'The card type cannot be empty'
        expected_error_messages = ['The card type is invalid']
        self.assertEqual(transaction_error_messages, expected_error_messages)

    def test_payment_without_card_number(self):
        transaction = payeezy.process_purchase('2499', 'visa', '', '1019', '123', 'Donald Duck')

        transaction_approved = transaction.is_transaction_approved()
        self.assertFalse(transaction_approved)

        transaction_error_messages = transaction.report_transaction_error_messages()
        # according to payeezy sample, expected error message may ALSO be:
        # 'The card number cannot be empty',
        # 'The card number must be numeric',
        # 'The credit card number check failed'
        # 'American Express card number must be 15 digits'
        expected_error_messages = ['The card number cannot be empty']
        self.assertEqual(transaction_error_messages, expected_error_messages)

    def test_payment_without_card_expiry(self):
        transaction = payeezy.process_purchase('2499', 'visa', '4005519200000004', '', '123', 'Donald Duck')

        transaction_approved = transaction.is_transaction_approved()
        self.assertFalse(transaction_approved)

        transaction_error_messages = transaction.report_transaction_error_messages()
        # according to payeezy sample, expected error message SUPPOSED to be:
        # 'The card has expired'
        expected_error_messages = ['Expiry Date is invalid']
        self.assertEqual(transaction_error_messages, expected_error_messages)

    @unittest.expectedFailure
    # payeezy sandbox API does **not** check cvv and transaction is being approved
    def test_payment_without_card_cvv(self):
        transaction = payeezy.process_purchase('2499', 'visa', '4005519200000004', '1019', '', 'Donald Duck')

        transaction_approved = transaction.is_transaction_approved()
        self.assertFalse(transaction_approved)

        transaction_error_messages = transaction.report_transaction_error_messages()
        # according to payeezy sample, expected error message SUPPOSED to be:
        # 'The cvv provided must be numeric'
        expected_error_messages = ['RELEVANT_CARD_CVV_ERROR_HERE']
        self.assertEqual(transaction_error_messages, expected_error_messages)

    @unittest.expectedFailure
    # Fails with 400 instead of the relevant API error
    def test_payment_without_cardholder_name(self):
        transaction = payeezy.process_purchase('2499', 'visa', '4005519200000004', '1019', '123', '')

        transaction_approved = transaction.is_transaction_approved()
        self.assertFalse(transaction_approved)

        transaction_error_messages = transaction.report_transaction_error_messages()
        # according to payeezy sample, expected error message SUPPOSED to be:
        # 'The card holder name cannot be empty'
        expected_error_messages = ['RELEVANT_CARDHOLDER_NAME_ERROR_HERE']
        self.assertEqual(transaction_error_messages, expected_error_messages)


if __name__ == '__main__':
    unittest.main()
