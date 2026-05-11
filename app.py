import streamlit as st

# Menambahkan Judul
st.title('Aplikasi Pertama Saya')

# Menambahkan Teks
st.write('Halo, ini adalah aplikasi web pertama yang saya buat dengan Streamlit!')

# Menambahkan Input
nama = st.text_input('Masukkan Nama Anda:')
if nama:
    st.write(f'Halo, {nama}!')
