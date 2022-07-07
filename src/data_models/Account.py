from src.data_models.Entity import Entity
from decimal import Decimal

_collection_name = "account"

class Account(Entity):
    """
    Holds account data.
    """

    def __init__(self, account_id: str):
        """
        Creates a new account.

        Parameters
        ----------
        account_id: str
            The id of the account.

        Raises
        ------
        ValueError
            Raised if the account id is undefined.
        """

        super().__init__(_collection_name)

        self.__validate_account_id(account_id)

        self.id = self.create_id(account_id)
        self.account_id = account_id
        self.account_name = ""
        self.account_type = ""
        self.account_institution = ""
        self.balance = Decimal("0.00")

    def __init__(self, account_id: str, account_name: str, account_type: str, account_institution: str, balance: Decimal):
        """
        Creates a new account.
        
        Parameters
        ----------
        account_id: str
            The id of the account.

        account_name: str
            The name of the account.

        account_type: str
            The type of account.

        account_institution: str
            The institution that manages this account.

        balance: Decimal
            The monetary balance on this account.

        Raises
        ------
        ValueError
            Raised if the account_id, account_name, account_type, or account_institution are undefined.

        TypeError
            Raised if the amount is undefined.
        """

        self.__validate_params(account_id, account_name, account_type, account_institution, balance)

        self.id = self.create_id(account_id)
        self.account_id = account_id
        self.account_name = account_name
        self.account_type = account_type
        self.account_institution = account_institution
        self.balance = balance


    def __validate_account_id(self, account_id: str):
        if not account_id or account_id.isspace():
            raise ValueError("'account_id' must be defined.")


    def __validate_params(self,account_id: str, account_name: str, account_type: str, account_institution: str, balance: Decimal):
        self.__validate_account_id(account_id)

        if not account_name or account_name.isspace():
            raise ValueError("'account_name' must be defined.")

        if not account_type or account_type.isspace():
            raise ValueError("'account_type' must be defined.")

        if not account_institution or account_institution.isspace():
            raise ValueError("'account_institution' must be defined.")

        if balance == None:
            raise TypeError("'balance' must be defined.")