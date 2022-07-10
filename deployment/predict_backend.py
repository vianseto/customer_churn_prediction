import pandas as pd
import numpy as np
import joblib
import ast
import tensorflow as tf

def predict(gender,tenure,internetSvc,onlineSec,onlineBcp,deviceProtc,techSupp,payment,monthlyCrg,totalCrg):

    data = {
        'gender' : gender,	
        'tenure' : tenure,
        'InternetService' :	internetSvc,
        'OnlineSecurity' : onlineSec,
        'OnlineBackup' : onlineBcp,
        'DeviceProtection' : deviceProtc,
        'TechSupport' :	techSupp,
        'PaymentMethod' : payment,	
        'MonthlyCharges' : monthlyCrg,	
        'TotalCharges' : totalCrg,	 
        'Churn' : "No"
    }

    features = pd.DataFrame(data, index=[0])

    preprocessing = joblib.load("data_preparation.pkl")
    predictor = tf.keras.models.load_model("ann_model.h5")
    with open('list_used_columns.txt', 'r') as used:
        used_col = used.read()
    with open('list_num_columns.txt', 'r') as num:
        num_col = num.read()
    with open('list_cat_columns.txt', 'r') as cat:
        cat_col = cat.read()
    list_num_col = ast.literal_eval(num_col)
    list_cat_col = ast.literal_eval(cat_col)    

    inf_norm = pd.DataFrame(preprocessing.transform(features), columns=[list_num_col+list_cat_col])
    inf_norm = np.array(inf_norm.drop(columns='Churn'))
    inf_norm 

    result = predictor.predict(inf_norm)

    if result[0][0] >= 0.5:
        result = 'Stay With Us'
    else:
        result = 'Leave Us'
    return result