from recharge.api import RechargeResource, RechargeScope, RechargeVersion


class StoreResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/store
    """

    object_list_key = "store"
    recharge_version: RechargeVersion = "2021-11"

    def get(self):
        """Get store information.
        https://developer.rechargepayments.com/2021-11/store/store_retrieve
        """
        required_scopes: list[RechargeScope] = ["store_info"]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self.url)
