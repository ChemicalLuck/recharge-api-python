from .resources import (
    RechargeAddress,
    RechargeCharge,
    RechargeCheckout,
    RechargeCustomer,
    RechargeOrder,
    RechargeSubscription,
    RechargeOnetime,
    RechargeDiscount,
    RechargeWebhook,
    RechargeMetafield,
    RechargeShop,
    RechargeProduct
)


class RechargeAPI(object):

    def __init__(self, access_token=None, log_debug=False):
        self.access_token = access_token
        self.log_debug = log_debug

        kwargs = {
            'access_token': access_token,
            'log_debug': log_debug,
        }

        self.Address = RechargeAddress(**kwargs)
        self.Charge = RechargeCharge(**kwargs)
        self.Checkout = RechargeCheckout(**kwargs)
        self.Customer = RechargeCustomer(**kwargs)
        self.Order = RechargeOrder(**kwargs)
        self.Subscription = RechargeSubscription(**kwargs)
        self.Onetime = RechargeOnetime(**kwargs)
        self.Discount = RechargeDiscount(**kwargs)
        self.Webhook = RechargeWebhook(**kwargs)
        self.Metafield = RechargeMetafield(**kwargs)
        self.Shop = RechargeShop(**kwargs)
        self.Product = RechargeProduct(**kwargs)
