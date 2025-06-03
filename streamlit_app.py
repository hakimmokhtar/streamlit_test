import streamlit as st
import requests

# Set the app title
st.title('PENCARIAN ENGINEER DAFFIM SDN BHD!!') 

# Add a welcome message 
st.write('Welcome to DAFFIM SDN BHD!') 

# Create a text input 
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!') 

# Display the customized message 
st.write('Customized Message:', widgetuser_input)

# API call to get exchange rates with base MYR
response = requests.get('https://api.vatcomply.com/rates?base=MYR')

if response.status_code == 200:
    data = response.json()
    rates = data.get('rates', {})

    # Dropdown (selectbox) to choose a currency
    selected_currency = st.selectbox('Choose a currency to convert MYR to:', sorted(rates.keys()))

    # User input: amount in MYR
    amount_myr = st.number_input('Enter amount in MYR:', min_value=0.0, value=1.0, step=0.1)

    # Conversion and result display
    if selected_currency and amount_myr:
        rate = rates[selected_currency]
        converted_amount = amount_myr * rate
        st.success(f"{amount_myr:.2f} MYR = {converted_amount:.2f} {selected_currency}")

else:
    st.error(f"API call failed with status code: {response.status_code}")
