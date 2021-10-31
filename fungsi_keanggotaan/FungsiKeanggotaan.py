class FungsiKeanggotaan:
    def __init__(self):
        pass

    def liniear_naik(self, a: int, b: int, x: int):
        """Menghitung derajat keangotaan kurva linear naik

        Args:
            a (int): nilai awal
            b (int): nilai batas
            x (int): nilai yang dihitung

        Returns:
            float / int : derajat keanggotaan 
        """
        if x <= a:
            return 0
        elif x >= b:
            return 1
        elif x > a and x < b:
            return (x-a)/(b-a)
        return False

    def liniear_turun(self, a: int, b: int, x: int):
        """Menghitung derajat keangotaan kurva linear turun

        Args:
            a (int): nilai awal
            b (int): nilai batas
            x (int): nilai yang dihitung

        Returns:
            float / int : derajat keanggotaan 
        """
        if x <= a:
            return 1
        elif x >= b:
            return 0
        elif x > a and x < b:
            return (b-x)/(b-a)
        return False

    def segitiga(self, a: int, b: int, c: int, x: int):
        """Menghitung derajat keangotaan kurva segitiga

        Args:
            a (int): nilai awal
            b (int): nilai tengah
            c (int): nilai batas
            x (int): nilai yang dihitung

        Returns:
            float / int : derajat keanggotaan 
        """
        if x <= a or x >= c:
            return 0
        elif x == b:
            return 1
        elif x >= a and x < b:
            return (b-x)/(b-a)
        elif x > b and x <= c:
            return (c-x)/(c-b)
        return False   

    def trapesium(self, a: int, b: int, c: int, d: int, x: int):
        """Menghitung derajat keangotaan kurva trapesium

        Args:
            a (int): nilai awal
            b (int): nilai tengah
            c (int): nilai tengah 1
            d (int): nilai batas
            x (int): nilai yang dihitung

        Returns:
            float / int : derajat keanggotaan 
        """
        if x <= a or x >= d:
            return 0
        elif x > a and x < b:
            return (x-a)/(b-a)
        elif x >= b and x <= c:
            return 1
        elif x > c and x < d:
            return (d-x)/(d-c)
        return False
