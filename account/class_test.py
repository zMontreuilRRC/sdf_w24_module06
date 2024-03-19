from account.account import Account
from account.account_type import AccountType

import unittest

class AccountTests(unittest.TestCase):
    def test_account_type_accessor(self):
        actual_type = AccountType.SAVINGS
        account = Account('SAVINGS', 99999, 100.00)

        self.assertEqual(account.account_type, actual_type)