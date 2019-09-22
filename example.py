from payeezy import api


# Declare your API_Key, API_SECRET and TOKEN
API_KEY = 'y6pWAJNyJyjGv66IsVuWnklkKUPFbb0a'
API_SECRET = '86fbae7030253af3cd15faef2a1f4b67353e41fb6799f576b5093ae52901e6f7'
TOKEN = 'fdoa-a480ce8951daa73262734cf102641994c1e55e7cdf4c02b6'
URL = 'https://api-cert.payeezy.com/v1/transactions'

payeezy = api.API(API_KEY, API_SECRET, TOKEN, URL)

transaction = payeezy.process_purchase(transaction_total='2499',
                                       card_type='VISA',
                                       card_number='4005519200000004',
                                       card_expiry='1220',
                                       card_cvv='123',
                                       cardholder_name='Donald Duck',
                                       merchant_reference='Sale')

transaction_response = transaction.transaction_response.json()

if transaction_response['transaction_status'] == 'approved':
    for key in transaction_response:
        print('%s : %s' % (key, transaction_response[key]))
else:
    print(transaction_response['Error'])
