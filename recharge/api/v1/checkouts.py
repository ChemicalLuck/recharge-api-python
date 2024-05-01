from typing import Literal, Required, TypedDict, TypeAlias

from recharge.api import RechargeResource, RechargeScope


class CheckoutUtmParams(TypedDict, total=False):
    utm_campaign: str
    utm_content: str
    utm_data_source: str
    utm_source: str
    utm_medium: str
    utm_term: str
    utm_timestamp: str


class CheckoutAnalyticsData(TypedDict, total=False):
    utm_params: list[CheckoutUtmParams]


class CheckoutBillingAddress(TypedDict, total=False):
    address1: str
    address2: str
    city: str
    company: str
    country: str
    first_name: str
    last_name: str
    phone: str
    province: str
    zip: str


CheckoutExternalCheckoutSource: TypeAlias = Literal[
    "big_commerce", "headless", "shopify"
]

CheckoutOrderIntervalUnit: TypeAlias = Literal["day", "week", "month"]


class CheckoutLineItemProperty(TypedDict):
    name: str
    value: str


CheckoutLineItemType: TypeAlias = Literal["SUBSCRIPTION", "ONETIME"]


class CheckoutLineItem(TypedDict, total=False):
    charge_interval_frequency: int
    cutoff_day_of_month: int
    cutoff_day_of_week: int
    expire_after_specific_number_of_charges: int
    first_recurring_charge_delay: int
    fulfillment_service: str
    grams: int
    image: str
    order_day_of_month: int
    order_day_of_week: int
    order_interval_frequency: int
    order_interval_unit: CheckoutOrderIntervalUnit
    original_price: str
    price: str
    product_id: int
    product_type: str
    properties: list[CheckoutLineItemProperty]
    quantity: int
    requires_shipping: bool
    sku: str
    tax_code: str
    taxable: bool
    title: str
    type: CheckoutLineItemType
    variant_id: int
    variant_title: str


class CheckoutNoteAttribute(TypedDict):
    name: str
    value: str


class CheckoutShippingAddress(TypedDict, total=False):
    address1: str
    address2: str
    city: str
    company: str
    country: str
    first_name: str
    last_name: str
    phone: str
    province: str
    zip: str


class CheckoutCreateBody(TypedDict, total=False):
    analytics_data: CheckoutAnalyticsData
    billing_address: CheckoutBillingAddress
    buyer_accepts_marketing: bool
    currency: str
    discount_code: str
    email: str
    external_checkout_id: str
    external_checkout_source: CheckoutExternalCheckoutSource
    external_checkout_customer_id: str
    line_items: Required[list[CheckoutLineItem]]
    note: str
    note_attributes: list[CheckoutNoteAttribute]
    phone: str
    shipping_address: CheckoutShippingAddress


class CheckoutUpdateBody(TypedDict, total=False):
    analytics_data: CheckoutAnalyticsData
    billing_address: CheckoutBillingAddress
    buyer_accepts_marketing: bool
    currency: str
    discount_code: str
    email: str
    external_checkout_id: str
    external_checkout_source: CheckoutExternalCheckoutSource
    external_checkout_customer_id: str
    line_items: list[CheckoutLineItem]
    note: str
    note_attributes: list[CheckoutNoteAttribute]
    partial_shipping: bool
    phone: str
    shipping_address: CheckoutShippingAddress


CheckoutPaymentProcessor: TypeAlias = Literal[
    "stripe", "braintree", "mollie", "authorize"
]

CheckoutPaymentType: TypeAlias = Literal[
    "CREDIT_CARD", "PAYPAL", "APPLE_PAY", "GOOGLE_PAY"
]


class CheckoutProcessBody(TypedDict, total=False):
    payment_processor: Required[CheckoutPaymentProcessor]
    payment_token: Required[str]
    payment_type: CheckoutPaymentType


class CheckoutResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/checkouts
    """

    object_list_key = "checkouts"

    def create(self, body: CheckoutCreateBody):
        """Create a new checkout.
        https://developer.rechargepayments.com/2021-01/checkouts/checkout_create
        """
        required_scopes: list[RechargeScope] = ["write_checkouts"]
        self.check_scopes(f"POST /{self.object_list_key}", required_scopes)

        return self._http_post(self.url, body)

    def get(self, checkout_id: str):
        """Get a checkout by ID.
        https://developer.rechargepayments.com/2021-01/checkouts/checkout_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_checkouts"]
        self.check_scopes(f"GET /{self.object_list_key}/:checkout_id", required_scopes)

        return self._http_get(f"{self.url}/{checkout_id}")

    def update(self, checkout_id: str, body: CheckoutUpdateBody):
        """Update a checkout.
        https://developer.rechargepayments.com/2021-01/checkouts/checkout_update
        """
        required_scopes: list[RechargeScope] = ["write_checkouts"]
        self.check_scopes(f"PUT /{self.object_list_key}/:checkout_id", required_scopes)

        return self._http_put(f"{self.url}/{checkout_id}", body)

    def get_shipping(self, checkout_id: str):
        """Retrieve shipping rates for a checkout
        https://developer.rechargepayments.com/2021-01/checkouts/checkout_retrieve_shipping_address
        """
        required_scopes: list[RechargeScope] = ["read_checkouts"]
        self.check_scopes(
            f"GET /{self.object_list_key}/:checkout_id/shipping_rates", required_scopes
        )

        return self._http_get(f"{self.url}/{checkout_id}/shipping_rates")

    def process(self, checkout_id: str, body: CheckoutProcessBody):
        """Process (charge) a checkout.
        https://developer.rechargepayments.com/2021-01/checkout/checkout_process
        """
        required_scopes: list[RechargeScope] = ["write_checkouts"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:checkout_id/charge", required_scopes
        )

        return self._http_post(f"{self.url}/{checkout_id}/charge", body)
