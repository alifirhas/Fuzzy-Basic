from FungsiKeanggotaan import *

def main():
    fk = FungsiKeanggotaan()

    # ! Kurva Linear
    # a = 10
    # b = 20
    # nilai = 17
    # derajat1 = fk.liniear_naik(a, b, nilai)
    # derajat2 = fk.liniear_turun(a, b, nilai)

    # print("Kurva Linear")
    # print(derajat1)
    # print(derajat2)

    # ! Kurva Segitiga
    # a = 15
    # b = 25
    # c = 35
    # nilai = 30
    # derajat = fk.segitiga(a, b, c, nilai)
    
    # print("Kurva Segitiga")
    # print(derajat)

    # ! Kurva Trapesium
    a = 15
    b = 24
    c = 27
    d = 35
    nilai = 24
    derajat = fk.trapesium(a, b, c, d, nilai)
    
    print("Kurva Trapesium")
    print(derajat)

if __name__ == '__main__':
    main()