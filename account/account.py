"""
Description: Module 06 demonstration -
    Class: A class that maintains bank accounts 
    at PiXELL River.
Author: {student name}
Date: {current date}
Usage: To incorporate this class into a class or 
program, import this using:
from account.account_type import Account 
"""

from account.account_type import AccountType

## CLASS
# given docstring for class
"""
A class that maintains bank account data.

Attributes:
    _account_type (AccountType): The type of bank account.
    _account_number (int): Account number of the bank account.
    _balance (float): Balance of the bank account.

Methods (instance methods):
    update_balance(): Modifies the balance of the bank account.
"""
# camelCase
# PascalCase

class Account:
    def __init__(self, account_type: str, account_num: int, balance: float):
        try:
            self._account_type = AccountType[account_type.upper()]
        except: 
            raise ValueError("Invalid account type")
        
        try:
            self._account_number = int(account_num)
        except:
            raise ValueError("Account number must be whole number")
        
        if account_num < 0:
            raise ValueError("Account number must be positive")
        
        try:
            self._balance = float(balance)
        except ValueError:
            raise ValueError("Balance must be wholly numeric")
        
    @property
    def account_type(self) -> AccountType:
        """
        Accessor of _account_type attribute
        """
        return self._account_type
    
    @property
    def account_number(self) -> int:
        """
        Accessor for account number
        """
        return self._account_number
    
    @property
    def balance(self) -> float:
        """
        Accessor for balance
        """
        return self._balance




## __INIT__
# given docstring for __init__
"""
Initialize a new account object with an account type,
account number and balance.
Args:
    account_type(str): The account type for the account.
    account_number(int): The account number for the account.
    balance (float): The balance of the account.
Returns:
    None
Raises:
    ValueError: When the account type is invalid.
    ValueError: When the account number is non-numeric.
    ValueError: When the account number is negative.
    ValueError: When the balance is non-numeric.
"""

## ACCESSORS

## MUTATORS
# given docstring for account type mutator:
"""
Sets the account type of the Account.
Args:
    value (str): The type of account.
Raises:
    ValueError: When the value provided is 
    not a valid AccountType.
"""

# given docstring for acount number mutator:
"""
Sets the account number of the Account.
Args:
    value (int): The account number.
Raises:
    ValueError: When the value provided not numeric.
    ValueError: When the value provided is negative.
"""

# given docstring for balance mutator:
"""
Sets the balance of the Account.
Args:
    value (float): The account balance.
Raises:
    ValueError: When the value provided not numeric.
"""


## __REPR__
# given docstring for __repr__
"""
Provides a representation of an Account object.
Returns:
    str: A representation of a bank account.
        format: account_type | account_number | balance
        example: [AccountType.MORTGAGE | 1234567 | -493912.53]
"""

## __STR__
# given docstring for __str__
"""
Returns a string representation of the class.
Returns:
    str:  A string representation of a bank account.
        format:  Type: AccountType
                Account Number: account number
                Balance: $balance
        example:
                Type: Mortgage
                Account Number: 1234567
                Balance: $-493,912.53    
"""

## UPDATE_BALANCE
# given docstring for update_balance()
"""
Update the balance of the account.  All deposits (+) are 
permitted.  Withdraws (-) are only permitted if sufficient funds.

Args:
    amount(float): amount of transaction.  Positive values 
    are deposited, negative values are withdrawn.

Returns:
    None
Raises:
    ValueError: When the amount is non-numeric.
    ValueError: When there are insufficient funds.
"""