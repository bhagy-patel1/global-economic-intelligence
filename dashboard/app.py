import streamlit as st
import pandas as pd
import plotly.express as px
import os

df = pd.read_csv(os.path.join(os.path.dirname(__file__), "../data/processed/economic_master_dataset.csv"))

st.title("🌍 Global Economic Intelligence Dashboard")

st.write("Analysis of global economic indicators using World Bank data")

country = st.selectbox("Select Country", df["Country Name"].unique())

year = st.selectbox("Select Year", sorted(df["Year"].unique()))

country_data = df[(df["Country Name"] == country) & (df["Year"] == year)]

st.subheader("Economic Indicators")

st.write(country_data[[
    "GDP_Growth",
    "Inflation",
    "Unemployment",
    "Exports",
    "Population"
]])
fig = px.bar(
    x=["GDP_Growth", "Inflation", "Unemployment", "Exports"],
    y=[country_data["GDP_Growth"].values[0], country_data["Inflation"].values[0], country_data["Unemployment"].values[0], country_data["Exports"].values[0]]
)

st.plotly_chart(fig)
st.subheader("Global GDP Growth Map")

fig = px.choropleth(
    df[df["Year"] == year],
    locations="Country Code",
    color="GDP_Growth",
    hover_name="Country Name",
    color_continuous_scale="Viridis"
)

st.plotly_chart(fig)