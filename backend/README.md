# Sistem Rekomendasi Laptop API

Backend FastAPI untuk sistem rekomendasi pemilihan laptop berbasis model Naive
Bayes. Backend membaca dataset final dan model hasil training dari artefak lokal
tanpa database atau proses training ulang.

## Struktur Project

```text
backend/
├── main.py
├── requirements.txt
├── .env.example
├── app/
│   ├── api/
│   ├── core/
│   ├── schemas/
│   ├── services/
│   └── utils/
├── data/
└── models/
```

`main.py` hanya berisi setup aplikasi, CORS, router, handler error, dan root
endpoint. Logic pembacaan data, model, options, metadata, dan rekomendasi berada
di folder `app/services/`.

## Instalasi

Jalankan perintah berikut dari folder `backend/`:

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

Salin `.env.example` menjadi `.env` bila ingin menyesuaikan konfigurasi lokal.

## Artefak Dataset dan Model

Tempatkan artefak hasil preprocessing dan training Colab pada path berikut:

```text
backend/data/laptops_backend_ready.csv
backend/data/frontend_options.json
backend/models/naive_bayes_laptop_pipeline.joblib
backend/models/model_metadata.json
```

File tersebut adalah sumber data utama runtime. Backend tidak memakai dummy data,
database, scraping, atau training ulang model.

## Menjalankan Backend

Dari folder `backend/`, jalankan:

```bash
fastapi dev main.py
```

Dokumentasi interaktif tersedia di `http://127.0.0.1:8000/docs`.

## Format Response

Response sukses:

```json
{
  "success": true,
  "message": "Pesan response",
  "data": {}
}
```

Response error:

```json
{
  "success": false,
  "message": "Pesan error",
  "data": null
}
```

## Endpoint dan Contoh

### GET `/api/health`

Request:

```bash
curl http://127.0.0.1:8000/api/health
```

Response:

```json
{
  "success": true,
  "message": "API berjalan.",
  "data": {
    "app_name": "Sistem Rekomendasi Laptop API",
    "app_version": "1.0.0",
    "dataset_available": true,
    "model_available": true,
    "options_available": true,
    "metadata_available": true,
    "status": "ready"
  }
}
```

### GET `/api/options`

Request:

```bash
curl http://127.0.0.1:8000/api/options
```

Response:

```json
{
  "success": true,
  "message": "Pilihan frontend berhasil dimuat.",
  "data": {
    "kebutuhan": [
      "Administrasi/Perkantoran",
      "Programming",
      "Desain Grafis",
      "Editing Video"
    ],
    "brand": ["Semua", "Acer", "Asus"],
    "ram_min": [4, 8, 16],
    "jumlah_hasil": [5, 10, 15, 20],
    "price_note": "Satuan harga mengikuti dataset asli."
  }
}
```

### GET `/api/laptops`

Request:

```bash
curl "http://127.0.0.1:8000/api/laptops?limit=5&brand=Asus&kebutuhan=Programming&search=vivobook"
```

Response:

```json
{
  "success": true,
  "message": "Daftar laptop berhasil dimuat.",
  "data": {
    "items": [
      {
        "model": "Vivobook 14",
        "brand_name": "Asus",
        "price": 8999000,
        "rating": 4.4,
        "processor_series": "Core i5",
        "processor_level": "Mid",
        "ram_num": 8,
        "memory_size": 512,
        "memory_type": "SSD",
        "gpu_type": "Integrated",
        "gpu_level": "Integrated Basic",
        "os_family": "Windows",
        "label_kebutuhan": "Programming",
        "predicted_label": "Programming",
        "prediction_confidence": 0.91,
        "alasan_label": "Sesuai untuk kebutuhan programming."
      }
    ],
    "total": 1,
    "limit": 5,
    "offset": 0
  }
}
```

### POST `/api/recommendations`

Request:

```bash
curl -X POST http://127.0.0.1:8000/api/recommendations ^
  -H "Content-Type: application/json" ^
  -d "{\"kebutuhan\":\"Programming\",\"budget_maksimal\":15000000,\"ram_min\":8,\"storage_min\":512,\"brand\":\"Semua\",\"os_family\":\"Windows\",\"processor_min_level\":\"Mid\",\"gpu_type\":\"Tidak wajib\",\"touch_screen\":\"Semua\",\"jumlah_hasil\":5}"
```

Response:

```json
{
  "success": true,
  "message": "Rekomendasi laptop berhasil dibuat.",
  "data": {
    "message": "Rekomendasi laptop berhasil dibuat.",
    "total": 5,
    "is_alternative": false,
    "recommendations": [
      {
        "model": "Vivobook 14",
        "brand_name": "Asus",
        "price": 8999000,
        "rating": 4.4,
        "processor_series": "Core i5",
        "processor_level": "Mid",
        "ram_num": 8,
        "memory_size": 512,
        "memory_type": "SSD",
        "gpu_type": "Integrated",
        "gpu_level": "Integrated Basic",
        "os_family": "Windows",
        "backend_predicted_label": "Programming",
        "backend_confidence": 0.91,
        "final_score": 0.86,
        "alasan_rekomendasi": "Direkomendasikan untuk Programming karena memiliki processor Core i5, RAM 8 GB, storage 512 GB SSD, GPU Integrated, dan harga masih sesuai filter."
      }
    ]
  }
}
```

### GET `/api/model-info`

Request:

```bash
curl http://127.0.0.1:8000/api/model-info
```

Response:

```json
{
  "success": true,
  "message": "Informasi model berhasil dimuat.",
  "data": {
    "nama_proyek": "Sistem Rekomendasi Pemilihan Laptop Berdasarkan Kebutuhan Pengguna",
    "algoritma": "Naive Bayes",
    "jenis_model": "Multinomial Naive Bayes dengan One Hot Encoding",
    "tanggal_training": "2026-06-06 07:39:46",
    "target": "label_kebutuhan",
    "fitur_model": ["brand_name", "processor_series", "processor_level"],
    "kelas": [
      "Administrasi/Perkantoran",
      "Desain Grafis",
      "Editing Video",
      "Programming"
    ],
    "metrics": {
      "accuracy": 0.9947
    },
    "catatan": [
      "Dataset final dapat digunakan pada backend FastAPI."
    ]
  }
}
```

## Ringkasan Endpoint

- `GET /`: informasi API.
- `GET /api/health`: status API dan kesiapan artefak.
- `GET /api/options`: pilihan input frontend dari file JSON.
- `GET /api/laptops`: daftar laptop ringkas dari dataset final.
- `POST /api/recommendations`: prediksi Naive Bayes dan rekomendasi laptop.
- `GET /api/model-info`: metadata model yang aman ditampilkan.

## Troubleshooting

### Dataset not found

Gejala: endpoint `/api/laptops`, `/api/options`, atau `/api/recommendations`
mengembalikan pesan dataset belum tersedia.

Solusi: pastikan file Colab `laptops_backend_ready.csv` sudah berada di:

```text
backend/data/laptops_backend_ready.csv
```

### Model not found

Gejala: endpoint `/api/recommendations` gagal karena model belum tersedia.

Solusi: pastikan file Colab `naive_bayes_laptop_pipeline.joblib` sudah berada di:

```text
backend/models/naive_bayes_laptop_pipeline.joblib
```

### CORS error

Gejala: frontend ReactJS tidak bisa memanggil API karena CORS.

Solusi: pastikan `.env` memuat origin frontend yang benar, misalnya:

```text
BACKEND_CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

Lalu restart backend.

### Package belum terinstall

Gejala: muncul error seperti `ModuleNotFoundError: No module named 'fastapi'`
atau command `fastapi` tidak dikenali.

Solusi:

```bash
pip install -r requirements.txt
fastapi dev main.py
```

Jika memakai virtual environment, aktifkan `.venv` terlebih dahulu.
