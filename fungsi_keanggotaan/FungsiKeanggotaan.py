class FungsiKeanggotaan:
    def __init__(self):
        pass

    def liniear_naik(self, a, b, x):
        if x <= a:
            return 0
        elif x >= b:
            return 1
        elif x > a and x < b:
            return (x-a)/(b-a)
        return False

    def liniear_turun(self, a, b, x):
        if x <= a:
            return 1
        elif x >= b:
            return 0
        elif x > a and x < b:
            return (b-x)/(b-a)
        return False

    def segitiga(self, a, b, c, x):
        if x <= a or x >= c:
            return 0
        elif x == b:
            return 1
        elif x >= a and x < b:
            return (b-x)/(b-a)
        elif x > b and x <= c:
            return (c-x)/(c-b)
        return False   

    def trapesium(self):
        return "Ini Trapesium"  

# fk = FungsiKeanggotaan();

# print(fk.liniear())