
class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
             self.value = self.__dict__['value']
        else:
             self.value = 0
        Account.ID_COUNT += 1
        
    def transfer(self, amount):
        self.value += amount

class Bank(object):
    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def account_corrupted(self, acc):
        zip = False
        addr = False
        for att in acc.__dict__:
            if (len(acc.__dict__) % 2 == 0 or att[0] == 'b'
                or 'name' not in acc.__dict__
                or 'id' not in acc.__dict__
                or 'value' not in acc.__dict__):
                return True
            if 'zip' in att:
                zip = True
            if 'addr' in att:
                addr = True
        if zip is False or addr is False:
            return True
        return False

    def account_exists(self, name_id):
        if isinstance(name_id, int) is False and isinstance(name_id, str) is False:
            return None
        acc = None
        for account in self.account:
            if account.id is name_id or account.name is name_id:
                acc = account
        return acc

    def transfer(self, origin, dest, amount):
        if ((isinstance(amount, float) is False and isinstance(amount, int) is False)
            or amount <= 0.0):
            print("TypeError: incorrect transfert amount.")
            return False
        acc1 = self.account_exists(origin)
        acc2 = self.account_exists(dest)
        if (acc1 is None or acc2 is None or acc1 is acc2
            or self.account_corrupted(acc1) is True
            or self.account_corrupted(acc2) is True):
            print("TypeError: incorrect accounts.")
            return False
        if acc1.value < amount:
            print("Error: unsufficient amount on account " + acc1.name + " (" + str(acc1.id) + ")")
            return False
        acc1.transfer(-amount)
        acc2.transfer(amount)
        return True

    def fix_account(self, account):
        acc = self.account_exists(account)
        if acc is None:
            print("TypeError: fix incorrect account.")
            return False
        if self.account_corrupted(acc) is False:
            print("Error: this account is not corrupted.")
            return False
