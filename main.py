# import streamlit as st
# import configparser
# from snowflake.snowpark import Session
# from Log_in import sfAccount_selector, session_builder
# from Context import role_selection


# st.title('Multi-Page App')
# config = configparser.ConfigParser()
# config.sections()
# config.read('config.ini')

# def main():
#     page_options = ["Log_in", "CONTEXT"]  # Add more pages here
#     selected_page = st.sidebar.selectbox("Select a Page", page_options)
    
#     if selected_page == "Login":
#         conn = sfAccount_selector(config)  # Get 'conn' from sfAccount_selector
#         if conn is not None:
#             session = Session.builder.configs(conn).create()  # Pass 'conn' to session_builder
    
#     if session is not None:
#         if selected_page == "Role Selection":
#             role_selection(session)
    
   
# if __name__ == "__main__":
#     main()

import streamlit as st
from Log_in import sfAccount_selector,config
from snowflake.snowpark import Session
from Context import role_selection

st.title('Multi-Page App')

# Define a Streamlit session state variable to store the 'session' object
if 'session' not in st.session_state:
    st.session_state.session = None

def main():
    page_options = ["Log_in", "CONTEXT"]  # Add more pages here
    selected_page = st.sidebar.selectbox("Select a Page", page_options)

    if selected_page == "Log_in":
        if st.session_state.session is None:
            conn = sfAccount_selector(config)  # Use your config object from login.py
            if conn is not None:
                st.session_state.session = Session.builder.configs(conn).create()

    if st.session_state.session is not None:
        if selected_page == "Context":
            role_selection(st.session_state.session)  # Pass the 'session' object to role_selection

    # Add similar blocks for other pages

if __name__ == "__main__":
    main()

