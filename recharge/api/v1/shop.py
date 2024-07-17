from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v1.shop import ShippingCountry, Store


class ShopResource(RechargeResource):
    """
    https://developer.rechargepayments.com/v1#shop
    """

    object_list_key = "shop"
    object_dict_key = "store"
    recharge_version: RechargeVersion = "2021-01"

    def get(self) -> Store:
        """Retrieve store using the Recharge API.
        https://developer.rechargepayments.com/2021-01/shop/shop_retrieve
        """
        required_scopes: list[RechargeScope] = ["store_info"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Store(**data)

    def shipping_countries(self) -> list[ShippingCountry]:
        """Retrieve shipping countries where items can be shipped.
        https://developer.rechargepayments.com/2021-01/shop/shop_shipping_countries
        """
        required_scopes: list[RechargeScope] = ["store_info"]
        self._check_scopes("GET /shipping_countries", required_scopes)

        url = f"{self._url}/shipping_countries"
        data = self._http_get(url, expected=list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [ShippingCountry(**item) for item in data]
