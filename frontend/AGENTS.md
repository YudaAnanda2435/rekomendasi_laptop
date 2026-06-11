# AGENTS.md

## Scope Kerja

- Seluruh pekerjaan agent wajib terbatas pada folder `frontend/`.
- Jangan membuat, mengubah, memindahkan, atau menghapus file di folder `backend/`.
- Jangan membuat, mengubah, memindahkan, atau menghapus file di luar folder `frontend/`.
- Baca struktur dan pola yang sudah ada sebelum melakukan perubahan, lalu pertahankan konsistensinya.
- Jangan menambahkan fitur di luar kebutuhan frontend sistem rekomendasi laptop.

## Konteks Aplikasi

- Frontend adalah aplikasi ReactJS yang dibangun dengan Vite.
- Styling menggunakan Tailwind CSS v4.
- Backend menggunakan FastAPI dan menjadi sumber utama seluruh data aplikasi.
- Frontend hanya mengumpulkan kebutuhan pengguna, mengambil data API, mengirim permintaan rekomendasi, dan menampilkan hasil.
- Frontend tidak menjalankan machine learning, tidak membaca file model, dan tidak membaca dataset CSV secara langsung.

## Batasan Fitur

Jangan membuat:

- login atau register;
- dashboard admin;
- database;
- scraping;
- fitur pembelian laptop;
- payment gateway;
- data dummy sebagai sumber data utama.

Jangan mengubah label kategori kebutuhan berikut:

- `Administrasi/Perkantoran`
- `Programming`
- `Desain Grafis`
- `Editing Video`

## Integrasi Backend API

- Ambil base URL dari environment variable `VITE_API_BASE_URL`.
- Gunakan fallback `http://127.0.0.1:8000` jika environment variable tidak tersedia.
- Semua request API wajib melalui service layer di `src/services/`.
- Hindari pemanggilan `fetch` langsung dan berulang di page atau komponen.
- Data utama aplikasi wajib berasal dari backend API, bukan data dummy.

Endpoint yang tersedia:

- `GET /api/health`
- `GET /api/options`
- `GET /api/laptops`
- `POST /api/recommendations`
- `GET /api/model-info`

Format response backend:

```json
{
  "success": true,
  "message": "...",
  "data": {}
}
```

- Gunakan nilai `success`, `message`, dan `data` sesuai respons backend.
- Selalu tangani kondisi loading, error, dan data kosong.
- Jika backend tidak aktif atau request gagal, tampilkan pesan error yang jelas dan mudah dipahami.
- Jika hasil rekomendasi kosong atau backend memberikan alternatif, tampilkan pesan dari backend.
- Jangan menyembunyikan error API dengan data dummy.

## Struktur Project

Gunakan struktur yang bersih, modular, dan sesuai tanggung jawab:

```text
src/
  components/
    elements/
    fragments/
    layouts/
  hooks/
  pages/
  services/
  styles/
    index.css
  utils/
```

- `src/components/elements/`: komponen kecil dan reusable, seperti `Button`, `Input`, `Select`, `Badge`, `Card`, `Loading`, `EmptyState`, dan `ErrorState`.
- `src/components/fragments/`: komponen gabungan, seperti `Navbar`, `HeroSection`, `RecommendationForm`, `RecommendationResult`, `LaptopCard`, dan `FilterSection`.
- `src/components/layouts/`: layout halaman atau wrapper struktur utama.
- `src/pages/`: komponen halaman.
- `src/services/`: konfigurasi dan fungsi request API.
- `src/utils/`: helper murni dan fungsi utilitas.
- `src/hooks/`: custom React hooks.
- `src/styles/index.css`: CSS utama aplikasi.

Pisahkan logic yang dapat digunakan ulang dari komponen. Page bertugas menyusun alur halaman, bukan menampung seluruh logic API dan tampilan dalam satu file besar.

## Aturan React

- Gunakan functional components dan React hooks.
- Buat komponen kecil dengan tanggung jawab yang jelas.
- Hindari duplikasi state, logic, dan markup.
- Letakkan logic request yang reusable di service atau custom hook.
- Gunakan nama komponen, props, state, dan fungsi yang jelas.
- Pastikan list memiliki key yang stabil.
- Jaga JSX tetap ringkas, bersih, dan mudah dibaca.

## Tailwind CSS v4 dan Styling

- Gunakan Tailwind CSS v4 melalui plugin `@tailwindcss/vite`.
- Gunakan `@import "tailwindcss";` di `src/styles/index.css`.
- Jangan menggunakan pola konfigurasi Tailwind v3 yang bergantung pada `tailwind.config.js` jika tidak diperlukan.
- Hindari `className` yang panjang, berulang, dan sulit dibaca di JSX.
- Jika sekumpulan style sering digunakan, buat class komponen yang reusable di CSS utama.
- Gunakan CSS modern dengan `@layer base`, `@layer components`, dan `@layer utilities`.
- Gunakan nama class yang jelas, misalnya `btn`, `btn-primary`, `card`, `input-field`, `select-field`, `section`, `page-shell`, dan `result-grid`.
- Jangan menggunakan inline style kecuali benar-benar diperlukan.
- Pertahankan tampilan responsif dan aksesibel.

Contoh pola CSS yang dianjurkan:

```css
@import "tailwindcss";

@layer base {
  /* Global element defaults */
}

@layer components {
  .btn {
    /* Reusable button styles */
  }

  .btn-primary {
    /* Primary button variant */
  }
}

@layer utilities {
  /* Project-specific utilities only when needed */
}
```

## Kualitas UX dan Aksesibilitas

- Berikan label yang jelas untuk setiap input.
- Gunakan elemen HTML semantik.
- Pastikan tombol dan kontrol form dapat digunakan dengan keyboard.
- Tampilkan status loading selama request berlangsung dan cegah submit berulang bila diperlukan.
- Tampilkan `EmptyState` saat data tidak tersedia dan `ErrorState` saat request gagal.
- Pertahankan pesan backend yang relevan agar pengguna memahami hasil rekomendasi.

## Verifikasi Sebelum Selesai

- Pastikan seluruh perubahan hanya berada di folder `frontend/`.
- Pastikan tidak ada perubahan pada `backend/` atau file di luar `frontend/`.
- Jalankan lint atau build frontend yang tersedia setelah perubahan jika memungkinkan.
- Pastikan integrasi tetap menggunakan backend API dan tidak menggantinya dengan data dummy.
- Pastikan label kategori kebutuhan tidak berubah.
- Laporkan file yang diubah dan hasil verifikasi secara ringkas.
