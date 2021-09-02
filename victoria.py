import streamlit as st
import pandas as pd
import plotly.express as px





crops=pd.read_csv("df_crops.csv").set_index("Produce_Variety")

regions = pd.read_csv("df_regions.csv").set_index("County")
crops_per_month = pd.read_csv("df_crops_per_month.csv").set_index("Month")





selected_status = st.sidebar.selectbox(
    "Select Data to view",
    options=[
        "Average Prices Chart",
        "Average Prices Table",
        "Crops per month",
        "Regions",
        "Regions Table"

    ],
)

if selected_status=="Average Prices Chart":
    st.title("Average Prices chart")
    st.subheader("subhead average prices")
    st.bar_chart(crops)
if selected_status=="Average Prices Table":
    st.title("Average Prices Table")
    st.subheader("subhead average prices")
    st.table(crops)

if selected_status=="Crops per month":
    st.title("number of crops sold per month")
    st.subheader("the one with highest is the best")
    st.bar_chart(crops_per_month)

if selected_status=="Regions":
    st.title("number of crops sold per month")
    st.subheader("the one with highest is the best")
    st.line_chart(regions)


if selected_status=="Regions Table":
    st.title("Regions")
    st.subheader("Regions table")
    st.table(regions)