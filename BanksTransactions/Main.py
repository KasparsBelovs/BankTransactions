from HandelsBanken.GetHandelsbankenAccount import *
from HandelsBanken.GetHandelsbankenAccounts import *
from HandelsBanken.GetHandelsbankenAccountTransactions import *
from SebBank.GetSebBankAccounts import *
from SebBank.GetSebBankAccount import *
from SebBank.GetSebBankAccountBalance import *
from SebBank.GetSebBankAccountTransactions import *
from SebBank.GeSebBankAccountSpecificTransaction import *

handelsbankenAccountId = 'ae57e780-6cf3-11e9-9c41-e957ce7d7d69'

#sebBankToken should be obtained and changed before start, Sandbox Identification Number = 9311219639
sebBankToken = '7kuGZUjOrZwUQ8zM6Fqk'
sebBankAccountId = '5a59028c-e757-4f22-b88c-3ba90573383c'
sebBankTransactionId = '6f24de7e-9f81-4f09-999a-b33bead16e8d'

#handelsbankenAccounts = GetHandelsbankenAccounts()
#handelsbankenAccount = GetHandelsbankenAccount(handelsbankenAccountId)
#handelsbankenAccountTransactions = GetHandelsbankenAccountTransactions(handelsbankenAccountId)

#sebBankAccounts = GetSebBankAccounts(sebBankToken)
#sebBankAccount = GetSebBankAccount(sebBankToken, sebBankAccountId)
#sebBankAccountBalance = GetSebBankAccountBalance(token = sebBankToken, account=sebBankAccountId)
#sebBankAccountTransactions = GetSebBankAccountTransactions(sebBankToken, sebBankAccountId)
#sebBankAccountSpecificTransaction = GeSebBankAccountSpecificTransaction(sebBankToken, sebBankAccountId, sebBankTransactionId)

#handelsbankenAccounts.run()
#handelsbankenAccount.run()
#handelsbankenAccountTransactions.run()

#sebBankAccounts.run()
#sebBankAccount.run()
#sebBankAccountBalance.run()
#sebBankAccountTransactions.run()
#sebBankAccountSpecificTransaction.run()
handelsbankenActionChoise = None
sebActionChoise = None

print('Choose whitch banke to use:')
print('1 HandelsBanken')
print('2 SebBank')
print('0. To Exit')
bankChoise = input()

if(int(bankChoise) == 1): 
    print('Choose what to get:')
    print('1 get handelsbanken Accounts')
    print('2 get handelsbanken Account')
    print('3 get handelsbanken Account Transactions')
    print('0 To Exit')
    handelsbankenActionChoise = input()
elif(int(bankChoise) == 2):
    print('Choose what to get:')
    print('1 get sebBank Accounts')
    print('2 get sebBank Account')
    print('3 get sebBank Account Balance')
    print('4 get sebBank Account Transactions')
    print('5 get sebBank Account Specific Transactions')
    print('0 To Exit')
    sebActionChoise = input()
elif(int(bankChoise) == 0):
     print('Good bye')
else:
    print('Wrong input')

if (handelsbankenActionChoise == None):
    pass
elif(int(handelsbankenActionChoise) == 1):
    handelsbankenAccounts = GetHandelsbankenAccounts()
    handelsbankenAccounts.run()
elif(int(handelsbankenActionChoise) == 2):
    handelsbankenAccount = GetHandelsbankenAccount(handelsbankenAccountId)
    handelsbankenAccount.run()
elif(int(handelsbankenActionChoise) == 3):
    handelsbankenAccountTransactions = GetHandelsbankenAccountTransactions(handelsbankenAccountId)
    handelsbankenAccountTransactions.run()
elif(int(handelsbankenActionChoise) == 0):
     print('Good bye')

if (sebActionChoise == None):
    pass   
elif(int(sebActionChoise) == 1):
    sebBankAccounts = GetSebBankAccounts(sebBankToken)
    sebBankAccounts.run()
elif(int(sebActionChoise) == 2):
    sebBankAccount = GetSebBankAccount(sebBankToken, sebBankAccountId)
    sebBankAccount.run()
elif(int(sebActionChoise) == 3):
    sebBankAccountBalance = GetSebBankAccountBalance(token = sebBankToken, account=sebBankAccountId)
    sebBankAccountBalance.run()
elif(int(sebActionChoise) == 4):
    sebBankAccountTransactions = GetSebBankAccountTransactions(sebBankToken, sebBankAccountId)
    sebBankAccountTransactions.run()
elif(int(sebActionChoise) == 5):
    sebBankAccountSpecificTransaction = GeSebBankAccountSpecificTransaction(sebBankToken, sebBankAccountId, sebBankTransactionId)
    sebBankAccountSpecificTransaction.run()
elif(int(sebActionChoise) == 0):
     print('Good bye')