import streamlit as st
from login import sfAccount_selector, session_builder
from role_selection import role_selection
from other_app import other_app  # Import other application functions

st.title('Multi-Page App')

def main():
    page_options = ["Log_in", "CONTEXT"]  # Add more pages here
    selected_page = st.sidebar.selectbox("Select a Page", page_options)

    if selected_page == "Log_in":
        # Call functions from login.py module
        sfAccount_selector(config)
        session_builder(conn)
    
    elif selected_page == "CONTEXT":
        role_selection()  # Call the function from role_selection.py module
    
   
if __name__ == "__main__":
    main()
