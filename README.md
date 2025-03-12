# Dashboard Analisis Bike Sharing 🚴‍♂️

Aplikasi ini bertujuan untuk menganalisis tren penyewaan sepeda berdasarkan data historis. Pengguna dapat melihat statistik dan visualisasi data, serta menganalisis penyewaan sepeda berdasarkan faktor seperti cuaca dan jam.

## Langkah-langkah Instalasi

1. **Clone atau Unduh Proyek**
   - Jika Anda belum memiliki proyek ini, clone repositori atau unduh file proyek yang berisi aplikasi ini ke dalam folder lokal Anda.

2. **Instalasi Dependensi**
   Pastikan Anda berada di dalam direktori proyek dan jalankan perintah berikut untuk menginstal dependensi yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

3. **File CSV yang Diperlukan**
    Pastikan Anda memiliki file CSV berikut yang digunakan oleh aplikasi:
    - main_data.csv - Data penyewaan sepeda yang telah dibersihkan.

    Pastikan file ini berada di direktori yang sama dengan `dashboard.py`.

## Menjalankan Aplikasi
Setelah Anda selesai menginstal semua dependensi, Anda dapat menjalankan aplikasi dengan perintah berikut:

1. **Arahkan ke Direktori Proyek**
    Masuk ke dalam direktori tempat `dashboard.py` berada dengan perintah berikut:
    ```bash
    cd dashboard
    ```

2. **Jalankan Aplikasi**
    Jalankan aplikasi menggunakan perintah berikut:
    ```bash
    streamlit run dashboard.py
    ```

3. **Akses Aplikasi di Browser**
    Setelah aplikasi berhasil dijalankan, Streamlit akan memberi URL lokal di terminal Anda yang biasanya berupa:
    ```bash
    Local URL:  http://localhost:8501
    Network URL:  http://<ip-address>:8501
    ```
    Buka URL tersebut di browser untuk mengakses dashboard analisis Bike Sharing.

## Cara Menggunakan Aplikasi
1. **Navigasi**
   Gunakan sidebar untuk memilih analisis yang ingin Anda lihat:
   - **Overview**: Menampilkan data yang diunggah beserta statistik deskriptif.
   - **Jam Penyewaan**: Visualisasi distribusi penyewaan sepeda berdasarkan jam.
   - **Pengaruh Cuaca**: Analisis pengaruh kondisi cuaca terhadap penyewaan sepeda.
   - **Clustering**: Analisis clustering penyewaan sepeda berdasarkan fitur tertentu.
   - **Forecasting**: Prediksi jumlah penyewaan sepeda di masa depan menggunakan time series forecasting.

2. **Filter Data**
   Gunakan filter interaktif di sidebar untuk memfilter data berdasarkan musim dan hari kerja.

3. **Melihat Hasil Analisis**
   Aplikasi akan menampilkan visualisasi dan analisis berdasarkan data yang telah difilter.

## Contoh Visualisasi
Berikut adalah beberapa contoh visualisasi yang dapat Anda lihat di dashboard:
- **Distribusi Penyewaan Sepeda per Jam**: Visualisasi distribusi penyewaan sepeda berdasarkan jam.
- **Pengaruh Cuaca**: Pengaruh kondisi cuaca terhadap penyewaan sepeda.
- **Clustering**: Hasil clustering penyewaan sepeda berdasarkan suhu dan jumlah penyewaan.
- **Forecasting**: Prediksi jumlah penyewaan sepeda di masa depan.

Selamat menganalisis! 🚴‍♂️