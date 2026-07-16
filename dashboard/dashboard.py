import streamlit as st
import pandas as pd

st.title("BMW Sales Dashboard")
st.markdown("Real-time transactional business operations insights")
page_icon="🚗",
    layout="wide"

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

# -------------------------------
# KPI Cards
# -------------------------------

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Total Sales",
    len(filtered)
)

c2.metric(
    "Average MSRP",
    f"${filtered['msrp_usd'].mean():,.0f}"
)

c3.metric(
    "Average Final Price",
    f"${filtered['final_sale_price_usd'].mean():,.0f}"
)

c4.metric(
    "Average Satisfaction",
    f"{filtered['customer_satisfaction_score'].mean():.2f}"
)

st.markdown("---")

# -------------------------------
# Visualization 1
# -------------------------------

col1,col2 = st.columns(2)

fig = px.histogram(
    filtered,
    x="final_sale_price_usd",
    nbins=30,
    title="Distribution of Final Sale Price"
)

col1.plotly_chart(fig,use_container_width=True)

# -------------------------------
# Visualization 2
# -------------------------------

fig2 = px.scatter(
    filtered,
    x="msrp_usd",
    y="final_sale_price_usd",
    color="fuel_type",
    title="MSRP vs Final Sale Price"
)

col2.plotly_chart(fig2,use_container_width=True)

# -------------------------------
# Visualization 3
# -------------------------------

fig3 = px.bar(
    filtered.groupby("region")["final_sale_price_usd"].mean().reset_index(),
    x="region",
    y="final_sale_price_usd",
    title="Average Final Sale Price by Region"
)

st.plotly_chart(fig3,use_container_width=True)

# -------------------------------
# Visualization 4
# -------------------------------

fig4 = px.box(
    filtered,
    x="fuel_type",
    y="final_sale_price_usd",
    title="Fuel Type vs Final Price"
)

st.plotly_chart(fig4,use_container_width=True)

st.markdown("---")

# -------------------------------
# Prediction Section
# -------------------------------

st.header("Prediction")

st.info("Example Prediction")

msrp = st.number_input(
    "MSRP",
    value=60000
)

discount = st.number_input(
    "Discount (%)",
    value=5.0
)

# Simple prediction formula
predicted_price = msrp * (1-discount/100)

st.success(
    f"Predicted Final Sale Price = ${predicted_price:,.2f}"
)

st.markdown("---")

# -------------------------------
# Data Table
# -------------------------------

st.subheader("Metrics")
st.metric("final_sale_price_usd", int(df["final_sale_price_usd"].sum()))

st.subheader("Filtered Sales Data")
st.dataframe(df)
