# Recharge API Wrapper

[![PyPI](https://github.com/ChemicalLuck/recharge-api/actions/workflows/python-publish.yml/badge.svg)](https://github.com/ChemicalLuck/recharge-api/actions/workflows/python-publish.yml)
![PyPI - License](https://img.shields.io/pypi/l/recharge-api)
![PyPI - Downloads](https://img.shields.io/pypi/dm/recharge-api)

## Installation

```bash
pip install recharge-api
```

## Usage

```python
from recharge import RechargeAPI

client = Recharge(access_token='XXXXX')

response = client.v1.Order.list({'status': 'QUEUED', 'limit': '250'})

for order in response['orders']:
    print(order['id'])
```

For more details on the content of the reponses, visit the (official recharge API docs)[https://developer.rechargepayments.com].

## Resources Available
### v1(2021-01)
- Address
- Charge
- Checkout
- Customer
- Discount
- Metafield
- Notification
- Onetime
- Order
- Product
- Shop
- Subscription
- Webhook
- Async Batch
### v2(2021-11)
- Address
- BundleSelection
- Charge
- Checkout
- Collection
- Customer
- Discount
- Metafield
- Notification
- Onetime
- Order
- Payment Method
- Plan
- Retention Strategy
- Subscription
- Webhook
- Async Batch
- Token
- Account
- Event
- Store

## License
MIT. See LICENSE for more details.

## Acknowledgements
This project is a fork of recharge-api by BuluBox which is no longer available.
