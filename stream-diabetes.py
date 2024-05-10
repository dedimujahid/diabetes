import streamlit as st
import pickle

# membaca model
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

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
    
st.success(diab_diagnosis)
