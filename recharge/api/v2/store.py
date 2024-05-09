from recharge.api import RechargeResource, RechargeScope


class StoreResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/store
    """

    object_list_key = "store"

    def get(self):
        """Get store information.
        https://developer.rechargepayments.com/2021-11/store/store_retrieve
        """
        required_scopes: list[RechargeScope] = ["store_info"]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(f"{self.url}")
