class Transaction(object):
    def __init__(self, fr, to, cost):
        assert cost < fr.assets()
            
        record(fr, to, cost)
        

class Account(object):
    def __init__(self, id):
        self.id = id
        

    def assets(self):
        return get_assets(self)


    def buy(self, other, cost):
        Transaction(self, other, cost)


    def sell(self, other, cost):
        Transaction(other, self, cost)
