import streamlit as st
import configparser
from snowflake.snowpark import Session
from Log_in import sfAccount_selector, session_builder
from Context import role_selection


st.title('Multi-Page App')
config = configparser.ConfigParser()
config.sections()
config.read('config.ini')

def main():
    page_options = ["Log_in", "CONTEXT"]  # Add more pages here
    selected_page = st.sidebar.selectbox("Select a Page", page_options)

    if selected_page == "Login":
        conn = sfAccount_selector(config)  # Get 'conn' from sfAccount_selector
        if conn is not None:
            session = Session.builder.configs(conn).create()  # Pass 'conn' to session_builder
    
    elif selected_page == "CONTEXT":
        role_selection(Session)  # Call the function from role_selection.py module
    
   
if __name__ == "__main__":
    main()
