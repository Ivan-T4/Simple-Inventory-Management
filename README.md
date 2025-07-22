# Simple-Inventory-Management

Proyek Python ini adalah sistem manajemen inventaris sederhana yang digunakan untuk memasukan, mengedit, menghapus informasi, dan mengambil produk menggunakan **Unique ID** setelah dicari sebelumnya berdasarkan **nama produk, client, tanggal masuk, grade produk** atau bahkan langsung menggunakkan **Unique ID**. Data disimpan dalam struktur dictionary.

## Fitur Utama

| Fitur                      | Penjelasan                                                                                                                                |
| ----------------------     | ------------------------------------------------------------------------------------------------------------------------------------------|
| Add Product                | Menambahkan produk baru beserta detailnya dan secara otomatis menghasilkan Unique ID. Penjelasan lebih ada dibagian bawah                 |
| Search Product             | Mencari produk berdasarkan Unique ID, nama produk, nama client, tanggal masuk, atau grade.                                                |
| Edit Product               | Mengedit detail produk yang ada. Unique ID akan diperbarui otomatis jika elemen penting berubah. Penjelasan lebih ada di bagian bawah     |
| Delete Product             | Menghapus produk dari inventaris.                                                                                                         |
| Takeout Product            | Mengambil produk dari inventaris. Stock produk akan otomatis berkurang jika sudah ada konfirmasi. Penjelasan lebih ada di bagian bawah |
| Show All Product details   | Menampilkan seluruh detail dari 1 produk yang telah dipilih                                                                               |
| Show All Inventory         | Menampilkan seluruh data produk dalam inventaris.                                                                                         |
| Exit                       | Menutup program atau kembali ke menu sebelumnya jika memungkinkan.                                                                        |

## Cara Pembuatan Unique ID

Unique ID dibuat berdasarkan gabungan dari beberapa elemen produk sebagai berikut:

* **2 huruf pertama nama produk**, dikonversi ke huruf kapital.
* **2 huruf pertama nama client**, dikonversi ke huruf kapital.
* **4 angka pertama Tanggal masuk** dalam format `DDMMYYYY`.
* **Kode ukuran** hasil konversi dimensi `lebar`, `panjang`, dan `tinggi` menjadi karakter.

### Contoh:

```python
Nama     = "CHAIN"
Client   = "ABCDEF"
Tanggal  = "25032025"
Ukuran   = (25, 34, 70)
```

1. Nama → `CH`
2. Client → `AB`
3. Tanggal → `2503`
4. Ukuran:

   * Lebar 25 → chr(65 + (25 % 26)) = chr(90) = `Z`
   * Panjang 34 → chr(65 + (34 % 26)) = chr(73) = `H`
   * Tinggi 70 → chr(65 + (70 % 26)) = chr(83) = `P`

Maka Unique ID: `CHAB2503ZHP`

> Konversi angka ke karakter: `65 → A`, `66 → B`, ..., `90 → Z` dst (loop dari A-Z).

## Logika pemasukan/penambahan produk baru ke inventaris

Untuk menambahkan produk, sistem menggunakan meminta detail produk yang dapat diinput user seperti:

```
1. Nama Produk
2. Client
3. Tanggal masuk produk
4. Ukuran produk(lebar, panjang, tinggi)
5. Jumlah produk yang dimasukkan
```

lalu sistem akan membuat `Unique ID` dari detail informasi produk yang telah diberikan.

Jika detail produk yang diberikan(diinput) **memiliki kesamaan dengan produk yang sudah ada** di inventaris, `Stock` dari produk yang ada di inventaris akan ditambah sesuai dengan jumlah yang user berikan/masukan.

jika detail produk yang diberikan(diinput) **hanya** memiliki kesamaan `Unique ID` dengaan produk yang sudah ada di inventaris tetapi detail dimensi atau ukuran berbeda, sistem akan **menolak** inputan tersebut dan menyarankan untuk memasukkan produk 1 hari setelahnya sehingga `Unique ID` berbeda

## Grading Ukuran Produk

Produk diklasifikasikan ke dalam 3 Grade berdasarkan volume:

| Grade | Volume (cm³)             |
| ----- | ------------------------ |
| A     | Volume ≥ 60.000          |
| B     | 10.000 ≤ Volume < 60.000 |
| C     | Volume < 10.000          |

Volume dihitung dengan rumus:

```python
volume = lebar * panjang * tinggi
```

## Logika Edit Produk

Untuk mengedit produk, sistem menggunakan pendekatan berikut:

1. Cari produk berdasarkan permintaan user (unique_id/nama produk/client/tanggal/grade).
2. pilih produk dengan memberikan Unique ID produknya.
3. Lakukan perubahan pada detail produk(nama produk/client/tanggal/ukuran) yang diinginkan.
4. Salin detailnya ke dictionary sementara (`temp_entry`).
5. Hitung ulang Unique ID berdasarkan data terbaru.
6. Simpan ke dictionary `inventory` dengan Unique ID baru.
7. Hapus ID lama dari inventaris.

### Contoh:
produk sudah dipilih menggunakan `Unique ID` = CHAB25032025ZHP, lalu sistem akan memberikan preview detail produk

```python
inventory = {
    "CHAB25032025ZHP": {
        "Nama": "CHAIN",
        "Client": "ABCDEF",
        "Tanggal": "25032025",
        "Grade": "A",
        "Stock": 30
    }
}
```

Misal user ingin mengubah `Client` menjadi "XYZ":

1. Field `Client` diganti ke XYZ.
2. Unique ID dibuat ulang menggunkan logika yang sama saat membuat `Unique ID` → `CHXY25032025ZHP`.
3. Data lama(`Unique ID`: "CHAB25032025ZHP" beserta detailnya) dihapus, data baru dimasukkan dengan `Unique ID` baru("CHXY25032025ZHP" beserta detailnya).

```python
inventory = {
    "CHXY25032025ZHP": {
        "Nama": "CHAIN",
        "Client": "XYZ",
        "Tanggal": "25032025",
        "Grade": "A",
        "Stock": 30
    }
}
```

## Logika pengambilan produk baru dari inventaris

Untuk pengambilan produk, sistem menggunakan pendekatan berikut:

1. Cari produk berdasarkan permintaan user (unique_id/nama produk/client/tanggal/grade).
2. Memilih produk dengan memberikan `Unique ID` produknya.
3. Melakukan preview produk yang ingin diambil.
4. Menanyakan jumlah atau `Stock` produk yang akan diambil.*
5. Mengurangi `Stock` produk dari inventaris setelah ada konfirmasi pengambilan.**

*: jika `Stock` produk yang ingin diambil **lebih banyak** dari yang ada di inventaris, permintaan pengambilan akan dibatalkan.
**: jika `Stock` produk di inventari menjadi **0** setelah adanya pengambilan, maka detail produk akan dihapus dari inventaris.

## Batasan Pemprogramman & Perlakuan Khusus

### 1. Penambahan Produk dengan ID Sama

Jika produk baru memiliki `Unique ID` yang sudah digunakan, sistem akan menolak penambahan tersebut **meskipun detail ukuran berbeda**. Hal ini dilakukan untuk menjaga Unique ID dan sebagai gantinya sistem memberikan
saran untuk **memasukkan produk 1 hari setelahnya** supaya `Unique ID` berbeda

### 2. Edit Produk Menjadi ID yang Sudah Ada

Jika hasil edit membuat produk memiliki `Unique ID` yang sama dengan produk lain di inventaris, sistem juga akan error karena `temp_entry` memiliki `Unique ID` yang sama dengan produk yang ada di inventory dictionary sehingga tidak bisa dibuat dan dimasukkan kedalam inventory dictionary.



## Bahasa

Kode ini sebagian menggunakan Bahasa Indonesia karena banyak instruksi user input dan beberapa variable menggunakan Bahasa Indonesia. Namun mayoritas penamaan variabel atau nama function tetap jelas dengan Bahasa Inggris agar dapat dipahami secara umum.

---
