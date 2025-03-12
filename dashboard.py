import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Mengatur konfigurasi Streamlit
st.set_page_config(page_title="Dashboard Analisis Bike Sharing", layout="wide")

# Judul Dashboard
st.title("Dashboard Analisis Bike Sharing")

# Memuat data
@st.cache_data
def load_data():
    main_data = pd.read_csv('cleaned_data.csv')
    return main_data

main_data = load_data()

# Sidebar untuk navigasi
st.sidebar.title("Navigasi")
option = st.sidebar.selectbox("Pilih Analisis", ["Overview", "Jam Penyewaan", "Pengaruh Cuaca", "Clustering", "Forecasting"])

# Filter interaktif
st.sidebar.title("Filter Data")
season = st.sidebar.selectbox("Pilih Musim", ["Semua", "Musim Semi", "Musim Panas", "Musim Gugur", "Musim Dingin"])
workingday = st.sidebar.checkbox("Hari Kerja", value=True)

# Filter data berdasarkan input pengguna
if season != "Semua":
    season_mapping = {"Musim Semi": 1, "Musim Panas": 2, "Musim Gugur": 3, "Musim Dingin": 4}
    main_data = main_data[main_data['season'] == season_mapping[season]]

if workingday:
    main_data = main_data[main_data['workingday'] == 1]
else:
    main_data = main_data[main_data['workingday'] == 0]

# Overview
if option == "Overview":
    st.header("Overview Data")
    st.write(main_data.head())
    st.write(main_data.describe())

# Jam Penyewaan
elif option == "Jam Penyewaan":
    st.header("Jam Penyewaan Sepeda Tertinggi dan Terendah")
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='hr', y='cnt', data=main_data.groupby('hr')['cnt'].mean().reset_index())
    plt.title('Rata-rata Jumlah Penyewaan Sepeda per Jam')
    plt.xlabel('Jam')
    plt.ylabel('Rata-rata Jumlah Penyewaan Sepeda')
    st.pyplot(plt)

# Pengaruh Cuaca
elif option == "Pengaruh Cuaca":
    st.header("Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda")

    # Pengaruh suhu
    st.subheader("Pengaruh Suhu")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='temp', y='cnt', data=main_data)
    plt.title('Hubungan antara Suhu dan Jumlah Penyewaan Sepeda')
    plt.xlabel('Suhu')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    st.pyplot(plt)

    # Pengaruh kelembaban
    st.subheader("Pengaruh Kelembaban")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='hum', y='cnt', data=main_data)
    plt.title('Hubungan antara Kelembaban dan Jumlah Penyewaan Sepeda')
    plt.xlabel('Kelembaban')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    st.pyplot(plt)

    # Pengaruh kecepatan angin
    st.subheader("Pengaruh Kecepatan Angin")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='windspeed', y='cnt', data=main_data)
    plt.title('Hubungan antara Kecepatan Angin dan Jumlah Penyewaan Sepeda')
    plt.xlabel('Kecepatan Angin')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    st.pyplot(plt)

    # Pengaruh cuaca (weather)
    st.subheader("Pengaruh Kondisi Cuaca")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='weathersit', y='cnt', data=main_data)
    plt.title('Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    st.pyplot(plt)

# Clustering
elif option == "Clustering":
    st.header("Clustering Penyewaan Sepeda")

    # Memilih fitur untuk clustering
    features = ['temp', 'hum', 'windspeed', 'cnt']
    data_clustering = main_data[features]

    # Standarisasi fitur
    scaler = StandardScaler()
    data_clustering_scaled = scaler.fit_transform(data_clustering)

    # Menentukan jumlah cluster menggunakan metode Elbow
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
        kmeans.fit(data_clustering_scaled)
        wcss.append(kmeans.inertia_)

    plt.figure(figsize=(10, 6))
    plt.plot(range(1, 11), wcss)
    plt.title('Metode Elbow')
    plt.xlabel('Jumlah Cluster')
    plt.ylabel('WCSS')
    st.pyplot(plt)

    # Melakukan clustering dengan jumlah cluster optimal (misalnya 3)
    kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
    clusters = kmeans.fit_predict(data_clustering_scaled)

    # Menambahkan hasil clustering ke dataset
    main_data['Cluster'] = clusters

    # Visualisasi hasil clustering
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='temp', y='cnt', hue='Cluster', data=main_data, palette='viridis')
    plt.title('Clustering Penyewaan Sepeda Berdasarkan Suhu dan Jumlah Penyewaan')
    plt.xlabel('Suhu')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    st.pyplot(plt)

# Forecasting
elif option == "Forecasting":
    st.header("Forecasting Jumlah Penyewaan Sepeda")

    # Menggunakan data harian untuk time series forecasting
    df_day = main_data[['dteday', 'cnt']].drop_duplicates().copy()
    df_day['dteday'] = pd.to_datetime(df_day['dteday'])
    df_day.set_index('dteday', inplace=True)

    # Melakukan dekomposisi time series
    decomposition = seasonal_decompose(df_day['cnt'], model='additive', period=365)
    st.subheader("Dekomposisi Time Series")
    st.pyplot(decomposition.plot())

    # Melakukan forecasting menggunakan Holt-Winters Exponential Smoothing
    model = ExponentialSmoothing(df_day['cnt'], seasonal='additive', seasonal_periods=365)
    fit = model.fit()

    # Membuat prediksi untuk 365 hari ke depan
    forecast = fit.forecast(steps=365)

    # Visualisasi hasil forecasting
    plt.figure(figsize=(10, 6))
    plt.plot(df_day['cnt'], label='Data Aktual')
    plt.plot(forecast, label='Forecast', linestyle='--')
    plt.title('Forecasting Jumlah Penyewaan Sepeda')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    plt.legend()
    st.pyplot(plt)