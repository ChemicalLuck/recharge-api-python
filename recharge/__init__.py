import logging
from typing import Optional

from requests import Session

import recharge.api.v1 as v1
import recharge.api.v2 as v2
from recharge.api import RechargeScope


class RechargeAPIv1Helper:
    def __init__(
        self,
        session: Session,
        logger: Optional[logging.Logger] = None,
        scopes: list[RechargeScope] = [],
    ):
        kwargs = {
            "session": session,
            "logger": logger or logging.getLogger(__name__),
            "scopes": scopes,
        }

        self.Address = v1.AddressResource(**kwargs)
        self.Charge = v1.ChargeResource(**kwargs)
        self.Checkout = v1.CheckoutResource(**kwargs)
        self.Customer = v1.CustomerResource(**kwargs)
        self.Order = v1.OrderResource(**kwargs)
        self.Subscription = v1.SubscriptionResource(**kwargs)
        self.Onetime = v1.OnetimeResource(**kwargs)
        self.Discount = v1.DiscountResource(**kwargs)
        self.Webhook = v1.WebhookResource(**kwargs)
        self.Metafield = v1.MetafieldResource(**kwargs)
        self.Shop = v1.ShopResource(**kwargs)
        self.Product = v1.ProductResource(**kwargs)
        self.AsyncBatch = v1.AsyncBatchResource(**kwargs)
        self.Notification = v1.NotificationResource(**kwargs)
        self.Token = v1.TokenResource(**kwargs)


class RechargeAPIv2Helper:
    def __init__(
        self,
        session: Session,
        logger: Optional[logging.Logger] = None,
        scopes: list[RechargeScope] = [],
    ):
        kwargs = {
            "session": session,
            "logger": logger or logging.getLogger(__name__),
            "scopes": scopes,
        }

        self.Address = v2.AddressResource(**kwargs)
        self.BundleSelection = v2.BundleSelectionResource(**kwargs)
        self.Charge = v2.ChargeResource(**kwargs)
        self.Checkout = v2.CheckoutResource(**kwargs)
        self.Collection = v2.CollectionResource(**kwargs)
        self.Customer = v2.CustomerResource(**kwargs)
        self.Discount = v2.DiscountResource(**kwargs)
        self.Metafield = v2.MetafieldResource(**kwargs)
        self.Notification = v2.NotificationResource(**kwargs)
        self.Onetime = v2.OnetimeResource(**kwargs)
        self.Order = v2.OrderResource(**kwargs)
        self.PaymentMethod = v2.PaymentMethodResource(**kwargs)
        self.Plan = v2.PlanResource(**kwargs)
        self.RetentionStrategy = v2.RetentionStrategyResource(**kwargs)
        self.Subscription = v2.SubscriptionResource(**kwargs)
        self.Webhook = v2.WebhookResource(**kwargs)
        self.AsyncBatch = v2.AsyncBatchResource(**kwargs)
        self.Token = v2.TokenResource(**kwargs)
        self.Account = v2.AccountResource(**kwargs)
        self.Event = v2.EventResource(**kwargs)
        self.Store = v2.StoreResource(**kwargs)


class RechargeAPI(object):
    def __init__(self, access_token: str, logger: Optional[logging.Logger] = None):
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-Recharge-Access-Token": access_token,
        }
        self.session = Session()
        self.session.headers.update(self.headers)

        kwargs = {
            "session": self.session,
            "logger": logger or logging.getLogger(__name__),
        }

        from recharge.api.v1 import TokenResource

        self.Token = TokenResource(**kwargs)

        self.scopes = self.Token.get()["scopes"]

        kwargs["scopes"] = self.scopes

        self.v1 = RechargeAPIv1Helper(**kwargs)
        self.v2 = RechargeAPIv2Helper(**kwargs)


__all__ = ["RechargeAPI"]
