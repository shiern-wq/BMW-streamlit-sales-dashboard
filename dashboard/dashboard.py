import streamlit as st
import pandas as pd
st.title("Sales Dashboard")
@st.cache_data
def load_data():
df = pd.read_csv("data/sales.csv", parse_dates=["date"])
return df
df = load_data()
st.sidebar.header("Filter Options")
region = st.sidebar.selectbox(
"Select Region",
options=["All"] + sorted(df["region"].unique().tolist())
)
if region != "All":
df = df[df["region"] == region]
product = st.sidebar.selectbox(
"Select Product",
options=["All"] + sorted(df["product"].unique().tolist())
)
if product != "All":
df = df[df["product"] == product]
st.subheader("Summary Metrics")
st.metric("Total Units Sold", int(df["units_sold"].sum()))
st.metric("Total Revenue", f"${df['revenue'].sum():,.2f}")
st.subheader("Revenue Over Time")
revenue_over_time = df.groupby("date")["revenue"].sum().reset_index()
st.line_chart(
revenue_over_time.rename(columns={"date":
"index"}).set_index("index")
)
st.subheader("Filtered Sales Data")
st.dataframe(df)
