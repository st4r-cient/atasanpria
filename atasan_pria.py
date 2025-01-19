import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter


st.title("Analisis Data Produk Atasan Pria")

# Upload file CSV
data_file = st.file_uploader("Upload file CSV", type=["csv"])
if data_file is not None:
    df = pd.read_csv(data_file)
    st.write("### Dataframe:")
    st.dataframe(df.head(2000))

    st.write("### Informasi Data:")
    st.text(df.info())

    st.write("### Statistik Data:")
    st.write(df.describe())

    # Handling missing values and duplicates
    st.write("### Jumlah Nilai Kosong:")
    st.write(df.isna().sum())

    st.write("### Jumlah Baris Duplikat:")
    st.write(df.duplicated().sum())

    # Mapping kategori
    mapping = {'Kaos Pria': 1, 'Kaos Polo Pria': 2, 'Kemeja Pria': 3}
    if 'category' in df.columns:
        df['category'] = df['category'].map(mapping)

        st.write("### Kategori Terpilih:")
        st.write(df['category'].value_counts())

    # Visualisasi Data
    st.write("### Visualisasi Hubungan Harga dan Rating:")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='price', y='rating', data=df, ax=ax)
    ax.set_title("Korelasi antara Harga dan Rating")
    st.pyplot(fig)

    st.write("### Visualisasi Jumlah Produk per Kategori:")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x='category', data=df, ax=ax)
    ax.set_title("Jumlah Produk per Kategori")
    st.pyplot(fig)

    st.write("### Distribusi Harga Produk:")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df['price'], bins=10, kde=True, ax=ax)
    ax.set_title("Distribusi Harga Produk")
    st.pyplot(fig)

    st.write("### Heatmap Korelasi:")
    numeric_df = df.select_dtypes(include=['number'])
    correlation_matrix = numeric_df.corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, ax=ax)
    ax.set_title("Heatmap Korelasi")
    st.pyplot(fig)
