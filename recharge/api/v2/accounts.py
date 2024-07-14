from recharge.api import RechargeResource, RechargeScope, RechargeVersion


class AccountResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/accounts
    """

    object_list_key = "accounts"
    recharge_version: RechargeVersion = "2021-11"

    def get(self, account_id: str):
        """Get an account.
        https://developer.rechargepayments.com/2021-11/accounts/account_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_accounts"]
        self.check_scopes(f"GET /{self.object_list_key}/:account_id", required_scopes)

        return self._http_get(f"{self.url}/{account_id}")

    def list_(self):
        """List accounts.
        https://developer.rechargepayments.com/2021-11/accounts/accounts_list
        """
        required_scopes: list[RechargeScope] = ["read_accounts"]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self.url)
