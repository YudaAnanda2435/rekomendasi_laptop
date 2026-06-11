# Backend Agent Instructions

## Scope Kerja

- Kerjakan seluruh perubahan hanya di dalam folder `backend/`.
- Jangan membuat, mengubah, memindahkan, atau menghapus file di `frontend/` maupun di luar `backend/`.
- Backend dibuat dengan FastAPI dan wajib dapat dijalankan dari folder `backend/` menggunakan:

  ```bash
  fastapi dev main.py
  ```

- Versi awal backend tidak menggunakan database.
- Backend melayani API yang akan dikonsumsi oleh frontend ReactJS.

## Tujuan Sistem

Backend menyediakan rekomendasi pemilihan laptop berdasarkan kebutuhan pengguna dengan algoritma utama Naive Bayes. Backend hanya melakukan inferensi menggunakan model yang sudah dilatih dan membaca dataset final hasil preprocessing Colab.

Jangan melakukan training ulang, preprocessing dataset mentah, atau scraping dari backend.

## Artefak Sumber Data

Artefak berikut akan ditempatkan di backend dan harus digunakan sebagai sumber data utama:

- `data/laptops_backend_ready.csv`: dataset final laptop yang siap digunakan backend.
- `data/frontend_options.json`: pilihan/filter yang disediakan kepada frontend.
- `models/naive_bayes_laptop_pipeline.joblib`: pipeline model Naive Bayes untuk inferensi.
- `models/model_metadata.json`: metadata model.

Ketentuan penggunaan artefak:

- Jangan mengganti artefak dengan dummy data sebagai sumber data utama.
- Jangan mengubah isi artefak kecuali pengguna secara eksplisit meminta perubahan tersebut.
- Gunakan path yang dihitung relatif terhadap lokasi backend, bukan bergantung pada current working directory yang tidak pasti.
- Muat dan validasi file secara aman. Berikan error yang jelas dan konsisten jika file belum tersedia, tidak dapat dibaca, atau formatnya tidak sesuai.
- Jangan memuat ulang dataset atau model pada setiap request jika dapat dimuat sekali dan digunakan kembali dengan aman.

## Label Kebutuhan

Gunakan label berikut secara persis. Jangan menerjemahkan, mengganti nama, mengubah kapitalisasi, atau menambahkan label baru:

- `Administrasi/Perkantoran`
- `Programming`
- `Desain Grafis`
- `Editing Video`

## Endpoint Wajib

Implementasikan endpoint berikut saat diminta:

- `GET /api/health`: status layanan serta kesiapan artefak penting.
- `GET /api/options`: pilihan input/filter untuk frontend dari `frontend_options.json`.
- `GET /api/laptops`: daftar laptop dari dataset final, dengan validasi query parameter yang diperlukan.
- `POST /api/recommendations`: validasi input pengguna, jalankan inferensi model Naive Bayes, lalu kembalikan rekomendasi laptop yang relevan.
- `GET /api/model-info`: informasi model yang aman ditampilkan dari `model_metadata.json`.

Jangan menambahkan endpoint login, register, dashboard admin, scraping, training ulang model, atau endpoint lain yang tidak diperlukan tanpa permintaan eksplisit.

## Struktur dan Arsitektur

- Gunakan struktur yang clean dan modular.
- Pertahankan `main.py` sebagai entry point yang ringkas untuk membuat aplikasi, memasang middleware yang diperlukan, mendaftarkan router, dan lifecycle aplikasi.
- Jangan menumpuk route handler, business logic, pembacaan file, dan transformasi data di `main.py`.
- Pisahkan tanggung jawab ke modul yang sesuai:
  - `routes/` untuk definisi endpoint dan pemetaan HTTP.
  - `schemas/` untuk model request, response, dan validasi Pydantic.
  - `services/` untuk business logic, pembacaan dataset, inferensi model, serta penyusunan rekomendasi.
  - `core/` untuk konfigurasi, konstanta, lifecycle, dan dependency bersama.
  - `utils/` hanya untuk helper generik yang benar-benar digunakan.
- Hindari abstraksi berlebihan. Ikuti pola yang sudah ada di backend jika project telah berkembang.
- Gunakan type hints pada fungsi publik dan bagian penting business logic.

## Kontrak API dan Validasi

- Gunakan Pydantic untuk memvalidasi seluruh request body dan response.
- Definisikan `response_model` untuk endpoint jika memungkinkan.
- Gunakan format response JSON yang konsisten untuk respons sukses maupun gagal.
- Jangan mengembalikan nilai `NaN`, tipe NumPy/Pandas yang tidak JSON-serializable, atau data internal yang tidak diperlukan frontend.
- Validasi nilai enum/filter, rentang numerik, pagination, dan input model sebelum menjalankan business logic.
- Gunakan status code HTTP yang tepat.
- Berikan pesan error yang jelas tanpa membocorkan stack trace, path lokal sensitif, atau detail internal model.
- Pertahankan kompatibilitas kontrak API dengan frontend. Jangan mengubah nama field response yang sudah digunakan tanpa permintaan eksplisit.

Format dasar yang disarankan:

```json
{
  "success": true,
  "message": "Request berhasil diproses",
  "data": {}
}
```

Untuk error:

```json
{
  "success": false,
  "message": "Penjelasan error yang jelas",
  "detail": null
}
```

## Aturan Rekomendasi dan Model

- Algoritma utama harus tetap Naive Bayes melalui pipeline joblib yang disediakan.
- Jangan mengganti algoritma, melatih model, atau melakukan fitting dari backend.
- Pastikan fitur yang dikirim ke model sesuai dengan skema dan urutan fitur pipeline/metadata.
- Gunakan hasil prediksi model sebagai dasar rekomendasi, lalu pilih/ranking laptop dari dataset final secara deterministik dan dapat dijelaskan.
- Jangan mengarang probabilitas, skor, spesifikasi, atau laptop yang tidak tersedia dalam artefak.
- Tangani ketidakcocokan versi model, fitur yang hilang, dan kegagalan inferensi dengan error yang jelas.

## Konfigurasi dan Keamanan

- Simpan konfigurasi terpusat di `core/`; jangan menyebarkan path atau konstanta yang sama ke banyak modul.
- Konfigurasi CORS harus terbatas pada kebutuhan frontend dan dapat diatur melalui konfigurasi/environment variable.
- Jangan menambahkan autentikasi karena login dan register berada di luar scope.
- Jangan mengeksekusi isi file data sebagai kode.
- Jangan memasukkan secret, credential, atau path mesin lokal ke source code.

## Testing dan Verifikasi

- Tambahkan atau perbarui test yang relevan ketika mengimplementasikan perilaku backend.
- Test minimal harus mencakup validasi schema, respons endpoint utama, service recommendation, dan kondisi artefak hilang/rusak.
- Gunakan fixture atau mocking untuk test; data fixture kecil boleh digunakan untuk pengujian, tetapi tidak boleh menjadi sumber data runtime utama.
- Setelah perubahan, verifikasi bahwa aplikasi dapat diimpor dan dijalankan dengan command wajib:

  ```bash
  fastapi dev main.py
  ```

- Jangan menyatakan perubahan selesai jika endpoint atau test terkait belum diverifikasi. Jika verifikasi terhalang karena artefak belum tersedia, jelaskan keterbatasannya dengan spesifik.

## Batasan Tegas

Jangan membuat:

- Login atau autentikasi pengguna.
- Register pengguna.
- Dashboard admin.
- Database atau integrasi ORM.
- Scraping.
- Training atau training ulang model dari backend.
- Dummy data sebagai data utama.
- Perubahan nama label kebutuhan.
- Perubahan apa pun di luar folder `backend/`.

## Checklist Sebelum Selesai

- Semua file yang berubah berada di dalam `backend/`.
- `main.py` tetap ringkas dan modular.
- Routes, schemas, services, core config, dan utils dipisahkan sesuai tanggung jawab.
- API memakai validasi Pydantic dan response JSON konsisten.
- Dataset CSV dan model joblib digunakan sebagai sumber runtime utama.
- Kondisi artefak hilang atau rusak ditangani dengan jelas.
- Tidak ada database, scraping, autentikasi, dashboard admin, atau training model.
- Empat label kebutuhan tetap persis seperti yang ditentukan.
- Perubahan telah diuji atau keterbatasan verifikasi telah dijelaskan.
