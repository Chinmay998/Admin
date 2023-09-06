# import configparser
# from snowflake.snowpark import Session
# from snowflake.snowpark.functions import *
# import pandas as pd
# import streamlit as st
# st.title('CONTEXT')
# def role_selection(session):
#     role_df = session.sql('show roles;').collect()
#     role_df = pd.DataFrame(role_df)
#     role_list = role_df['name']
#     role_select = st.sidebar.selectbox('Select a Role', role_list)
#     if st.sidebar.button('Use Role'):
#         set_role = session.sql(f'''USE ROLE {role_select} ;''').collect()
#         st.session_state.selected_role = role_select
        

# def warehouse_selection(session):
#     try:
#         warehouse_df = session.sql('show warehouses;').collect()
#         warehouse_df = pd.DataFrame(warehouse_df)
    
#         warehouse_list = warehouse_df['name']
#         warehouse_select = st.sidebar.selectbox('Select a Role', warehouse_list)
#         if st.sidebar.button('Use Warehouse'):
#             set_warehouse = session.sql(f'''USE WAREHOUSE {warehouse_select} ;''').collect()
#             st.session_state.selected_warehouse = warehouse_select
    
#     except Exception as e:
#         #st.sidebar.error(f"Error fetching warehouse: {e}")
#         warehouse_list = [] #clear the warehouse list
#         warehouse_select = st.sidebar.selectbox('Select a Warehouse', warehouse_list)


import streamlit as st
import pandas as pd

def role_selection(session):
    query = 'show roles;'  # Define your SQL query here
    role_df = session.sql(query).collect()
    role_df = pd.DataFrame(role_df)
    role_list = role_df['name']
    role_select = st.sidebar.selectbox('Select a Role', role_list)
    if st.sidebar.button('Use Role'):
        set_role = session.sql(f'''USE ROLE {role_select} ;''').collect()
        st.session_state.selected_role = role_select



if __name__ == "__main__":
    session = st.session_state['Session'] 
    role_selection(session)
    warehouse_selection(session)
