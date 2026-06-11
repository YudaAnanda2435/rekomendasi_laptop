# LaptopWise

LaptopWise adalah sistem rekomendasi laptop berbasis web untuk membantu pengguna memilih laptop sesuai kebutuhan, budget, dan spesifikasi utama.

Dokumen ini adalah panduan utama proyek untuk client. Isinya mencakup frontend, backend, alur instalasi, cara menjalankan aplikasi, endpoint API, deployment, dan troubleshooting.

## Gambaran Singkat

- Frontend: ReactJS + Vite + Tailwind CSS v4
- Backend: FastAPI
- Model: Naive Bayes
- Data utama: dataset hasil preprocessing dari backend
- Frontend hanya konsumsi API backend

## Fitur Utama

- Landing page informatif
- Form rekomendasi laptop
- Hasil rekomendasi utama dan alternatif
- Halaman data laptop dari backend
- Halaman informasi sistem dan model
- Status backend
- Loading, error, empty state, dan state alternatif

## Batasan Produk

Tidak ada fitur:

- login / register
- dashboard admin
- database
- scraping
- pembelian laptop
- payment gateway
- training model dari web

## Label Kebutuhan Laptop

Label kebutuhan yang dipakai konsisten oleh frontend dan backend:

- Administrasi/Perkantoran
- Programming
- Desain Grafis
- Editing Video

## Struktur Project

```text
App/
|-- backend/
|   |-- app/
|   |-- data/
|   |-- models/
|   |-- main.py
|   |-- requirements.txt
|   +-- .env.example
+-- frontend/
    |-- src/
    |-- index.html
    |-- package.json
    |-- vite.config.js
    |-- .env.example
    |-- vercel.json
    +-- README.md
```

## Teknologi

Frontend:

- ReactJS
- Vite
- Tailwind CSS v4
- `@tailwindcss/vite`
- React Router DOM
- Lucide React
- AOS

Backend:

- FastAPI
- Python Dotenv
- Pandas
- NumPy
- Scikit-learn
- Joblib

Model dan data:

- Naive Bayes
- Dataset final hasil preprocessing
- Metadata model
- File options frontend

## Prasyarat

Pastikan sudah terpasang:

- Node.js 18+ dan npm
- Python 3.10+
- Git
- Browser modern

Cek versi:

```bash
node -v
npm -v
python --version
```

## Artefak Backend yang Wajib Ada

Backend membutuhkan file berikut:

```text
backend/data/laptops_backend_ready.csv
backend/data/frontend_options.json
backend/models/naive_bayes_laptop_pipeline.joblib
backend/models/model_metadata.json
```

Jika salah satu file hilang, endpoint rekomendasi atau informasi model bisa gagal.

## Environment Backend

Masuk ke folder backend:

```bash
cd backend
```

Salin environment file:

```bash
Copy-Item .env.example .env
```

Contoh isi `.env` backend:

```env
APP_NAME=Sistem Rekomendasi Laptop API
APP_VERSION=1.0.0
API_PREFIX=/api
BACKEND_CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

Jika frontend berjalan di domain atau port lain, tambahkan origin tersebut ke `BACKEND_CORS_ORIGINS`.

## Instalasi Backend

```bash
cd backend
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

Jika memakai Command Prompt:

```bash
.venv\Scripts\activate.bat
```

## Menjalankan Backend

```bash
cd backend
.\.venv\Scripts\activate
fastapi dev main.py
```

Backend default berjalan di:

```text
http://127.0.0.1:8000
```

Dokumentasi API:

```text
http://127.0.0.1:8000/docs
```

Health check:

```text
http://127.0.0.1:8000/api/health
```

## Environment Frontend

Masuk ke folder frontend:

```bash
cd frontend
```

Salin environment file:

```bash
Copy-Item .env.example .env
```

Contoh isi `.env` frontend:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

Fallback default jika env tidak tersedia:

```text
http://127.0.0.1:8000
```

## Instalasi Frontend

```bash
cd frontend
npm install
```

Jika PowerShell membatasi script npm, gunakan:

```bash
npm.cmd install
```

## Menjalankan Frontend

```bash
cd frontend
npm run dev
```

Frontend default berjalan di:

```text
http://localhost:5173
```

## Urutan Menjalankan Aplikasi

Gunakan dua terminal.

Terminal 1:

```bash
cd backend
.\.venv\Scripts\activate
fastapi dev main.py
```

Terminal 2:

```bash
cd frontend
npm install
npm run dev
```

Lalu buka:

```text
http://localhost:5173
```

## Route Frontend

- `/` - Beranda
- `/recommendation` - Form dan hasil rekomendasi
- `/laptops` - Data laptop
- `/about` - Informasi sistem
- `*` - Not Found

## Endpoint Backend

Frontend memakai endpoint berikut:

| Endpoint | Method | Fungsi |
| --- | --- | --- |
| `/api/health` | GET | Cek status backend |
| `/api/options` | GET | Ambil pilihan form dan filter |
| `/api/laptops` | GET | Ambil data laptop |
| `/api/recommendations` | POST | Kirim payload rekomendasi |
| `/api/model-info` | GET | Ambil metadata model |

## Kontrak Response API

Frontend mengharapkan response seperti ini:

```json
{
  "success": true,
  "message": "Pesan response",
  "data": {}
}
```

Jika `success` bernilai `false`, frontend akan menampilkan pesan error dari backend.

## Contoh Payload Rekomendasi

```json
{
  "kebutuhan": "Programming",
  "budget_maksimal": 8000000,
  "ram_min": 8,
  "storage_min": 256,
  "brand": "Semua",
  "os_family": "Windows",
  "processor_min_level": "Mid",
  "gpu_type": "Tidak wajib",
  "touch_screen": "Semua",
  "jumlah_hasil": 5
}
```

Catatan:

- `budget_maksimal` mengikuti satuan harga dataset.
- `brand`, `os_family`, `processor_min_level`, dan `touch_screen` bisa bernilai `Semua`.
- `gpu_type` bisa bernilai `Tidak wajib`.
- `jumlah_hasil` minimum 1 dan maksimum 50.

## Perilaku Rekomendasi Alternatif

Jika tidak ada laptop yang memenuhi semua filter, backend dapat mengembalikan:

```json
{
  "is_alternative": true,
  "message": "Tidak ditemukan laptop yang memenuhi semua kriteria. Sistem menampilkan alternatif terbaik dengan beberapa filter yang dilonggarkan."
}
```

Setiap item alternatif dapat memiliki:

- `unmet_filters`
- `match_percentage`
- `is_exact_match`
- `alasan_rekomendasi`

Frontend akan menampilkan badge alternatif dan daftar filter yang belum terpenuhi agar hasil mudah dipahami.

## Halaman Frontend

### Beranda

- Hero section
- Message laptop visual
- Fitur sistem
- Cara kerja sistem
- Kategori kebutuhan laptop
- Preview sistem rekomendasi
- Kenapa LaptopWise
- CTA akhir

### Rekomendasi

Endpoint yang dipakai:

- `GET /api/options`
- `POST /api/recommendations`

Fitur:

- Form preferensi laptop
- Validasi input
- Loading state
- Error state
- Empty state
- Hasil rekomendasi utama
- Hasil alternatif

### Data Laptop

Endpoint yang dipakai:

- `GET /api/options`
- `GET /api/laptops`

Fitur:

- Search model atau brand
- Filter brand
- Filter kebutuhan
- Limit jumlah data
- Card katalog laptop

### Tentang Sistem

Endpoint yang dipakai:

- `GET /api/model-info`

Isi utama:

- Penjelasan sistem
- Teknologi yang digunakan
- Informasi model
- Metrik model jika tersedia
- Daftar label kebutuhan
- Catatan harga mengikuti dataset

### Not Found

- Pesan halaman tidak ditemukan
- Tombol kembali ke beranda

## Integrasi Frontend dan Backend

Alur data:

1. Frontend membaca `VITE_API_BASE_URL`.
2. Frontend memanggil backend melalui service layer di `src/services/`.
3. Backend membaca dataset, options, metadata, dan model.
4. Backend mengembalikan response dengan format `success`, `message`, dan `data`.
5. Frontend menampilkan loading, error, empty state, atau success state.

Frontend tidak:

- Menjalankan model machine learning
- Membaca file `.joblib`
- Membaca CSV dataset secara langsung
- Membuat data dummy sebagai sumber data utama

## Struktur Service Frontend

File utama:

- `apiClient.js` - request umum, base URL, error handling
- `healthService.js` - `getHealth()`
- `optionsService.js` - `getOptions()`
- `laptopService.js` - `getLaptops(params)`
- `recommendationService.js` - `getRecommendations(payload)`
- `modelInfoService.js` - `getModelInfo()`

## Build dan Deploy Frontend

Build:

```bash
cd frontend
npm run build
```

Preview build:

```bash
npm run preview
```

Untuk deploy ke Vercel:

- set root project ke `frontend/`
- pastikan `frontend/vercel.json` dipakai untuk rewrite SPA
- set `VITE_API_BASE_URL` ke URL backend produksi

Contoh frontend produksi:

```env
VITE_API_BASE_URL=https://api.domain-client.com
```

Contoh backend produksi:

```env
BACKEND_CORS_ORIGINS=https://domain-client.com
```

## Troubleshooting

### Backend belum jalan

Pastikan `fastapi dev main.py` aktif dan `http://127.0.0.1:8000/api/health` bisa dibuka.

### Frontend tidak bisa ambil data

Periksa:

- `frontend/.env`
- `VITE_API_BASE_URL`
- backend sedang aktif
- CORS backend mengizinkan origin frontend

### Refresh page jadi Not Found saat deploy

Pastikan SPA rewrite tersedia di `frontend/vercel.json`.

### CORS error

Tambahkan origin frontend ke `BACKEND_CORS_ORIGINS` di backend `.env`.

### Package belum terinstall

Frontend:

```bash
cd frontend
npm install
```

Backend:

```bash
cd backend
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### File artefak tidak ditemukan

Pastikan dataset, options, model pipeline, dan metadata tersedia di `backend/data/` dan `backend/models/`.

## Checklist Sebelum Serah ke Client

- Backend aktif
- Frontend aktif
- Environment frontend benar
- CORS backend sudah sesuai
- Dataset dan model tersedia
- Route React bisa dibuka dan di-refresh tanpa error
- Build frontend sukses

## Catatan Akhir

Frontend hanya konsumsi API. Semua data utama tetap berasal dari backend FastAPI. Dokumen ini adalah referensi utama untuk menjalankan dan memahami seluruh sistem.
