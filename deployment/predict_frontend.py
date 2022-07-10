import predict_backend
import streamlit as st
from PIL import Image

def app():
    colH1, colH2 = st.columns([0.05,10])
    colH2.header('Telco Customer Churn Predictor')
    st.write("")
    image = Image.open('T-1_new.jpeg')
    st.image(image)
    colH1, colH2 = st.columns([0.05,10])
    colH2.caption('This Application For **Predict** about Telco Customer is Churn or Not')

    gender = st.selectbox('Customer Gender',['Male','Female'])
    tenure = st.number_input('How Long The Customer Stay With Us (Month)', value=24)
    internetSvc = st.selectbox('Customer Internet Service', ['DSL','Fiber optic', 'No'])
    st.write("Facility Services Subscription :")
    colH1, colH2 = st.columns([5,5])
    onlineSec = colH1.selectbox('Online Security', ['Yes','No', 'No internet service'])
    onlineBcp = colH2.selectbox('Online Backup', ['Yes','No', 'No internet service'])
    deviceProtc = colH1.selectbox('Device Protection', ['Yes','No', 'No internet service'])
    techSupp = colH2.selectbox('Technical Support', ['Yes','No', 'No internet service'])
    payment = st.selectbox('Payment Method', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
    monthlyCrg = st.number_input('Customer Monthly Charge (USD$)', value=52.50)
    totalCrg = st.number_input('Customer Total Charge (USD$)', value=1208.15)

    col1, col2, col3 = st.columns([9,10,1])
    button = col2.button('Predict')

    if button == True:
      st.success(f'He / She will {predict_backend.predict(gender,tenure,internetSvc,onlineSec,onlineBcp,deviceProtc,techSupp,payment,monthlyCrg,totalCrg)} !')