import streamlit as st
import requests

# Title of the app
st.title("Financial Management App")

# Sidebar navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Add Record", "View Records", "Financial Summary"])

# Add Record Page
if page == "Add Record":
    st.header("Add a New Record")
    
    # Input fields
    record_type = st.selectbox("Record Type", ["donations", "expenditures", "assets"])
    name = st.text_input("Name/Description")
    amount = st.number_input("Amount", step=0.01)
    purpose = st.text_input("Purpose (for donations)")
    category = st.text_input("Category (for expenditures)")
    condition = st.text_input("Condition (for assets)")
    date = st.date_input("Date")
    
    # Add Record Button
    if st.button("Add Record"):
        data = {
            'name': name,
            'amount': amount,
            'purpose': purpose,
            'category': category,
            'condition': condition,
            'date': date.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Send POST request to Flask backend
        try:
            response = requests.post("http://192.168.100.43:5000/add", data=data)
            if response.status_code == 200:
                st.success("Record added successfully!")
            else:
                st.error(f"Failed to add record. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to the server: {e}")

# View Records Page
elif page == "View Records":
    st.header("View Records")
    
    # Select table to view
    table = st.selectbox("Select Table", ["donations", "expenditures", "assets"])
    
    # View Records Button
    if st.button("View"):
        try:
            response = requests.get(f"http://192.168.100.43:5000/view/{table}")
            if response.status_code == 200:
                records = response.json()
                st.table(records)
            else:
                st.error(f"Failed to fetch records. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to the server: {e}")

# Financial Summary Page
elif page == "Financial Summary":
    st.header("Financial Summary")
    
    # Get Summary Button
    if st.button("Get Summary"):
        try:
            response = requests.get("http://192.168.100.43:5000/summary")
            if response.status_code == 200:
                summary = response.json()
                st.write(f"Total Donations: {summary['total_donations']}")
                st.write(f"Total Expenditures: {summary['total_expenditures']}")
                st.write(f"Balance: {summary['balance']}")
                st.write(f"Total Assets: {summary['total_assets']}")
            else:
                st.error(f"Failed to fetch summary. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to the server: {e}")
