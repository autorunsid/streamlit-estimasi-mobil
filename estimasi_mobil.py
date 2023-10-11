import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Km Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM Mobil')
enginesize = st.number_input('Input Ukuran Mesin Mobil')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, enginesize]]
    )
    st.write('Estimasi Harga Mobil Bekas dalam Ponds : ', predict)
    st.write('Estimasi Harga Mobil Bekas dalam IDR (Juta) : ', predict*19000)
