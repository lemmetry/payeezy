Payeezy
=======

.. image:: https://img.shields.io/pypi/v/payeezy.svg?branch=master
    :target: https://pypi.python.org/pypi/payeezy

.. image:: https://travis-ci.org/lemmetry/payeezy.svg?branch=master
    :target: https://travis-ci.org/lemmetry/payeezy

This is an **unofficial** package-to-be for processing transactions with `Payeezy <https://developer.payeezy.com/>`_ using Python3.2

.. code-block:: python

    >>> transaction = api.process_purchase(transaction_total='2499',
                                           card_type='VISA',
                                           card_number='4005519200000004',
                                           card_expiry='1218',
                                           card_cvv='123',
                                           cardholder_name='Donald Duck',
                                           merchant_reference='Sale')


Installation:
=============

.. code-block:: bash

    $ pip install payeezy


Usage:
======

See `example.py <https://github.com/lemmetry/payeezy/blob/master/example.py>`_


Functions supported:
====================

- `Credit Card Payments <https://developer.payeezy.com/creditcardpayment/apis/post/transactions>`_: Purchase/Authorize
- Check the status of the submitted transaction
- Check error messages for failed transaction
