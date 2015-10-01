import unittest
from payeezy import payeezy


payeezy.API_KEY = 'y6pWAJNyJyjGv66IsVuWnklkKUPFbb0a'
payeezy.API_SECRET = '86fbae7030253af3cd15faef2a1f4b67353e41fb6799f576b5093ae52901e6f7'
payeezy.TOKEN = 'fdoa-a480ce8951daa73262734cf102641994c1e55e7cdf4c02b6'


class TestContainer(unittest.TestCase):
    pass


def card_type_and_number_test_generator(card_type, card_number):
    def test(self):
        purchase_result = payeezy.process_purchase(transaction_total='2499',
                                                   card_type=card_type,
                                                   card_number=card_number,
                                                   card_expiry='1218',
                                                   card_cvv='123',
                                                   cardholder_name='Donald Duck',
                                                   merchant_reference='Sale')
        self.assertTrue(payeezy.is_transaction_approved(purchase_result))
    return test

if __name__ == '__main__':
    cards = [
        ['visa', '4005519200000004'],
        ['visa', '4012000033330026']
    ]

    for t in cards:
        test_name = 'test_%s_%s' % (t[0][:2], t[1][-4:])
        test = card_type_and_number_test_generator(t[0], t[1])
        setattr(TestContainer, test_name, test)
    unittest.main()
