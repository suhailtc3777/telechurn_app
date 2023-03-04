# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 00:08:08 2023

@author: suhail
"""

import numpy as np
import pickle
import streamlit as st

#load saved model
load_model = pickle.load(open("C:/Users/suhail/deployment_3pm/Svm_model.pkl","rb"))

# Creating a function for prediction
    
def telecom_pred(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = load_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person will not be churned'
    else:
      return 'The person will churned'
  
def main():
    
    # giving a titile
    st.title("telecom Churn Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Telcecom churn app </h2>
    </div>
    """
    
    # getting the input data from user
   
    account_length = st.text_input("Account Length")
    voice_plan = st.text_input("Voice plan")
    voice_messages = st.text_input("Voice Messages")
    intl_plan = st.text_input("International Plan")
    customer_calls = st.text_input("Customer Calls")
    total_charges = st.text_input("Total Charges")
    total_calls = st.text_input("total calls")
    total_mins = st.text_input("Total Minutes")
    
    # code for prediction
    tele_churn = " "
    
    # creating a Button for prediction
     
    if st.button("Submit"):
        tele_churn = telecom_pred([account_length,voice_plan,voice_messages,intl_plan,customer_calls,total_charges,total_calls,total_mins])
    
    
    st.success(tele_churn)
    
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    