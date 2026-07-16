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

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_items = filtered_df["Quantity"].sum()
avg_margin = (total_profit / total_sales) * 100 if total_sales > 0 else 0

with kpi1:
    st.metric(label="Total Revenue", value=f"${total_sales:,.2f}", delta="+4.2%")

with kpi2:
    st.metric(label="Net Profit", value=f"${total_profit:,.2f}", delta=f"+${total_profit*0.02:,.2f}")

with kpi3:
    st.metric(label="Units Sold", value=f"{total_items:,}", delta="-1.5%", delta_color="inverse")

with kpi4:
    st.metric(label="Profit Margin", value=f"{avg_margin:.1f}%", delta="0.8%")

st.markdown("---") # Visual separator divider
