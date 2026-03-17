
import streamlit as st
from orchestrator.crew import run_crew
from PIL import Image
import os

st.set_page_config(page_title="AI Financial Analyst Crew", layout="wide")

st.title("📊 AI Financial Analyst Crew")
st.write("Multi-agent stock analysis dashboard 🤖")

st.sidebar.header("Controls")
company = st.sidebar.text_input("Company Name", "Tesla")
ticker = st.sidebar.text_input("Stock Ticker", "TSLA")

if st.sidebar.button("Run Analysis 🚀"):
    if not company or not ticker:
        st.error("Please enter both company and ticker")
    else:
        with st.spinner("Agents are working..."):
            report, logs = run_crew(company, ticker)

        st.success("Analysis Complete!")

        st.subheader("📰 Market News")

        if "No meaningful recent news found." in report:
            st.info("No strong news signals found for this stock.")
        else:
            for line in report.split("\n"):
                if "Sentiment" in line:
                    st.write(line)

        chart_path = f"output/charts/{ticker}.png"
        if os.path.exists(chart_path):
            st.subheader("📈 Stock Chart")
            st.image(Image.open(chart_path))

        st.subheader("🤖 Agent Logs")
        st.code(logs)
