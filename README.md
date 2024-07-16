# Recharge API Wrapper

[![Python](https://img.shields.io/pypi/pyversions/recharge-api.svg)](https://badge.fury.io/py/recharge-api)
[![PyPI](https://badge.fury.io/py/recharge-api.svg)](https://badge.fury.io/py/recharge-api)
[![PyPI](https://github.com/ChemicalLuck/recharge-api/actions/workflows/python-publish.yml/badge.svg)](https://github.com/ChemicalLuck/recharge-api/actions/workflows/python-publish.yml)
![PyPI - Downloads](https://img.shields.io/pypi/dm/recharge-api)

## Installation

```bash
pip install recharge-api
```

## Usage

```python
from recharge import RechargeAPI

client = Recharge(access_token='XXXXX')

response = client.v1.Order.list_({'status': 'QUEUED', 'limit': '250'})

for order in response['orders']:
    print(order['id'])
```

For more details on the content of the reponses, visit the [official recharge API docs](https://developer.rechargepayments.com).

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

## Resources

- [Recharge API 2021-01](https://developer.rechargepayments.com/2021-01/)
- [Recharge API 2021-11](https://developer.rechargepayments.com/2021-11/)
- [Recharge API Webhook Examples 2021-01](https://docs.getrecharge.com/docs/webhook-payload-examples)
- [Recharge API Webhook Examples 2021-11](https://docs.getrecharge.com/docs/webhooks-examples-2021-11)

## License

[MIT](LICENSE)

## Acknowledgements

This project is a fork of recharge-api by BuluBox which is no longer available.
