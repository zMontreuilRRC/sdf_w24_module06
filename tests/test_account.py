from account.account import Account
from account.account_type import AccountType

import unittest

class AccountTests(unittest.TestCase):
    def test_class_init_valid_inputs_succeeds(self):
        actual_type = AccountType.MORTGAGE
        actual_number = 123456
        actual_balance = 123.45

        test_account = Account("Mortgage", actual_number, actual_balance)

        self.assertEqual(test_account.account_type, actual_type)
        self.assertEqual(test_account.account_number, actual_number)
        self.assertEqual(test_account.balance, actual_balance)

    def test_class_init_invalid_type_raises_valueerror(self):
        actual_number = 123456
        actual_balance = 123.45

        expected_message = "Invalid account type"

        with self.assertRaises(ValueError) as context:
            test_account = Account("Martgage", 
                                   actual_number, 
                                   actual_balance)
            
        self.assertEqual(expected_message, str(context.exception))