import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


@st.cache
def dataLoad():
    data=pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn_new.csv")
    return data

def app():
    st.header('Telco Customer Churn Analysis')
    st.write("")
    st.subheader('Customer Data')
    st.write("")
    data=dataLoad().drop("Unnamed: 0",axis=1)
    st.write(data)
    st.write("")
    st.subheader('Analysis')
    colW1, colW2= st.columns([0.1,5])
    colW2.write('- Customer Churn Rate')
    
    fig1,ax1=plt.subplots(figsize=(20,8))
    data.Churn.value_counts().plot(kind='pie', labels=['',''], autopct='%.0f%%', figsize=[10,10], fontsize=15, ax=ax1)
    ax1.set_title('Customer Churn Rate', fontsize=15)
    ax1.set_ylabel('')
    ax1.legend(labels=['No','Yes'], fontsize=20, loc='best')
    st.pyplot(fig1)
    st.write("Berdasarkan hasil diagram diatas dapat diketahui bahwa \
        customer cenderung loyal, karena memiliki `churn rate` yang terbilang cukup rendah")

    colW1, colW2= st.columns([0.1,5])
    colW2.write('- Customer Tenure')
    churn = st.selectbox('Customer Tenure Based on', ['All','No Churn','Churn'])

    fig2,ax2=plt.subplots(figsize=(15,8))
    sns.histplot(data = data[data.Churn=='No'], x = 'tenure', legend = True, ax=ax2)
    ax2.set_title('Customer Tenure by No Churn Customer')

    fig3,ax3=plt.subplots(figsize=(15,8))
    sns.histplot(data = data[data.Churn=='Yes'], x = 'tenure', legend = True, ax=ax3)
    ax3.set_title('Customer Tenure by Churn Customer')

    fig4,ax4=plt.subplots(figsize=(15,8))
    sns.histplot(data = data, x = 'tenure', hue='Churn', legend = True, ax=ax4)
    ax4.set_title('Customer Tenure')

    if churn == 'All':
        st.pyplot(fig4)
    elif churn == 'No Churn':
        st.pyplot(fig2)
    else:
        st.pyplot(fig3)

    st.write("Berdasarkan hasil diatas dapat disimpulkan bahwa \
             dengan semakin lama `tenure` maka semakin menurun juga \
             tingkat `churn` seorang customer, customer `churn` terbanyak \
             terdapat pada customer yang baru berlangganan dibawah setengah tahun")

    colW1, colW2= st.columns([0.1,5])
    colW2.write('- Services Facility')

    services = st.selectbox('Customer Churn Based on Facility Services', ['Online Security','Online Backup','Device Protection', 'Tech Support'])

    fig5,ax5=plt.subplots(figsize=(15,8))
    sns.countplot(x="OnlineSecurity", hue="Churn", data=data, ax=ax5)
    ax5.set_title('Customer Churn Rate Based on Online Security')

    fig6,ax6=plt.subplots(figsize=(15,8))
    sns.countplot(x="OnlineBackup", hue="Churn", data=data, ax=ax6)
    ax6.set_title('Customer Churn Rate Based on Online Backup')

    fig7,ax7=plt.subplots(figsize=(15,8))
    sns.countplot(x="DeviceProtection", hue="Churn", data=data, ax=ax7)
    ax7.set_title('Customer Churn Rate Based on Device Protection')

    fig8,ax8=plt.subplots(figsize=(15,8))
    sns.countplot(x="TechSupport", hue="Churn", data=data, ax=ax8)
    ax8.set_title('Customer Churn Rate Based on Tech Support')

    if services == 'Online Security':
        st.pyplot(fig5)
    elif services == 'Online Backup':
        st.pyplot(fig6)
    elif services == 'Device Protection':
        st.pyplot(fig7)
    else:
        st.pyplot(fig8)

    st.write("Berdasarkan hasil diatas dapat disimpulkan bahwa customer akan cenderung \
        churn ketika memilih untuk tidak berlangganan dalam beberapa fasilitas tambahan \
        yang diberikan seperti `Online Security`, `Online Backup`, `Device Protection`, dan \
        `Tech Support`. Dapat diasumsikan bahwa terdapat biaya tambahan apabila customer ingin \
        berlangganan pada fasilitas tambahan sehingga beberapa customer akan churn karena perlu \
        biaya yang lebih banyak apabila ingin mendapatkan fasilitas tersebut dan mungkin penyedia \
        jasa layanan lainnya tidak memberlakukan biaya tambahan apabila customer ingin menikmati fasilitas tersebut.")

    colW1, colW2= st.columns([0.1,5])
    colW2.write('- Customer Demographics')
    demographics = st.selectbox('Customer Churn Based on Demographics', ['Gender','Senior Citizen','Partner', 'Dependents'])
    
    fig9,ax9=plt.subplots(figsize=(15,8))
    sns.countplot(x="gender", hue="Churn", data=data, ax=ax9)
    ax9.set_title('Customer Churn Rate Based on Gender')

    fig10,ax10=plt.subplots(figsize=(15,8))
    sns.countplot(x="SeniorCitizen", hue="Churn", data=data, ax=ax10)
    ax10.set_title('Customer Churn Rate Based on Senior Citizen')

    fig11,ax11=plt.subplots(figsize=(15,8))
    sns.countplot(x="Partner", hue="Churn", data=data, ax=ax11)
    ax11.set_title('Customer Churn Rate Based on Partner')

    fig12,ax12=plt.subplots(figsize=(15,8))
    sns.countplot(x="Dependents", hue="Churn", data=data, ax=ax12)
    ax12.set_title('Customer Churn Rate Based on Dependents')

    if demographics == 'Gender':
        st.pyplot(fig9)
    elif demographics == 'Senior Citizen':
        st.pyplot(fig10)
    elif demographics == 'Partner':
        st.pyplot(fig11)
    else:
        st.pyplot(fig12)
    
    st.write("Berdasarkan hasil diatas dapat disimpulkan bahwa demografi seorang customer tidak terlalu mempengaruhi churn rate")
    
    colW1, colW2= st.columns([0.1,5])
    colW2.write('- Customer Contract')
    
    fig13,ax13=plt.subplots(figsize=(15,8))
    sns.countplot(x="Contract", hue="Churn", data=data, ax=ax13)
    ax13.set_title('Customer Churn Based on Contract')
    st.pyplot(fig13)

    st.write("Berdasarkan hasil diatas dapat disimpulkan bahwa customer cenderung `churn` ketika baru berlangganan dalam beberapa bulan")

    colW1, colW2= st.columns([0.1,5])
    colW2.write('- Payment Method')
    fig14,ax14=plt.subplots(figsize=(15,8))
    data.PaymentMethod.value_counts().plot(kind='pie', autopct='%.0f%%', figsize=[10,10], fontsize=15, ax=ax14)
    ax14.set_title('Customer Churn Based on Payment Method', fontsize=15)
    ax14.set_ylabel('')
    st.pyplot(fig14)

    st.write("Berdasarkan hasil diatas dapat diketahui bahwa customer \
        masih banyak yang melakukan pembayaran secara manual daripada \
        otomatis dan dapat diasumsikan bahwa customer yang melakukan \
        pembayaran secara otomatis merupakan customer yang sudah mapan secara ekonomi")