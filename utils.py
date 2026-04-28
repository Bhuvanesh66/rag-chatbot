# utils.py
import os
from dotenv import load_dotenv
import streamlit as st

def get_api_key():
    # Force-load .env from current project folder
    load_dotenv(dotenv_path=".env", override=True)

    # 1) Try environment (local dev)
    key = os.getenv("GITHUB_TOKEN")

    # 2) Fallback to Streamlit secrets (for cloud)
    if not key and "GITHUB_TOKEN" in st.secrets:
        key = st.secrets["GITHUB_TOKEN"]

    return key