# LaptopWise - Sistem Rekomendasi Laptop

LaptopWise adalah aplikasi web untuk membantu pengguna memilih laptop berdasarkan kebutuhan utama, budget, dan preferensi spesifikasi. Sistem terdiri dari dua bagian:

- **Frontend**: ReactJS + Vite + Tailwind CSS v4.
- **Backend**: FastAPI yang membaca dataset final, options frontend, metadata model, dan model Naive Bayes.

Aplikasi ini tidak memiliki fitur login, register, dashboard admin, pembelian laptop, payment gateway, scraping, database, atau training ulang model dari web. Semua data utama berasal dari backend API.

## Ringkasan Fitur

- Landing page informatif untuk menjelaskan sistem.
- Form rekomendasi laptop berdasarkan kebutuhan pengguna.
- Hasil rekomendasi dengan alasan, score, confidence, dan status alternatif.
- Halaman data laptop dari dataset backend.
- Filter data laptop berdasarkan search, brand, kebutuhan, dan limit.
- Halaman informasi sistem dan metadata model.
- Status koneksi backend.
- Handling loading, error, empty state, dan fallback rekomendasi.

## Label Kebutuhan Laptop

Label berikut digunakan oleh frontend dan backend. Jangan diubah tanpa menyesuaikan dataset dan model:

- `Administrasi/Perkantoran`
- `Programming`
- `Desain Grafis`
- `Editing Video`

## Struktur Project

Struktur utama project:

```text
App/
|-- backend/
|   |-- main.py
|   |-- requirements.txt
|   |-- .env.example
|   |-- app/
|   |-- data/
|   +-- models/
+-- frontend/
    |-- index.html
    |-- package.json
    |-- vite.config.js
    |-- .env.example
    |-- README.md
    +-- src/
```

Struktur frontend:

```text
frontend/src/
|-- assets/
|-- components/
|   |-- elements/
|   |-- fragments/
|   +-- layouts/
|-- hooks/
|-- pages/
|-- services/
|-- styles/
|   +-- index.css
+-- utils/
```

Struktur backend:

```text
backend/
|-- main.py
|-- requirements.txt
|-- app/
|   |-- api/
|   |-- core/
|   |-- schemas/
|   |-- services/
|   +-- utils/
|-- data/
+-- models/
```

## Teknologi

Frontend:

- ReactJS
- Vite
- Tailwind CSS v4
- `@tailwindcss/vite`
- React Router DOM
- Lucide React
- AOS animation

Backend:

- Python
- FastAPI
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Python Dotenv

Model dan data:

- Naive Bayes
- Dataset final hasil preprocessing
- File options frontend
- Metadata model

## Prasyarat Instalasi

Pastikan perangkat sudah memiliki:

- Node.js dan npm
- Python 3.10 atau lebih baru
- Git, jika project diambil dari repository
- Browser modern seperti Chrome, Edge, atau Firefox

Cek versi:

```bash
node -v
npm -v
python --version
```

Di Windows PowerShell, jika command `npm` diblokir oleh policy, gunakan `npm.cmd`.

## Artefak Backend yang Wajib Ada

Backend membutuhkan file berikut:

```text
backend/data/laptops_backend_ready.csv
backend/data/frontend_options.json
backend/models/naive_bayes_laptop_pipeline.joblib
backend/models/model_metadata.json
```

File tersebut adalah sumber data utama runtime. Backend tidak membuat data dummy sebagai pengganti file di atas.

## Konfigurasi Environment Backend

Masuk ke folder backend:

```bash
cd backend
```

Salin `.env.example` menjadi `.env`.

Windows PowerShell:

```bash
Copy-Item .env.example .env
```

Command Prompt:

```bash
copy .env.example .env
```

Isi default:

```env
APP_NAME=Sistem Rekomendasi Laptop API
APP_VERSION=1.0.0
API_PREFIX=/api
BACKEND_CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

Jika frontend berjalan di port lain, tambahkan origin frontend ke `BACKEND_CORS_ORIGINS`.

## Instalasi Backend

Dari folder `backend/`:

```bash
python -m venv .venv
```

Aktifkan virtual environment.

Windows PowerShell:

```bash
.\.venv\Scripts\activate
```

Command Prompt:

```bash
.venv\Scripts\activate.bat
```

Install dependency:

```bash
pip install -r requirements.txt
```

## Menjalankan Backend

Dari folder `backend/` dan virtual environment aktif:

```bash
fastapi dev main.py
```

Backend default berjalan di:

```text
http://127.0.0.1:8000
```

Dokumentasi API FastAPI tersedia di:

```text
http://127.0.0.1:8000/docs
```

Cek health endpoint:

```text
http://127.0.0.1:8000/api/health
```

Backend siap digunakan jika response menunjukkan dataset, model, options, dan metadata tersedia.

## Konfigurasi Environment Frontend

Buka terminal baru, lalu masuk ke folder frontend:

```bash
cd frontend
```

Salin `.env.example` menjadi `.env`.

Windows PowerShell:

```bash
Copy-Item .env.example .env
```

Command Prompt:

```bash
copy .env.example .env
```

Isi default:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

Jika backend dijalankan di server lain, ganti value tersebut. Contoh:

```env
VITE_API_BASE_URL=https://api-domain-client.com
```

Setelah mengubah `.env`, restart development server frontend.

## Instalasi Frontend

Dari folder `frontend/`:

```bash
npm install
```

Jika PowerShell memblokir script npm:

```bash
npm.cmd install
```

## Menjalankan Frontend

Dari folder `frontend/`:

```bash
npm run dev
```

Atau di PowerShell:

```bash
npm.cmd run dev
```

Frontend default berjalan di:

```text
http://localhost:5173
```

Jika port 5173 sudah dipakai, Vite akan memilih port lain. Jika port berubah, pastikan backend CORS mengizinkan origin baru tersebut.

## Urutan Menjalankan Web Lengkap

Gunakan dua terminal.

Terminal 1 untuk backend:

```bash
cd backend
.\.venv\Scripts\activate
fastapi dev main.py
```

Terminal 2 untuk frontend:

```bash
cd frontend
npm run dev
```

Buka browser:

```text
http://localhost:5173
```

Lalu cek halaman:

- Beranda: `http://localhost:5173/`
- Rekomendasi: `http://localhost:5173/recommendation`
- Data Laptop: `http://localhost:5173/laptops`
- Tentang Sistem: `http://localhost:5173/about`

## Build Production Frontend

Dari folder `frontend/`:

```bash
npm run build
```

Output build berada di:

```text
frontend/dist/
```

Preview hasil build:

```bash
npm run preview
```

Default preview biasanya berjalan di:

```text
http://localhost:4173
```

## Script Frontend

Script tersedia di `frontend/package.json`:

```json
{
  "dev": "vite",
  "build": "vite build",
  "lint": "eslint .",
  "preview": "vite preview"
}
```

Penggunaan:

```bash
npm run dev
npm run build
npm run lint
npm run preview
```

## Endpoint Backend yang Dipakai Frontend

Frontend menggunakan endpoint berikut:

| Endpoint | Method | Fungsi |
| --- | --- | --- |
| `/api/health` | GET | Mengecek status backend dan kesiapan artefak |
| `/api/options` | GET | Mengambil pilihan form rekomendasi dan filter |
| `/api/laptops` | GET | Mengambil daftar laptop dari dataset |
| `/api/recommendations` | POST | Mengirim preferensi user dan mengambil rekomendasi |
| `/api/model-info` | GET | Mengambil informasi model dan metrik |

Base URL backend diambil dari:

```env
VITE_API_BASE_URL
```

Fallback frontend jika `.env` tidak tersedia:

```text
http://127.0.0.1:8000
```

## Format Response API

Frontend mengharapkan format response:

```json
{
  "success": true,
  "message": "Pesan response",
  "data": {}
}
```

Jika `success` bernilai `false`, frontend akan menampilkan pesan error dari backend.

## Contoh Payload Rekomendasi

Frontend mengirim payload ke `POST /api/recommendations` seperti berikut:

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

- `budget_maksimal` memakai nilai harga dalam Rupiah hasil preprocessing dataset.
- `brand`, `os_family`, `processor_min_level`, dan `touch_screen` dapat bernilai `Semua`.
- `gpu_type` dapat bernilai `Tidak wajib`.
- `jumlah_hasil` minimal 1 dan maksimal 50.

## Behavior Rekomendasi Alternatif

Jika tidak ada laptop yang memenuhi semua filter, backend dapat mengembalikan:

```json
{
  "is_alternative": true,
  "message": "Tidak ditemukan laptop yang memenuhi semua kriteria. Sistem menampilkan alternatif terbaik dengan beberapa filter yang dilonggarkan."
}
```

Setiap item alternatif dapat memiliki:

- `unmet_filters`: daftar filter yang belum terpenuhi.
- `match_percentage`: persentase kecocokan.
- `is_exact_match`: status apakah item memenuhi semua filter.
- `alasan_rekomendasi`: alasan dari backend.

Frontend akan menampilkan badge `Alternatif` dan daftar filter yang belum terpenuhi agar user tidak salah memahami hasil.

## Halaman Frontend

### Beranda

Route:

```text
/
```

Isi utama:

- Hero section.
- Message laptop visual.
- Fitur sistem.
- Cara kerja sistem.
- Kategori kebutuhan laptop.
- Preview sistem rekomendasi.
- Kenapa LaptopWise.
- CTA akhir.

### Rekomendasi

Route:

```text
/recommendation
```

Endpoint yang dipakai:

- `GET /api/options`
- `POST /api/recommendations`

Fitur:

- Form preferensi laptop.
- Validasi input.
- Loading state.
- Error state.
- Empty state.
- Hasil rekomendasi utama.
- Hasil alternatif jika filter terlalu ketat.

### Data Laptop

Route:

```text
/laptops
```

Endpoint yang dipakai:

- `GET /api/options`
- `GET /api/laptops`

Fitur:

- Search model atau brand.
- Filter brand.
- Filter kebutuhan.
- Limit jumlah data.
- Card katalog laptop.

### Tentang Sistem

Route:

```text
/about
```

Endpoint yang dipakai:

- `GET /api/model-info`

Isi utama:

- Penjelasan sistem.
- Teknologi yang digunakan.
- Informasi model.
- Metrik model jika tersedia.
- Daftar label kebutuhan.
- Catatan harga mengikuti dataset.

### Not Found

Route:

```text
*
```

Menampilkan pesan halaman tidak ditemukan dan tombol kembali ke beranda.

## Integrasi Frontend dan Backend

Alur data:

1. Frontend membaca `VITE_API_BASE_URL`.
2. Frontend memanggil backend melalui service layer di `src/services/`.
3. Backend membaca dataset, options, metadata, dan model.
4. Backend mengembalikan response dengan format `success`, `message`, dan `data`.
5. Frontend menampilkan data, loading, error, atau empty state sesuai response.

Frontend tidak:

- Menjalankan model machine learning.
- Membaca file `.joblib`.
- Membaca CSV dataset secara langsung.
- Membuat data dummy sebagai sumber data utama.

## Struktur Service Frontend

Service API berada di:

```text
frontend/src/services/
```

File utama:

- `apiClient.js`: client request umum, base URL, error handling.
- `healthService.js`: `getHealth()`.
- `optionsService.js`: `getOptions()`.
- `laptopService.js`: `getLaptops(params)`.
- `recommendationService.js`: `getRecommendations(payload)`.
- `modelInfoService.js`: `getModelInfo()`.

## Tailwind CSS v4

Project menggunakan Tailwind CSS v4 dengan konfigurasi Vite:

```js
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [react(), tailwindcss()],
})
```

CSS utama:

```text
frontend/src/styles/index.css
```

File tersebut memakai:

```css
@import "tailwindcss";
```

Project tidak membutuhkan `tailwind.config.js` untuk setup dasar Tailwind v4.

## Catatan Deployment

Untuk deployment frontend:

1. Pastikan backend sudah online dan dapat diakses publik atau oleh server frontend.
2. Set `VITE_API_BASE_URL` ke URL backend produksi.
3. Jalankan build frontend:

   ```bash
   npm run build
   ```

4. Upload isi folder `frontend/dist/` ke layanan hosting frontend.
5. Pastikan backend CORS mengizinkan domain frontend produksi.

Contoh `.env` frontend produksi:

```env
VITE_API_BASE_URL=https://api.laptopwise-client.com
```

Contoh `.env` backend produksi:

```env
BACKEND_CORS_ORIGINS=https://laptopwise-client.com
```

## Checklist Sebelum Demo ke Client

- Backend aktif di `http://127.0.0.1:8000`.
- Endpoint `/api/health` status ready.
- File dataset tersedia.
- File options tersedia.
- File model tersedia.
- File metadata tersedia.
- Frontend aktif di `http://localhost:5173`.
- `.env` frontend mengarah ke backend yang benar.
- Halaman Rekomendasi berhasil menampilkan hasil.
- Halaman Data Laptop berhasil menampilkan data.
- Halaman Tentang Sistem berhasil menampilkan informasi model.
- Tidak ada error CORS di browser console.

## Troubleshooting

### Backend belum jalan

Gejala:

- Frontend menampilkan pesan backend belum terhubung.
- Request API gagal.

Solusi:

```bash
cd backend
.\.venv\Scripts\activate
fastapi dev main.py
```

Lalu buka:

```text
http://127.0.0.1:8000/api/health
```

### Frontend belum jalan

Gejala:

- `http://localhost:5173` tidak dapat dibuka.

Solusi:

```bash
cd frontend
npm install
npm run dev
```

### CORS error

Gejala:

- Browser console menampilkan error CORS.
- API sebenarnya aktif, tetapi frontend tidak bisa membaca response.

Solusi:

1. Cek URL frontend, misalnya `http://localhost:5173`.
2. Pastikan URL tersebut ada di backend `.env`:

   ```env
   BACKEND_CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
   ```

3. Restart backend.

### `VITE_API_BASE_URL` salah

Gejala:

- Frontend mencoba request ke URL backend yang salah.
- Network tab menampilkan request ke host yang tidak aktif.

Solusi:

1. Buka `frontend/.env`.
2. Pastikan isinya:

   ```env
   VITE_API_BASE_URL=http://127.0.0.1:8000
   ```

3. Restart frontend:

   ```bash
   npm run dev
   ```

### Package frontend belum terinstall

Gejala:

- `vite` tidak dikenali.
- Import React atau package lain gagal.

Solusi:

```bash
cd frontend
npm install
```

### Package backend belum terinstall

Gejala:

- `ModuleNotFoundError`.
- `fastapi` command tidak dikenali.

Solusi:

```bash
cd backend
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### Virtual environment belum aktif

Gejala:

- Dependency Python sudah diinstall tetapi tetap tidak terbaca.

Solusi:

```bash
cd backend
.\.venv\Scripts\activate
```

Pastikan prompt terminal menampilkan `(.venv)`.

### Dataset atau model tidak ditemukan

Gejala:

- `/api/health` menunjukkan `dataset_available`, `model_available`, `options_available`, atau `metadata_available` bernilai `false`.
- Endpoint rekomendasi gagal.

Solusi:

Pastikan file berikut ada:

```text
backend/data/laptops_backend_ready.csv
backend/data/frontend_options.json
backend/models/naive_bayes_laptop_pipeline.joblib
backend/models/model_metadata.json
```

### Port sudah digunakan

Gejala:

- Backend atau frontend gagal start karena port sudah dipakai.

Solusi:

- Tutup proses yang memakai port tersebut.
- Atau jalankan frontend di port lain dan tambahkan origin baru ke CORS backend.

### PowerShell memblokir npm

Gejala:

- Muncul pesan `running scripts is disabled on this system`.

Solusi cepat:

```bash
npm.cmd install
npm.cmd run dev
```

## Maintenance Notes

- Jangan mengubah label kebutuhan tanpa menyesuaikan dataset dan model.
- Jangan mengganti sumber data utama dengan dummy data.
- Jika backend URL berubah, update `frontend/.env`.
- Jika frontend domain berubah, update `BACKEND_CORS_ORIGINS` di backend.
- Jika model atau dataset diganti, cek ulang `/api/health`, `/api/model-info`, dan hasil rekomendasi.
- Jalankan `npm run build` sebelum menyerahkan frontend production.

## Ringkasan Cepat untuk Client

Urutan menjalankan aplikasi lokal:

```bash
cd backend
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
fastapi dev main.py
```

Buka terminal kedua:

```bash
cd frontend
npm install
npm run dev
```

Buka:

```text
http://localhost:5173
```
