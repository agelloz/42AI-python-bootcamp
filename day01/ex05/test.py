from the_bank import Account
from the_bank import Bank

thebank = Bank()
acc1 = Account("test", value=100, zip=75000, addr='1 Boulevard Bessieres')
acc2 = Account("test2", value=50, zip=3454, addr='rgreg')
acc3 = Account("test3")
thebank.add(acc1)
thebank.add(acc2)
thebank.add(acc3)
thebank.transfer('test', 'test2', 50)
thebank.transfer(1, 'test2', 50)
thebank.transfer(1, 'test2', 50)
thebank.fix_account('test3')
