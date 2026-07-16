import streamlit as st
import pandas as pd

st.title("BMW Sales Dashboard")

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

Model = st.sidebar.selectbox(
    "Select Model",
    options=["All"] + sorted(df["model"].unique().tolist())
)

if Model != "All":
    df = df[df["model"] == Model]

Sales_Channel = st.sidebar.selectbox(
    "Select Sales_Chanel",
    options=["All"] + sorted(df["Sales Channel"].unique().tolist())
)

if Sales_Channel != "All":
    df = df[df["Sales Channel"] == Sales Channel]


st.subheader("Metrics")
st.metric("final_sale_price_usd", int(df["final_sale_price_usd"].sum()))

st.subheader("Filtered Sales Data")
st.dataframe(df)
