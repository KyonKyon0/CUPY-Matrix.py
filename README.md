# Program CuPy/NuPy Loop

## Deskripsi
Program ini adalah skrip berbasis Python yang digunakan untuk menguji performa CuPy/Numpy dalam operasi matriks dan loop. Program ini menyediakan antarmuka interaktif bagi pengguna untuk memasukkan jumlah loop dan ukuran matriks acak yang akan diproses.

## Fitur
- Menampilkan informasi sistem sebelum eksekusi program.
- Memproses operasi matriks menggunakan CuPy atau Numpy.
- Validasi input pengguna untuk mencegah kesalahan.
- Memberikan peringatan jika jumlah loop melebihi batas yang direkomendasikan (1000 iterasi).
- Menyediakan opsi setelah eksekusi:
  - Exit program
  - Restart program
  - Clear screen dan kembali ke loop section

## Prasyarat
- Python 3.x
- CuPy (jika menggunakan NVIDIA GPU)
- NumPy (jika tidak menggunakan NVIDIA GPU)
- Time library (built-in Python)

## Instalasi
1. Pastikan Python sudah terinstal di sistem.
2. Instal dependensi dengan menjalankan perintah berikut sesuai dengan kebutuhan:
   ```bash
   pip install cupy # Jika menggunakan NVIDIA GPU
   pip install numpy # Jika tidak menggunakan NVIDIA GPU
   ```

## Cara Penggunaan
1. Jalankan skrip menggunakan perintah berikut:
   ```bash
   python nama_file.py
   ```
2. Ikuti instruksi yang ditampilkan di terminal.
3. Masukkan jumlah loop yang diinginkan.
4. Masukkan ukuran matriks acak.
5. Tunggu hingga program selesai mengeksekusi perhitungan matriks.
6. Pilih opsi setelah eksekusi:
   - `0` untuk keluar
   - `1` untuk menjalankan ulang program
   - `2` untuk membersihkan layar dan kembali ke menu utama

## Catatan Penting
- Jika jumlah loop yang dimasukkan melebihi 1000, program akan memberikan peringatan dan meminta konfirmasi pengguna sebelum melanjutkan.
- Semakin besar ukuran matriks dan jumlah loop, semakin besar konsumsi RAM dan GPU yang digunakan.

## Penulis
**Oscar Victorious Putra Tambunan** (51424063)

## Lisensi
Program ini dibuat untuk tujuan edukasi dan eksperimen. Penggunaan kembali dan modifikasi diperbolehkan dengan mencantumkan kredit kepada penulis.

