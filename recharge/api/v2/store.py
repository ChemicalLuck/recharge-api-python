from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v2.store import Store


class StoreResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/store
    """

    object_list_key = "store"
    object_dict_key = "store"
    recharge_version: RechargeVersion = "2021-11"

    def get(self) -> Store:
        """Get store information.
        https://developer.rechargepayments.com/2021-11/store/store_retrieve
        """
        required_scopes: list[RechargeScope] = ["store_info"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Store(**data)
