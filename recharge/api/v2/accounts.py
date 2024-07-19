from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v2.account import Account


class AccountResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/accounts
    """

    object_list_key = "accounts"
    object_dict_key = "account"
    recharge_version: RechargeVersion = "2021-11"

    def get(self, account_id: str) -> Account:
        """Get an account.
        https://developer.rechargepayments.com/2021-11/accounts/account_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_accounts"]
        self._check_scopes(f"GET /{self.object_list_key}/:account_id", required_scopes)

        url = f"{self._url}/{account_id}"
        data = self._http_get(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Account(**data)

    def list_(self) -> list[Account]:
        """List accounts.
        https://developer.rechargepayments.com/2021-11/accounts/accounts_list
        """
        required_scopes: list[RechargeScope] = ["read_accounts"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url, expected=list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Account(**item) for item in data]

    def list_all(self) -> list[Account]:
        """List all accounts.
        https://developer.rechargepayments.com/2021-11/accounts/accounts_list
        """
        required_scopes: list[RechargeScope] = ["read_accounts"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._paginate(self._url)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Account(**item) for item in data]
