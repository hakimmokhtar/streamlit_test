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
    selected_currency = st.selectbox('Choose a currency to view exchange rate against MYR:', sorted(rates.keys()))

    # Display the exchange rate
    if selected_currency:
        exchange_rate = rates[selected_currency]
        st.success(f"1 MYR = {exchange_rate} {selected_currency}")
else:
    st.error(f"API call failed with status code: {response.status_code}")
