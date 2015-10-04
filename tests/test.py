import unittest
from payeezy import api
from payeezy import transactions


payeezy = transactions.Transaction
payeezy.API_KEY = 'y6pWAJNyJyjGv66IsVuWnklkKUPFbb0a'
payeezy.API_SECRET = '86fbae7030253af3cd15faef2a1f4b67353e41fb6799f576b5093ae52901e6f7'
payeezy.TOKEN = 'fdoa-a480ce8951daa73262734cf102641994c1e55e7cdf4c02b6'
payeezy.URL = 'https://api-cert.payeezy.com/v1/transactions'


class OverallTestCase(unittest.TestCase):

    def test_authorization(self):
        transaction = api.process_authorization('2499', 'visa', '4005519200000004', '1019', '123', 'Donald Duck')
        transaction_approved = transaction.is_transaction_approved()
        self.assertTrue(transaction_approved)


class ProcessPaymentTestCase(unittest.TestCase):

    def test_payment_with_clean_data(self):
        transaction = api.process_purchase('2499', 'visa', '4005519200000004', '1019', '123', 'Donald Duck')

        transaction_approved = transaction.is_transaction_approved()
        self.assertTrue(transaction_approved)

    def test_payment_without_transaction_total(self):
        transaction = api.process_purchase('', 'visa', '4005519200000004', '1019', '123', 'Donald Duck')

        transaction_approved = transaction.is_transaction_approved()
        self.assertFalse(transaction_approved)

        transaction_error_messages = transaction.report_transaction_error_messages()
        # according to payeezy sample, expected error message may ALSO be:
        # 'The amount provided is invalid'
        expected_error_messages = ['The amount is missing']
        self.assertEqual(transaction_error_messages, expected_error_messages)

    def test_payment_without_card_type(self):
        transaction = api.process_purchase('2499', '', '4005519200000004', '1019', '123', 'Donald Duck')

        transaction_approved = transaction.is_transaction_approved()
        self.assertFalse(transaction_approved)

        transaction_error_messages = transaction.report_transaction_error_messages()
        # according to payeezy sample, expected error message may ALSO be:
        # 'The card type cannot be empty'
        expected_error_messages = ['The card type is invalid']
        self.assertEqual(transaction_error_messages, expected_error_messages)

    def test_payment_without_card_number(self):
        transaction = api.process_purchase('2499', 'visa', '', '1019', '123', 'Donald Duck')

        transaction_approved = transaction.is_transaction_approved()
        self.assertFalse(transaction_approved)

        transaction_error_messages = transaction.report_transaction_error_messages()
        # according to payeezy sample, expected error message may ALSO be:
        # 'The card number cannot be empty',
        # 'The card number must be numeric',
        # 'The credit card number check failed'
        # 'American Express card number must be 15 digits'
        expected_error_messages = ['The card number must be 16 digits']
        self.assertEqual(transaction_error_messages, expected_error_messages)

    def test_payment_without_card_expiry(self):
        transaction = api.process_purchase('2499', 'visa', '4005519200000004', '', '123', 'Donald Duck')

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
        transaction = api.process_purchase('2499', 'visa', '4005519200000004', '1019', '', 'Donald Duck')

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
        transaction = api.process_purchase('2499', 'visa', '4005519200000004', '1019', '123', '')

        transaction_approved = transaction.is_transaction_approved()
        self.assertFalse(transaction_approved)

        transaction_error_messages = transaction.report_transaction_error_messages()
        # according to payeezy sample, expected error message SUPPOSED to be:
        # 'The card holder name cannot be empty'
        expected_error_messages = ['RELEVANT_CARDHOLDER_NAME_ERROR_HERE']
        self.assertEqual(transaction_error_messages, expected_error_messages)


if __name__ == '__main__':
    unittest.main()
