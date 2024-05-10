from recharge.api import RechargeResource, RechargeScope


class ShopResource(RechargeResource):
    """
    https://developer.rechargepayments.com/v1#shop
    """

    object_list_key = "shop"

    def get(self):
        """Retrieve store using the Recharge API.
        https://developer.rechargepayments.com/2021-01/shop/shop_retrieve
        """
        required_scopes: list[RechargeScope] = ["store_info"]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(f"{self.url}")

    def shipping_countries(self):
        """Retrieve shipping countries where items can be shipped.
        https://developer.rechargepayments.com/2021-01/shop/shop_shipping_countries
        """
        required_scopes: list[RechargeScope] = ["store_info"]
        self.check_scopes("GET /shipping_countries", required_scopes)

        return self._http_get(f"{self.url}/shipping_countries")
