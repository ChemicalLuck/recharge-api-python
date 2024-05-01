from typing import Literal, TypeAlias

from recharge.api.v1.tokens import TokenResource


RechargeVersion: TypeAlias = Literal["2021-01", "2021-11"]


class RechargeAPI(object):
    def __init__(
        self, access_token: str, debug=False, version: RechargeVersion = "2021-01"
    ):
        self.access_token = access_token
        self.debug = debug
        self.version = version

        kwargs = {
            "access_token": access_token,
            "debug": debug,
        }

        self.Token = TokenResource(**kwargs)
        self.scopes = self.Token.get()["scopes"]

        kwargs["scopes"] = self.scopes

        if self.version == "2021-01":
            from recharge.api.v1 import (
                AddressResource,
                ChargeResource,
                CheckoutResource,
                CustomerResource,
                OrderResource,
                SubscriptionResource,
                OnetimeResource,
                DiscountResource,
                WebhookResource,
                MetafieldResource,
                ShopResource,
                ProductResource,
                AsyncBatchResource,
                NotificationResource,
            )
        elif self.version == "2021-11":
            raise NotImplementedError("2021-11 is not yet implemented")
        else:
            raise ValueError(f"Unknown version: {self.version}")

        self.Address = AddressResource(**kwargs)
        self.Charge = ChargeResource(**kwargs)
        self.Checkout = CheckoutResource(**kwargs)
        self.Customer = CustomerResource(**kwargs)
        self.Order = OrderResource(**kwargs)
        self.Subscription = SubscriptionResource(**kwargs)
        self.Onetime = OnetimeResource(**kwargs)
        self.Discount = DiscountResource(**kwargs)
        self.Webhook = WebhookResource(**kwargs)
        self.Metafield = MetafieldResource(**kwargs)
        self.Shop = ShopResource(**kwargs)
        self.Product = ProductResource(**kwargs)
        self.AsyncBatch = AsyncBatchResource(**kwargs)
        self.Notification = NotificationResource(**kwargs)


__all__ = ["RechargeAPI", "RechargeVersion"]
