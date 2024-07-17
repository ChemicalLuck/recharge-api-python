from recharge.api import RechargeResource, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v1.token import TokenInformation


class TokenResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/token_information/token_information_object
    """

    object_list_key = "token_information"
    object_dict_key = "token_information"
    recharge_version: RechargeVersion = "2021-01"

    def get(self) -> TokenInformation:
        """Get token information.
        https://developer.rechargepayments.com/2021-01/token_information/token_information_retrieve
        """
        data = self._http_get(self._url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return TokenInformation(**data)
