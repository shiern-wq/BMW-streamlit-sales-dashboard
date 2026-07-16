import streamlit as st
import pandas as pd

st.title("BMW Sales Dashboard")
st.markdown("Real-time transactional business operations insights")

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

st.subheader("Metrics")
st.metric("final_sale_price_usd", int(df["final_sale_price_usd"].sum()))

st.subheader("Filtered Sales Data")
st.dataframe(df)

drift_summary = clean_df.groupby('sale_year')[['msrp_usd','final_sale_price_usd','discount_percent']].mean().round(2)
display(drift_summary)
drift_summary.plot(kind='bar', figsize=(8,5))
plt.title('Data Drift Check: Average Pricing Variables by Year')
plt.xlabel('Sale Year'); plt.ylabel('Average Value')
plt.show()

