from typing import TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v1.checkout import (
    Checkout,
    CheckoutAnalyticsData,
    CheckoutBillingAddress,
    CheckoutExternalCheckoutSource,
    CheckoutLineItem,
    CheckoutNoteAttribute,
    CheckoutPaymentProcessor,
    CheckoutPaymentType,
    CheckoutShippingAddress,
    CheckoutShippingRate,
    CheckoutCharge,
)


class CheckoutCreateBodyOptional(TypedDict, total=False):
    analytics_data: CheckoutAnalyticsData
    billing_address: CheckoutBillingAddress
    buyer_accepts_marketing: bool
    currency: str
    discount_code: str
    email: str
    external_checkout_id: str
    external_checkout_source: CheckoutExternalCheckoutSource
    external_checkout_customer_id: str
    note: str
    note_attributes: list[CheckoutNoteAttribute]
    phone: str
    shipping_address: CheckoutShippingAddress


class CheckoutCreateBody(CheckoutCreateBodyOptional):
    line_items: list[CheckoutLineItem]


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


class CheckoutProcessBodyOptional(TypedDict, total=False):
    payment_type: CheckoutPaymentType


class CheckoutProcessBody(CheckoutProcessBodyOptional):
    payment_processor: CheckoutPaymentProcessor
    payment_token: str


class CheckoutResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/checkouts
    """

    object_list_key = "checkouts"
    object_dict_key = "checkout"
    recharge_version: RechargeVersion = "2021-01"

    def create(self, body: CheckoutCreateBody) -> Checkout:
        """Create a new checkout.
        https://developer.rechargepayments.com/2021-01/checkouts/checkout_create
        """
        required_scopes: list[RechargeScope] = ["write_checkouts"]
        self._check_scopes(f"POST /{self.object_list_key}", required_scopes)

        data = self._http_post(self._url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Checkout(**data)

    def get(self, checkout_id: str) -> Checkout:
        """Get a checkout by ID.
        https://developer.rechargepayments.com/2021-01/checkouts/checkout_retrieve
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
        https://developer.rechargepayments.com/2021-01/checkouts/checkout_update
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
        https://developer.rechargepayments.com/2021-01/checkouts/checkout_retrieve_shipping_address
        """
        required_scopes: list[RechargeScope] = ["read_checkouts"]
        self._check_scopes(
            f"GET /{self.object_list_key}/:checkout_id/shipping_rates", required_scopes
        )

        url = f"{self._url}/{checkout_id}/shipping_rates"
        self.object_list_key = "shipping_rates"
        data = self._http_get(url, expected=list)
        self.object_list_key = "checkouts"
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [CheckoutShippingRate(**item) for item in data]

    def process(self, checkout_id: str, body: CheckoutProcessBody) -> CheckoutCharge:
        """Process (charge) a checkout.
        https://developer.rechargepayments.com/2021-01/checkout/checkout_process
        """
        required_scopes: list[RechargeScope] = ["write_checkouts"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:checkout_id/charge", required_scopes
        )

        url = f"{self._url}/{checkout_id}/charge"
        self.object_list_key = "checkout_charge"
        data = self._http_post(url, body)
        self.object_list_key = "checkouts"
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return CheckoutCharge(**data)
