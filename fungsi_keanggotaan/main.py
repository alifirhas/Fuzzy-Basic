from FungsiKeanggotaan import *

def main():
    fk = FungsiKeanggotaan()

    a = 10
    b = 20
    nilai = 17
    derajat1 = fk.liniear_naik(a, b, nilai)
    derajat2 = fk.liniear_turun(a, b, nilai)

    print("Hello, world!")
    print(derajat1)
    print(derajat2)


if __name__ == '__main__':
    main()