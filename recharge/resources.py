import logging
import time

from urllib.parse import urlencode

import requests

log = logging.getLogger(__name__)


class RechargeResource(object):
    """
    Resource from the Recharge API. This class handles
    logging, sending requests, parsing JSON, and rate
    limiting.

    Refer to the API docs to see the expected responses.
    https://developer.rechargepayments.com/
    """
    base_url = 'https://api.rechargeapps.com'
    object_list_key = None

    def __init__(self, access_token=None, log_debug=False):
        self.log_debug = log_debug
        self.headers = {
            'Accept':                  'application/json',
            'Content-Type':            'application/json',
            'X-Recharge-Access-Token': access_token,
        }

    def log(self, url, response):
        if self.log_debug:
            log.info(url)
            log.info(response.headers['X-Recharge-Limit'])

    @property
    def url(self):
        return f'{self.base_url}/{self.object_list_key}'

    def http_delete(self, url):
        response = requests.delete(url, headers=self.headers)
        log.info(url)
        log.info(response.headers['X-Recharge-Limit'])
        if response.status_code == 429:
            return self.http_delete(url)
        return response

    def http_get(self, url):
        response = requests.get(url, headers=self.headers)
        self.log(url, response)
        if response.status_code == 429:
            time.sleep(1)
            return self.http_get(url)
        return response.json()

    def http_put(self, url, data):
        response = requests.put(url, json=data, headers=self.headers)
        self.log(url, response)
        if response.status_code == 429:
            time.sleep(1)
            return self.http_put(url, data)
        return response.json()

    def http_post(self, url, data):
        response = requests.post(url, json=data, headers=self.headers)
        self.log(url, response)
        if response.status_code == 429:
            time.sleep(1)
            return self.http_post(url, data)
        return response.json()

    def create(self, data):
        return self.http_post(self.url, data)

    def update(self, resource_id, data):
        return self.http_put(f'{self.url}/{resource_id}', data)

    def get(self, resource_id):
        return self.http_get(f'{self.url}/{resource_id}')

    def list(self, url_params=None):
        """
        The list method takes a dictionary of filter parameters.
        Refer to the recharge docs for available filters for
        each resource.
        """
        params = ('?' + urlencode(url_params, doseq=True)) if url_params else ''
        return self.http_get(self.url + params)


class RechargeAddress(RechargeResource):
    """
    https://developer.rechargepayments.com/#addresses
    """
    object_list_key = 'addresses'

    def apply_discount(self, address_id, discount_code):
        """ Apply a discount code to an address.
        https://developer.rechargepayments.com/#add-discount-to-address-new
        """
        return self.http_post(
            f'{self.url}/{address_id}/apply_discount',
            {'discount_code': discount_code}
        )

    def count(self, data=None):
        """Retrieve the count of addresses.
        https://developer.rechargepayments.com/v1#count-addresses
        """
        params = ('?' + urlencode(data, doseq=True)) if data else ''
        return self.http_get(f'{self.url}/count{params}')

    def create(self, customer_id, data):
        """Create an address for the customer.
        https://developer.rechargepayments.com/#create-address
        """
        url = f'{self.base_url}/customers/{customer_id}/{self.object_list_key}'
        return self.http_post(url, data)

    def delete(self, address_id):
        """Delete an address.
        https://developer.rechargepayments.com/v1#delete-an-address
        """
        return self.http_delete(f'{self.url}/{address_id}')


class RechargeCharge(RechargeResource):
    """
    https://developer.rechargepayments.com/#charges
    """
    object_list_key = 'charges'

    def change_next_charge_date(self, charge_id, to_date):
        """Change the date of a queued charge.
        https://developer.rechargepayments.com/#change-next-charge-date
        """
        return self.http_put(
            f'{self.url}/{charge_id}/change_next_charge_date',
            {'next_charge_date': to_date}
        )

    def count(self, data=None):
        """Retrieve a count of charges.
        https://developer.rechargepayments.com/v1#count-charges
        """
        params = ('?' + urlencode(data, doseq=True)) if data else ''
        return self.http_get(f'{self.url}/count{params}')

    def full_refund(self, charge_id):
        """Full refund a charge
        https://developer.rechargepayments.com/v1#full-refund-a-charge
        """
        return self.http_post(
            f'{self.url}/{charge_id}/refund',
            {"full_refund": True}
        )

    def process(self, charge_id):
        """Process a charge.
        https://developer.rechargepayments.com/v1#process-a-charge
        """
        return self.http_post(
            f'{self.url}/{charge_id}/process',
            {}
        )

    def refund(self, charge_id, amount):
        """Refund a charge.
        https://developer.rechargepayments.com/v1#refund-a-charge
        """
        return self.http_post(
            f'{self.url}/{charge_id}/refund',
            {"amount": amount}
        )

    def skip(self, charge_id, subscription_id):
        """Skip a charge.
        https://developer.rechargepayments.com/v1#skip-a-charge
        """
        return self.http_post(
            f'{self.url}/{charge_id}/skip',
            {"subscription_id": subscription_id}
        )

    def unskip(self, charge_id, subscription_id):
        """Unskip a charge.
        https://developer.rechargepayments.com/v1#unskip-a-charge
        """
        return self.http_post(
            f'{self.url}/{charge_id}/unskip',
            {"subscription_id": subscription_id}
        )


class RechargeCheckout(RechargeResource):
    """
    https://developer.rechargepayments.com/#checkouts
    """
    object_list_key = 'checkouts'

    def charge(self, checkout_id, data):
        """Process (charge) a checkout.
        https://developer.rechargepayments.com/#process-checkout-beta
        """
        return self.http_post(
            f'{self.url}/{checkout_id}/charge',
            data
        )

    def get_shipping(self, checkout_id):
        """Retrieve shipping rates for a checkout
        https://developer.rechargepayments.com/v1#retrieve-shipping-rates-for-a-checkout
        """
        return self.http_get(f'{self.url}/{checkout_id}/shipping_rates')


class RechargeCustomer(RechargeResource):
    """
    https://developer.rechargepayments.com/#customers
    """
    object_list_key = 'customers'

    def count(self, data=None):
        """Retrieve a count of customers.
        https://developer.rechargepayments.com/v1#count-customers
        """
        params = ('?' + urlencode(data, doseq=True)) if data else ''
        return self.http_get(f'{self.url}/count{params}')

    def delete(self, customer_id):
        """Delete a customer.
        https://developer.rechargepayments.com/v1#delete-a-customer
        """
        return self.http_delete(f'{self.url}/{customer_id}')


class RechargeOrder(RechargeResource):
    """
    https://developer.rechargepayments.com/#orders
    """
    object_list_key = 'orders'

    def change_date(self, order_id, to_date):
        """Change the date of a queued order.
        https://developer.rechargepayments.com/#change-order-date
        """
        return self.http_put(
            f'{self.url}/{order_id}/change_date',
            {'scheduled_at': f'{to_date}T00:00:00'}
        )

    def change_variant(self, order_id, old_variant_id, new_variant_id):
        """Change an order variant.
        https://developer.rechargepayments.com/v1#change-an-order-variant
        """
        return self.http_put(
            f'{self.url}/{order_id}/update_shopify_variant/{old_variant_id}',
            {
                "new_shopify_variant_id": new_variant_id,
                "shopify_variant_id":     old_variant_id
            }
        )

    def count(self, data=None):
        """Retrieve a count of all orders.
        https://developer.rechargepayments.com/v1#count-orders
        """
        params = ('?' + urlencode(data, doseq=True)) if data else ''
        return self.http_get(f'{self.url}/count{params}')

    def delete(self, order_id):
        """https://developer.rechargepayments.com/v1#delete-an-order
        https://developer.rechargepayments.com/#delete-order-beta
        """
        return self.http_delete(f'{self.url}/{order_id}')

    def update_items(self, order_id, data):
        """Update order line_items
        https://developer.rechargepayments.com/v1#update-order-line_items
        """
        return self.http_put(
            f'{self.url}/{order_id}',
            data
        )


class RechargeSubscription(RechargeResource):
    """
    https://developer.rechargepayments.com/#subscriptions
    """
    object_list_key = 'subscriptions'

    def activate(self, subscription_id):
        """Activate a cancelled subscription.
        https://developer.rechargepayments.com/v1#activate-a-subscription
        """
        return self.http_post(
            f'{self.url}/{subscription_id}/activate',
            {}
        )

    def cancel(self, subscription_id, data=None):
        """Cancel a subsciption.
        https://developer.rechargepayments.com/#cancel-subscription
        """
        return self.http_post(f'{self.url}/{subscription_id}/cancel', data)

    def change_address(self, subscription_id, address_id):
        """Change a subscription address.
        https://developer.rechargepayments.com/v1#change-a-subscription-address
        """
        return self.http_post(
            f'{self.url}/{subscription_id}/change_address',
            {"address_id": address_id}
        )

    def count(self, data=None):
        """Returns the count of subscriptions.
        https://developer.rechargepayments.com/v1#count-subscriptions
        """
        params = ('?' + urlencode(data, doseq=True)) if data else ''
        return self.http_get(f'{self.url}/count{params}')

    def delete(self, subscription_id, data=None):
        """Delete a subscription
        https://developer.rechargepayments.com/#delete-subscription
        """
        return self.http_delete(f'{self.url}/{subscription_id}')

    def set_next_charge_date(self, subscription_id, date):
        """Change the next charge date of a subscription
        https://developer.rechargepayments.com/#change-next-charge-date-on-subscription
        """
        return self.http_post(
            f'{self.url}/{subscription_id}/set_next_charge_date',
            {'date': date}
        )


class RechargeOnetime(RechargeResource):
    """
    https://developer.rechargepayments.com/#onetimes
    """
    object_list_key = 'onetimes'

    def delete(self, onetime_id, data=None):
        """Delete a Onetime
        https://developer.rechargepayments.com/#delete-a-onetime
        """
        return self.http_delete(f'{self.url}/{onetime_id}', data)


class RechargeDiscount(RechargeResource):
    """
    https://developer.rechargepayments.com/#discounts
    """
    object_list_key = 'discounts'

    def apply(self, resource, resource_id, discount_code):
        """Apply a discount to an address or charge.
        https://developer.rechargepayments.com/v1#apply-a-discount-to-an-address
        """
        if resource not in ['addresses', 'charges']:
            raise ValueError("Resource is not 'addresses' or 'charges'")
        return self.http_post(
            f'{self.base_url}/{resource}/{resource_id}/apply_discount',
            {"discount_code": discount_code}
        )

    def count(self, data=None):
        """Receive a count of all discounts.
        https://developer.rechargepayments.com/v1#count-discounts
        """
        params = ('?' + urlencode(data, doseq=True)) if data else ''
        return self.http_get(f'{self.url}/count{params}')

    def delete(self, discount_id, data=None):
        """Delete a Discount
        https://developer.rechargepayments.com/#delete-a-discount
        """
        return self.http_delete(f'{self.url}/{discount_id}')

    def remove(self, resource, resource_id):
        """Remove a discount from a charge or address without destroying the discount.
        https://developer.rechargepayments.com/v1#remove-a-discount
        """
        if resource not in ['addresses', 'charges']:
            raise ValueError("Resource is not 'addresses' or 'charges'.")
        return self.http_post(
            f'{self.base_url}/{resource}/{resource_id}/remove_discount',
            {}
        )


class RechargeProduct(RechargeResource):
    """
    https://developer.rechargepayments.com/v1#products
    """
    object_list_key = 'products'

    def count(self, data=None):
        """Retrieve a count of all products.
        https://developer.rechargepayments.com/v1#count-products
        """
        params = ('?' + urlencode(data, doseq=True)) if data else ''
        return self.http_get(f'{self.url}/count{params}')

    def delete(self, product_id):
        """Delete a product from store.
        https://developer.rechargepayments.com/v1#delete-a-product
        """
        return self.http_delete(f'{self.url}/{product_id}')


class RechargeShop(RechargeResource):
    """
    https://developer.rechargepayments.com/v1#shop
    """
    object_list_key = 'shop'

    def retrieve(self):
        """Retrieve store using the Recharge API.
        https://developer.rechargepayments.com/v1#retrieve-a-shop
        """
        return self.http_get(f'{self.url}')

    def shipping_countries(self):
        """Retrieve shipping countries where items can be shipped.
        https://developer.rechargepayments.com/v1#retrieve-a-shop
        """
        return self.http_get(f'{self.url}/shipping_countries')


class RechargeMetafield(RechargeResource):
    """
    https://developer.rechargepayments.com/v1#the-metafield-object
    """
    object_list_key = 'metafields'

    def count(self, data=None):
        """Retrieves a number of metafields for some specific query parameter.
        https://developer.rechargepayments.com/v1#count-metafields
        """
        params = ('?' + urlencode(data, doseq=True)) if data else ''
        return self.http_get(f'{self.url}/count{params}')

    def delete(self, metafield_id):
        """Delete a metafield.
        https://developer.rechargepayments.com/v1#delete-a-metafield
        """
        return self.http_delete(f'{self.url}/{metafield_id}')