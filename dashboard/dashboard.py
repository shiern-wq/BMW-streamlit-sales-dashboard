import streamlit as st
import pandas as pd

st.title("Sales Dashboard")

@st.cache_data
def load_data():
    df = pd.read_csv("data/sales.csv", parse_dates=["sale_date"])
    return df

df = load_data()

st.sidebar.header("Filter Options")

Country = st.sidebar.selectbox(
    "Select Country",
    options=["All"] + sorted(df["country"].unique().tolist())
)

if Country != "All":
    df = df[df["country"] == Country]

st.subheader("Metrics")
st.metric("final_sale_price_usd", int(df["final_sale_price_usd"].sum()))

st.subheader("Filtered Sales Data")
st.dataframe(df)
