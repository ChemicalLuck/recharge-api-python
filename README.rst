
====================
Recharge API Wrapper
====================

|python| |license|

------------------

A fork of recharge-api by BuluBox.
Expanded to include every v1 recharge api endpoint as well as all methods available.

------------
Installation
------------

.. code-block:: bash

    pip install recharge-api

-----
Usage
-----

.. code-block:: python

    from recharge-api import RechargeAPI

    api = RechargeAPI(access_token='XXXXX')

    response = api.Order.list({'status': 'QUEUED', 'limit': '250'})

    for order in response['orders']:
        print(order['id'])


For more details on the content of the reponses, visit the `official recharge API docs <https://developer.rechargepayments.com/>`_.

-------------------
Resources Available
-------------------

::

    api.Address
    api.Charge    
    api.Checkout    
    api.Customer    
    api.Order    
    api.Subscription
    api.Onetime
    api.Discount
    api.Shop
    api.Product

-----------------
Methods Available
-----------------

::

    api.*.create    
    api.*.update    
    api.*.get    
    api.*.list    

    api.Address.apply_discount    
    api.Checkout.charge    
    api.Order.change_date    
    api.Order.delete    
    api.Subscription.cancel    
    api.Subscription.set_next_charge_date    


-------  
License
-------

MIT. See `LICENSE`_ for more details.

.. |python| image:: https://img.shields.io/pypi/pyversions/recharge.svg?style=flat-square
    :target: https://pypi.python.org/pypi/recharge
    :alt: Python 3.4, 3.5, 3.6

.. |license| image:: https://img.shields.io/github/license/BuluBox/recharge-api.svg?style=flat-square
    :target: https://github.com/BuluBox/recharge-api/blob/master/LICENSE
    :alt: MIT License
