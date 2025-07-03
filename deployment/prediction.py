# import libraries
import pandas as pd
import streamlit as st
import pickle
import json

def run():

    # import numeric column data
    with open('src/num_cols.txt', 'r') as f_num:
        num_cols = json.load(f_num)

    # import categorical column data
    with open('src/cat_cols.txt', 'r') as f_cat:
        cat_cols = json.load(f_cat)

    # import classification model
    with open('src/best_model.pkl', 'rb') as f_model:
        best_model = pickle.load(f_model)
        
    st.title("Churn Prediction")
    st.write("")
    # variable for customer information
    customer_id = st.text_input(label = 'Input customer_id', value = "")  # input for customer_id column
    gender = st.selectbox(label = 'Choose customers\' gender', options = ['male', 'female']) # input for gender column
    senior_citizen = st.selectbox(label = 'Are customers a senior citizen?',  # inpur for senior_citizen column
                             options = ['yes', 'no'])
    partner = st.selectbox(label = 'Are customers having a partner?', options = ['yes', 'no']) # input for partner column
    dependents = st.selectbox(label = 'Are customers having dependents?', options = ['yes', 'no']) # input for dependents column
    tenure = st.number_input(label = 'Input customers tenure', min_value = 0) # input for tenure column
    phone_service = st.selectbox(label = 'Are customers having phone service?', options = ['yes', 'no']) # input for phone_service column
    multiple_lines = st.selectbox(label = 'Are customers having multiple phone service lines?', # input for multiple_lines column
                                options = ['yes', 'no', 'no phone service'])
    internet_service = st.selectbox(label = 'Customers internet service type', options = ['no', 'dsl', 'fiber optic']) # input for internet_service column
    online_security = st.selectbox(label = 'Are customers subscribe to our antivirus products?', # input for online_security column
                                   options = ['no', 'yes', 'no internet service'])
    streaming_tv = st.selectbox(label = 'Are customers subsribing to our streaming tv services?', # input for streaming_tv column
                                options = ['yes', 'no', 'no internet service'])
    contract = st.selectbox(label = 'Customers contract type', options = ['one year', 'month-to-month', 'two year']) # input for contract column
    paperless_billing = st.selectbox(label = 'Are customers prefer paperless billing?', # input for paperless_billing column
                                     options = ['yes', 'no'])
    payment_method = st.selectbox(label = 'Customers preferred payment methods', # input for payment_method column
                                  options = ['bank transfer (automatic)', 'electronic check', 'credit card (automatic)',
                                             'mailed check'])
    monthly_charges = st.number_input(label = 'Customers charges per month', # input for monthly_charges column
                                      min_value = 0.0)
    total_charges = st.number_input(label = 'Customers total charges until now', # input for total_charges column
                                    min_value = 0.0)


    # create variable for dataframe
    data = pd.DataFrame([{'customer_id': customer_id,
                     'gender': gender,
                     'senior_citizen': senior_citizen,
                     'partner': partner,
                     'dependents': dependents,
                     'tenure': tenure,
                     'phone_service': phone_service,
                     'multiple_lines': multiple_lines,
                     'internet_service': internet_service,
                     'online_security': online_security,
                     'streaming_tv': streaming_tv,
                     'contract': contract,
                     'paperless_billing': paperless_billing,
                     'payment_method': payment_method,
                     'monthly_charges': monthly_charges,
                     'total_charges': total_charges
                     }])

    
    df_class = data.copy()
    
    if st.button(label = 'predict'):
        y_pred_inf = best_model.predict(df_class)
        if y_pred_inf[0] == 1:
            st.write('Customers predited will churn')
        elif y_pred_inf[0] == 0:
            st.write('Customers predicted will not churn')