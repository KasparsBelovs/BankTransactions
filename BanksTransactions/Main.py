from HandelsBanken.GetHandelsbankenAccount import *
from HandelsBanken.GetHandelsbankenAccounts import *
from HandelsBanken.GetHandelsbankenAccountTransactions import *
from SebBank.GetSebBankAccounts import *
from SebBank.GetSebBankAccount import *
from SebBank.GetSebBankAccountBalance import *
from SebBank.GetSebBankAccountTransactions import *
from SebBank.GeSebBankAccountSpecificTransaction import *

handelsbankenAccountId = 'ae57e780-6cf3-11e9-9c41-e957ce7d7d69'
#Token should be obtained and changed before start
sebBankToken = '5GrdaJl615IpyBf1cJ5M'
sebBankAccountId = '5a59028c-e757-4f22-b88c-3ba90573383c'
sebBankTransactionId = '6f24de7e-9f81-4f09-999a-b33bead16e8d'

handelsbankenAccounts = GetHandelsbankenAccounts()
handelsbankenAccount = GetHandelsbankenAccount(handelsbankenAccountId)
handelsbankenAccountTransactions = GetHandelsbankenAccountTransactions(handelsbankenAccountId)

sebBankAccounts = GetSebBankAccounts(sebBankToken)
sebBankAccount = GetSebBankAccount(sebBankToken, sebBankAccountId)
sebBankAccountBalance = GetSebBankAccountBalance(sebBankToken, sebBankAccountId)
sebBankAccountTransactions = GetSebBankAccountTransactions(sebBankToken, sebBankAccountId)
sebBankAccountSpecificTransaction = GeSebBankAccountSpecificTransaction(sebBankToken, sebBankAccountId, sebBankTransactionId)

#handelsbankenAccounts.run()
#handelsbankenAccount.run()
#handelsbankenAccountTransactions.run()

#sebBankAccounts.run()
#sebBankAccount.run()
#sebBankAccountBalance.run()
#sebBankAccountTransactions.run()
sebBankAccountSpecificTransaction.run()