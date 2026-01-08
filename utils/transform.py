import pandas as pd
import numpy as np
from datetime import datetime
import warnings

# Menonaktifkan peringatan FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)
pd.set_option('future.no_silent_downcasting', True)

def clean_product_data(product_list):
    """Membersihkan dan mentransformasi data produk menjadi format yang diinginkan."""

    # Mengubah data produk menjadi DataFrame
    data_frame = pd.DataFrame(product_list)

    # Menghapus baris dengan judul yang tidak valid
    data_frame = data_frame[data_frame['title'].str.lower() != 'unknown product']

    # Membersihkan dan mengonversi harga
    data_frame['price'] = data_frame['price'].replace(r'[^\d.]', '', regex=True)
    data_frame['price'] = data_frame['price'].replace('', np.nan)
    data_frame.dropna(subset=['price'], inplace=True)
    data_frame['price'] = data_frame['price'].astype(float) * 16000  # USD ke IDR

    # Perbaikan parsing rating: ekstrak angka desimal pertama saja
    data_frame['rating'] = data_frame['rating'].str.extract(r'([0-5]\.\d)')
    data_frame.dropna(subset=['rating'], inplace=True)
    data_frame['rating'] = data_frame['rating'].astype(float)

    # Membersihkan informasi warna (menghapus non-digit)
    data_frame['colors'] = data_frame['colors'].replace(r'\D', '', regex=True)
    data_frame['colors'] = data_frame['colors'].replace('', np.nan)
    data_frame.dropna(subset=['colors'], inplace=True)
    data_frame['colors'] = data_frame['colors'].astype(int)

    # Membersihkan informasi ukuran dan gender
    data_frame['size'] = data_frame['size'].replace(r'Size:\s*', '', regex=True)
    data_frame['gender'] = data_frame['gender'].replace(r'Gender:\s*', '', regex=True)

    # Menghapus baris duplikat dan data yang kosong
    data_frame.drop_duplicates(inplace=True)
    data_frame.dropna(inplace=True)

    # Menambahkan kolom timestamp
    data_frame['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return data_frame
