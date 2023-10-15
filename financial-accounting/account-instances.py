import accounts




cash = Cash('Cash', '23-10-05', 500_000)  # You must provide a begin_balance value here



print(cash.ledger)
cash.debit('23-10-08', 'Purchase of groceries', 200.53)
cash.debit('23-10-09', 'Purchase of cat food', 100.53)
cash.credit('23-10-10', 'Sale of cat', 500.53)
cash.debit('23-10-10', 'Purchase of new car', 20_000.53)
print(cash.ledger)
print(cash.balance)
#print(*cash.transactions, sep='\n')