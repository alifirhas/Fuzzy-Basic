# Penjelasan Cara Kerja

## Kurva Linear

Kurva Linear akan mengambil 2 masukan yaitu
  
- a : titik awal
- b : titik akhir

Kurva Linear dibedakan menjadi 2 jenis, yaitu

- Kurva Linear Naik --> a > b
- Kurva Linear Turun --> a < b

### Kurva Linear Naik

![](../attachments/2021-10-30-20-26-22.png)

Rumus untuk menentukan derajat keanggotaan dari suatu nilai pada Kurva Linear Naik adalah dengan menggunakan rumus berikut

![](../attachments/2021-10-30-20-28-10.png)

Yang diterjemahkan dalam bentuk Flowchart sebagai

![](../attachments/Fungsi-Keanggotaan-Linear-Naik.jpg)

Yang diterjemahkan ke dalam bentuk program python, menjadi

```python
a = 10
b = 20
nilai = 15
derajat = 0

def linear_naik(a, b, x):
    if x <= a:
        return 0
    elif x >= b:
        return 1
    elif x > a and x < b:
        return (x-a)/(b-a)

derajat = linear_naik(a, b, nilai)

```

Rumus yang digunakan mendapat sedikit penyeseuain pada, karena dengan rumus seperti ini akan memiliki tipe data output

```
a < x           -> Output Int
a <= x <= b     -> Output Float/Double
b > x           -> Output Int
```

Tetapi jika nilai "x" merupakan nilai yang sama dengan nilai "b" atau "a", maka output yang dikerluarkan ``` a <= x <= b ``` akan menjadi nilai 0.0 atau 1.0 karena nilai "x" mengalami proses perhitungan, jadi rumus akan diubah seperti ini

```
a <= x      -> Output Int
a < x < b   -> Output Float/Double
b >= x      -> Output Int
```

Dengan seperti diatas maka tidak akan ada output nilai 0 atau 1 dengan tipe data Float/Double.
* * *

### Kurva Linear Turun

![](../attachments/2021-10-30-21-53-45.png)

Rumus untuk menentukan derajat keanggotaan dari suatu nilai pada Kurva Linear Naik adalah dengan menggunakan rumus berikut

![](../attachments/2021-10-30-21-54-19.png)

Yang diterjemahkan dalam bentuk Flowchart sebagai

![](../attachments/Fungsi-Keanggotaan-Linear-Turun.jpg)

Yang diterjemahkan ke dalam bentuk program python, menjadi

```python
a = 10
b = 20
nilai = 15
derajat = 0

def linear_turun(a, b, x):
    if x <= a:
        return 1
    elif x >= b:
        return 0
    elif x > a and x < b:
        return (b-x)/(b-a)
    return False

derajat = linear_turun(a, b, nilai)

```

Rumus juga mendapat penyesuaian sama dengan Kurva Linear Naik

```
a < x           -> Output Int
a <= x <= b     -> Output Float/Double
b > x           -> Output Int
```

* * *

## Kurva Segitiga



* * *
## Kurva Trapesium


