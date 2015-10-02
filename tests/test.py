import unittest
from payeezy import transactions


payeezy = transactions.Transaction
payeezy.TOKEN = 'fdoa-a480ce8951daa73262734cf102641994c1e55e7cdf4c02b6'
payeezy.API_SECRET = '86fbae7030253af3cd15faef2a1f4b67353e41fb6799f576b5093ae52901e6f7'
payeezy.API_KEY = 'y6pWAJNyJyjGv66IsVuWnklkKUPFbb0a'


class OverallTestCase(unittest.TestCase):
    def test_purchase(self):
        transaction = payeezy()
        transaction.process_purchase('2499', 'visa', '4005519200000004', '1019', '123', 'Donald Duck')
        self.assertTrue(transaction.is_transaction_approved())

    def test_authorization(self):
        transaction = payeezy()
        transaction.process_authorization('2499', 'visa', '4005519200000004', '1019', '123', 'Donald Duck')
        self.assertTrue(transaction.is_transaction_approved())

if __name__ == '__main__':
    unittest.main()
