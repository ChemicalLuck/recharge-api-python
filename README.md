# Recharge API Wrapper

## Installation

```bash
pip install recharge-api
```

## Usage

```python
from recharge import RechargeAPI

client = Recharge(access_token='XXXXX')

response = client.Order.list({'status': 'QUEUED', 'limit': '250'})

for order in response['orders']:
    print(order['id'])
```

For more details on the content of the reponses, visit the (official recharge API docs)[https://developer.rechargepayments.com].

## Resources Available
- Addresses
- Charges
- Checkouts
- Customers
- Discounts
- Metafields
- Notifications
- Onetimes
- Orders
- Products
- Shop
- Subscriptions
- Webhooks
- Async Batches

## License
MIT. See LICENSE for more details.

## Acknowledgements
This project is a fork of recharge-api by BuluBox which is no longer available.
