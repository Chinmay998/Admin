import streamlit as st
from role_selection_app import role_selection

st.title('CONTEXT')

def main():
    app_options = ["Role Selection", "Warehouse Selection"]  # Add more pages here
    selected_app = st.sidebar.selectbox("Select an Application", app_options)
    
    if selected_app == "Role Selection":
        role_selection(session)  # Import this function from your module
    
    # Add similar blocks for other pages here

if __name__ == "__main__":
    session = st.session_state['Session']
    main()
