from payeezy import transactions

payeezy = transactions.Transaction

# Declare your API_Key, API_SECRET and TOKEN
payeezy.API_KEY = 'y6pWAJNyJyjGv66IsVuWnklkKUPFbb0a'
payeezy.API_SECRET = '86fbae7030253af3cd15faef2a1f4b67353e41fb6799f576b5093ae52901e6f7'
payeezy.TOKEN = 'fdoa-a480ce8951daa73262734cf102641994c1e55e7cdf4c02b6'

transaction = payeezy()
purchase_result = transaction.process_purchase(transaction_total='2499',
                                               card_type='VISA',
                                               card_number='4005519200000004',
                                               card_expiry='1218',
                                               card_cvv='123',
                                               cardholder_name='Donald Duck',
                                               merchant_reference='Sale')
if transaction.is_transaction_approved():
    print('Thank you for your purchase')
else:
    print(transaction.report_transaction_error_messages)
