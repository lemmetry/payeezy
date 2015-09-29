from payeezy import payeezy


payeezy.API_KEY = 'y6pWAJNyJyjGv66IsVuWnklkKUPFbb0a'
payeezy.API_SECRET = '86fbae7030253af3cd15faef2a1f4b67353e41fb6799f576b5093ae52901e6f7'
payeezy.TOKEN = 'fdoa-a480ce8951daa73262734cf102641994c1e55e7cdf4c02b6'

purchase_result = payeezy.process_purchase(transaction_total='2499',
                                           card_type='VISA',
                                           card_number='4005519200000004',
                                           card_expiry='1218',
                                           card_cvv='123',
                                           cardholder_name='Donald Duck',
                                           merchant_reference='Sale')

if payeezy.is_transaction_approved(purchase_result):
    print('Thank you for your purchase')
else:
    print(payeezy.report_transaction_error_messages(purchase_result))
