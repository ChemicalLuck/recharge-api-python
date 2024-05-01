from recharge.api.notifications import NotificationResource
from recharge.api.addresses import AddressResource
from recharge.api.charges import ChargeResource
from recharge.api.checkouts import CheckoutResource
from recharge.api.customers import CustomerResource
from recharge.api.orders import OrderResource
from recharge.api.subscriptions import SubscriptionResource
from recharge.api.onetimes import OnetimeResource
from recharge.api.discounts import DiscountResource
from recharge.api.webhooks import WebhookResource
from recharge.api.metafields import MetafieldResource
from recharge.api.shop import ShopResource
from recharge.api.products import ProductResource
from recharge.api.async_batches import AsyncBatchResource
from recharge.api.tokens import TokenResource


class RechargeAPI(object):
    def __init__(self, access_token=None, debug=False):
        self.access_token = access_token
        self.debug = debug

        kwargs = {
            "access_token": access_token,
            "log_debug": debug,
        }

        self.Token = TokenResource(**kwargs)
        self.scopes = self.Token.get()["scopes"]

        kwargs["scopes"] = self.scopes

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
