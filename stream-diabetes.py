import streamlit as st
import pickle
import sys

try:
    import sklearn
except ImportError:
    st.error("Modul scikit-learn tidak ditemukan. Silakan pastikan untuk menginstalnya dengan menjalankan 'pip install scikit-learn'.")
    sys.exit(1)

# membaca model
try:
    diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
except FileNotFoundError:
    st.error("File diabetes_model.sav tidak ditemukan.")
    sys.exit(1)
except Exception as e:
    st.error(f"Terjadi kesalahan saat memuat model: {str(e)}")
    sys.exit(1)

# judul web
st.title('Data Mining Prediksi Diabetes')

#membagi kolom 
col1, col2 = st.columns(2)

pregnancies = col1.text_input('input nilai pregnancies')
Glucose = col2.text_input('input nilai glucose')
BloodPressure = col1.text_input('input nilai Blood Pressure')
SkinThickness = col2.text_input('input nilai Skin Thickness')
Insulin = col1.text_input('input nilai Insulin')
BMI = col2.text_input('input nilai BMI')
DiabetesPedigreeFunction = col1.text_input('input nilai Diabetes Pedigree Function')
Age = col2.text_input('input nilai Age')

# code untuk prediksi
diab_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('test prediksi diabetes') :
    try:
        # Konversi input ke tipe numerik
        input_data = [
            float(pregnancies), float(Glucose), float(BloodPressure), 
            float(SkinThickness), float(Insulin), float(BMI), 
            float(DiabetesPedigreeFunction), float(Age)
        ]

        diab_prediction = diabetes_model.predict([input_data])

        if (diab_prediction[0] == 1):
            diab_diagnosis = 'pasien terkena diabetes'
        else:
            diab_diagnosis = 'pasien tidak terkena diabetes'
    except ValueError:
        st.error("Pastikan semua nilai yang Anda masukkan adalah angka.")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat melakukan prediksi: {str(e)}")

st.success(diab_diagnosis)
