from recharge.api import RechargeResource, RechargeScope


class ShopResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/store
    """

    object_list_key = "store"

    def get(self):
        """Retrieve store using the Recharge API.
        https://developer.rechargepayments.com/2021-11/shop/shop_retrieve
        """
        required_scopes: list[RechargeScope] = ["store_info"]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(f"{self.url}")
