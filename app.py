import streamlit as st
import pickle

# Load model
final_model = pickle.load(open('final_model.pkl', 'rb'))

st.title('Car Price Prediction')

# Inputs (matching dataset exactly)
insurance_validity = st.selectbox(
    "Insurance Validity",
    ['Comprehensive', 'Third Party Insurance', 'Third Party', 'Zero Dep', 'Not Available']
)

fuel_type = st.selectbox(
    "Fuel Type",
    ['Petrol', 'Diesel', 'CNG']
)

kms_driven = st.number_input("KMs Driven", min_value=0)

ownsership = st.selectbox(
    "Ownership",
    ['First Owner', 'Second Owner', 'Third Owner', 'Fourth Owner', 'Fifth Owner']
)

transmission = st.selectbox(
    "Transmission",
    ['Manual', 'Automatic']
)

# Correct mappings (matching training)
d1 = {
    'Comprehensive':0,
    'Third Party Insurance':1,
    'Third Party':1,
    'Zero Dep':2,
    'Not Available':3
}

d2 = {'Petrol':0, 'Diesel':1, 'CNG':2}

d3 = {'Manual':0, 'Automatic':1}

d4 = {
    'First Owner':1,
    'Second Owner':2,
    'Third Owner':3,
    'Fourth Owner':4,
    'Fifth Owner':5
}

# Prediction
if st.button('Predict Price'):
    test = [[
        d1[insurance_validity],
        d2[fuel_type],
        kms_driven,
        d4[ownsership],
        d3[transmission]
    ]]

    yp = final_model.predict(test)[0]
    st.success(f'Predicted Car Price: ₹ {round(yp,2)} lakhs')