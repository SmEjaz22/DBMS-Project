import streamlit as st
import pyodbc


# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return pyodbc.connect("DRIVER={SQL Server};SERVER=" +
                          st.secrets['server'] +';DATABASE=' +
                          st.secrets['database'])

conn = init_connection()


# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


rows = run_query("SELECT * from mytable;")

# Print results.
for i in rows:
    st.write(
        f"{i[0]} has name {i[1]} ,contact no is {i[2]} and ID card is: {i[3]}")
