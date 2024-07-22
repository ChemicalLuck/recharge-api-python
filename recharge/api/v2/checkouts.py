from typing import Literal, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v2.checkout import (
    Checkout,
    CheckoutShippingRate,
)


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


CheckoutExternalCheckoutSource = Literal["big_commerce", "headless", "shopify"]

CheckoutOrderIntervalUnit = Literal["day", "week", "month"]


class CheckoutLineItemProperty(TypedDict):
    name: str
    value: str


CheckoutLineItemType = Literal["SUBSCRIPTION", "ONETIME"]


class CheckoutLineItemExternalProductId(TypedDict):
    ecommerce: str


class CheckoutLineItemExternalVariantId(TypedDict):
    ecommerce: str


class CheckoutLineItemImages(TypedDict):
    large: str
    medium: str
    small: str
    original: str


CheckoutLineItemPurchaseItemType = Literal["subscription", "onetime"]


class CheckoutLineItemSubscriptionPreferences(TypedDict):
    charge_interval_frequency: int
    cutoff_day_of_month: int
    cutoff_day_of_week: int
    expire_after_specific_number_of_charges: int
    order_day_of_month: int
    order_day_of_week: int
    order_interval_frequency: int
    interval_unit: CheckoutOrderIntervalUnit


class CheckoutBodyLineItem(TypedDict, total=False):
    external_product_id: CheckoutLineItemExternalProductId
    external_variant_id: CheckoutLineItemExternalVariantId
    handle: str
    images: CheckoutLineItemImages
    properties: list[CheckoutLineItemProperty]
    purchase_item_type: CheckoutLineItemPurchaseItemType
    quantity: int
    sku: str
    subscription_preferences: CheckoutLineItemSubscriptionPreferences
    title: str
    unit_price: str
    variant_title: str
    weight: int


class CheckoutOrderAttribute(TypedDict):
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


class CheckoutAppliedDiscount(TypedDict):
    discount_code: str


class CheckoutAppliedShippingRate(TypedDict):
    handle: str


class CheckoutCustomShippingRateOption(TypedDict):
    code: str
    price: str
    title: str
    handle: str


class CheckoutExternalTransactionId(TypedDict):
    payment_processor: str


class CheckoutAppliedShippingLine(TypedDict):
    code: str
    price: str
    source: str
    title: str
    taxable: bool


class CheckoutCreateBodyOptional(TypedDict, total=False):
    get_shipping_rates: bool
    analytics_data: CheckoutAnalyticsData
    applied_discounts: list[CheckoutAppliedDiscount]
    applied_shipping_rate: CheckoutAppliedShippingRate
    custom_shipping_rate_options: list[CheckoutCustomShippingRateOption]
    billing_address: CheckoutBillingAddress
    currency: str
    email: str
    external_checkout_id: str
    external_checkout_source: str
    external_transaction_id: CheckoutExternalTransactionId
    note: str
    order_attributes: list[CheckoutOrderAttribute]
    shipping_address: CheckoutShippingAddress


class CheckoutCreateBody(CheckoutCreateBodyOptional):
    line_items: list[CheckoutBodyLineItem]


class CheckoutUpdateBody(TypedDict, total=False):
    get_shipping_rates: bool
    analytics_data: CheckoutAnalyticsData
    applied_shipping_rate: CheckoutAppliedShippingRate
    billing_address: CheckoutBillingAddress
    buyer_accepts_marketing: bool
    discount_code: str
    currency: str
    email: str
    external_checkout_id: str
    external_checkout_source: str
    line_items: list[CheckoutBodyLineItem]
    note: str
    partial_shipping: bool
    order_attributes: list[CheckoutOrderAttribute]
    phone: str
    shipping_address: CheckoutShippingAddress
    shipping_line: CheckoutAppliedShippingLine


CheckoutPaymentProcessor = Literal["stripe", "braintree", "authorize"]

CheckoutPaymentType = Literal[
    "CREDIT_CARD", "PAYPAL", "APPLE_PAY", "GOOGLE_PAY", "SEPA_DEBIT"
]


class CheckoutProcessBodyOptional(TypedDict, total=False):
    payment_type: CheckoutPaymentType


class CheckoutProcessBody(TypedDict):
    payment_processor: CheckoutPaymentProcessor
    payment_token: str


class CheckoutResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/checkouts
    """

    object_list_key = "checkouts"
    object_dict_key = "checkout"
    recharge_version: RechargeVersion = "2021-11"

    def create(self, body: CheckoutCreateBody) -> Checkout:
        """Create a new checkout.
        https://developer.rechargepayments.com/2021-11/checkouts/checkout_create
        """
        required_scopes: list[RechargeScope] = ["write_checkouts"]
        self._check_scopes(f"POST /{self.object_list_key}", required_scopes)

        data = self._http_post(self._url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Checkout(**data)

    def get(self, checkout_id: str) -> Checkout:
        """Get a checkout by ID.
        https://developer.rechargepayments.com/2021-11/checkouts/checkout_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_checkouts"]
        self._check_scopes(f"GET /{self.object_list_key}/:checkout_id", required_scopes)

        url = f"{self._url}/{checkout_id}"
        data = self._http_get(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Checkout(**data)

    def update(self, checkout_id: str, body: CheckoutUpdateBody) -> Checkout:
        """Update a checkout.
        https://developer.rechargepayments.com/2021-11/checkouts/checkout_update
        """
        required_scopes: list[RechargeScope] = ["write_checkouts"]
        self._check_scopes(f"PUT /{self.object_list_key}/:checkout_id", required_scopes)

        url = f"{self._url}/{checkout_id}"
        data = self._http_put(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Checkout(**data)

    def get_shipping(self, checkout_id: str) -> list[CheckoutShippingRate]:
        """Retrieve shipping rates for a checkout
        https://developer.rechargepayments.com/2021-11/checkouts/checkout_retrieve_shipping_address
        """
        required_scopes: list[RechargeScope] = ["read_checkouts"]
        self._check_scopes(
            f"GET /{self.object_list_key}/:checkout_id/shipping_rates", required_scopes
        )

        url = f"{self._url}/{checkout_id}/shipping_rates"
        data = self._http_get(url, expected=list, response_key="shipping_rates")
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [CheckoutShippingRate(**item) for item in data]

    def process(self, checkout_id: str, body: CheckoutProcessBody) -> Checkout:
        """Process (charge) a checkout.
        https://developer.rechargepayments.com/2021-11/checkout/checkout_process
        """
        required_scopes: list[RechargeScope] = ["write_checkouts"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:checkout_id/charge", required_scopes
        )

        url = f"{self._url}/{checkout_id}/charge"
        data = self._http_post(url, body, response_key="checkout_charge")
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Checkout(**data)
