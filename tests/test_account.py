import unittest

from decimal import Decimal
from src.data_models.Account import Account;

class AccountTests(unittest.TestCase):
    
    # Asserts an account is created.
    def test_create_account(self):
        # Partial constructor test.
        account = Account("some_id")

        self.assertEqual("account::some_id", account.id)

        # Full constructor test.
        account = Account("some_id", "some_name", "some_type", "some_institution", "some_owner", Decimal("100.00"))

        self.assertEqual("account::some_id", account.id)
        self.assertEqual("some_id", account.account_id)
        self.assertEqual("some_name", account.account_name)
        self.assertEqual("some_type", account.account_type)
        self.assertEqual("some_institution", account.account_institution)
        self.assertEqual("some_owner", account.account_owner_id)
        self.assertEqual(100.00, account.balance)

    # Asserts validation works on the account parameters.
    def test_account_validation(self):
        # Bad account id.
        with self.assertRaises(ValueError):
            Account(None)

        # Bad account name.
        with self.assertRaises(ValueError):
            Account("some_id", None)

        # Bad account type.
        with self.assertRaises(ValueError):
            Account("some_id", "some_name", None)

        # Bad account institution.
        with self.assertRaises(ValueError):
            Account("some_id", "some_name", "some_type", None)

        # Bad account owner id.
        with self.assertRaises(ValueError):
            Account("some_id", "some_name", "some_type", "some_institution", None)

        # Bad account balance.
        with self.assertRaises(TypeError):
            Account("some_id", "some_name", "some_type", "some_institution", "some_owner", None)

    # Asserts the to string format is correct.
    def test_account_to_str(self):
        account = Account("some_id", "some_name", "some_type", "some_institution", "some_owner", Decimal("100.00"))
        expected_str = "'id': 'account::some_id' | 'account_id': 'some_id' | 'account_name': 'some_name' | 'account_type': 'some_type' | 'account_institution': 'some_institution' | 'account_owner_id': 'some_owner' | 'balance': '$100.00'"

        self.assertEqual(expected_str, account.__str__())