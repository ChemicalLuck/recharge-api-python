import logging
from typing import Optional

import recharge.api.v1 as v1
import recharge.api.v2 as v2
from recharge.client import RechargeClient
from recharge.types import RechargeScope


class RechargeAPIv1:
    def __init__(self, client: RechargeClient, scopes: list[RechargeScope]) -> None:
        kwargs = {"client": client, "scopes": scopes}
        self.Address = v1.AddressResource(**kwargs)
        self.AsyncBatch = v1.AsyncBatchResource(**kwargs)
        self.Charge = v1.ChargeResource(**kwargs)
        self.Checkout = v1.CheckoutResource(**kwargs)
        self.Customer = v1.CustomerResource(**kwargs)
        self.Discount = v1.DiscountResource(**kwargs)
        self.Metafield = v1.MetafieldResource(**kwargs)
        self.Notification = v1.NotificationResource(**kwargs)
        self.Onetime = v1.OnetimeResource(**kwargs)
        self.Order = v1.OrderResource(**kwargs)
        self.Product = v1.ProductResource(**kwargs)
        self.Shop = v1.ShopResource(**kwargs)
        self.Subscription = v1.SubscriptionResource(**kwargs)
        self.Token = v1.TokenResource(**kwargs)
        self.Webhook = v1.WebhookResource(**kwargs)


class RechargeAPIv2:
    def __init__(self, client: RechargeClient, scopes: list[RechargeScope]) -> None:
        kwargs = {"client": client, "scopes": scopes}
        self.Account = v2.AccountResource(**kwargs)
        self.Address = v2.AddressResource(**kwargs)
        self.AsyncBatch = v2.AsyncBatchResource(**kwargs)
        self.BundleSelection = v2.BundleSelectionResource(**kwargs)
        self.Charge = v2.ChargeResource(**kwargs)
        self.Checkout = v2.CheckoutResource(**kwargs)
        self.Collection = v2.CollectionResource(**kwargs)
        self.Customer = v2.CustomerResource(**kwargs)
        self.Discount = v2.DiscountResource(**kwargs)
        self.Event = v2.EventResource(**kwargs)
        self.Metafield = v2.MetafieldResource(**kwargs)
        self.Notification = v2.NotificationResource(**kwargs)
        self.Onetime = v2.OnetimeResource(**kwargs)
        self.Order = v2.OrderResource(**kwargs)
        self.PaymentMethod = v2.PaymentMethodResource(**kwargs)
        self.Plan = v2.PlanResource(**kwargs)
        self.Product = v2.ProductResource(**kwargs)
        self.RetentionStrategy = v2.RetentionStrategyResource(**kwargs)
        self.Store = v2.StoreResource(**kwargs)
        self.Subscription = v2.SubscriptionResource(**kwargs)
        self.Token = v2.TokenResource(**kwargs)
        self.Webhook = v2.WebhookResource(**kwargs)


class RechargeAPI:
    def __init__(
        self,
        access_token: str,
        logger: Optional[logging.Logger] = None,
        client: Optional[RechargeClient] = None,
    ) -> None:
        self.client = client or RechargeClient(access_token, logger=logger)

        from recharge.api.v1 import TokenResource

        token = TokenResource(self.client)
        self.scopes: list[RechargeScope] = token.get()["scopes"]

        self.v1 = RechargeAPIv1(self.client, self.scopes)
        self.v2 = RechargeAPIv2(self.client, self.scopes)


__all__ = ["RechargeAPI", "RechargeAPIv1", "RechargeAPIv2"]
