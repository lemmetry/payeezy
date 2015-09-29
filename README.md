### Payeezy
This is an **unofficial** package-to-be for processing transactions with [Payeezy](https://developer.payeezy.com/) using Python3.2

##### Prerequisites:
* Python3 is a **must** (also, no versions other than 3.2 were tested)
* [requests](https://github.com/kennethreitz/requests)

##### Installation:
```pip install payeezy```

##### Usage:
1. Import
2. Assign your development/production values to ```API_KEY```, ```API_SECRET``` and ```TOKEN```
3. 
```
purchase_result = process_purchase(transaction_total='2499',
                                   card_type='VISA',
                                   card_number='4005519200000004',
                                   card_expiry='1218',
                                   card_cvv='123', 
                                   cardholder_name='Donald Duck', 
                                   merchant_reference='Sale')
if is_transaction_approved(purchase_result):
    print('Thank you for your purchase')
else:
    print(report_transaction_error_messages(purchase_result))
```

##### Functions supported:
- [x] [Credit Card Payments](https://developer.payeezy.com/creditcardpayment/apis/post/transactions): Purchase/Authorize
- [x] Check the status of the submitted transaction
- [x] Check error messages for failed transaction

##### To do:
- [ ] Provide test card numbers
- [ ] [Tokenize Credit card](https://developer.payeezy.com/tokenizedtreditcardpost/apis/post/transactions/tokens-1)
- [ ] [Token Based Payments](https://developer.payeezy.com/tokenbasedpayments/apis/post/transactions)
