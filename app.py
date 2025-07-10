import streamlit as st
import pandas as pd
import base64
import request

st.title = ("Read CSV from GitHub")

url = "https://raw.githubusercontent.com/kaixxxnnn/testing/main/data.csv"

def load_data():
  return pd.read_csv(url)

try:
  df = load_data()
  st.success("Data loaded sucessfully!")
  st.dataframe(df)
except Exception as e:
  st.error(f"Failed to load data: {e}")
