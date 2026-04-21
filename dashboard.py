
import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="SOC Simulation System", layout="wide")

st.title("🛡️ Cyber Incident Response & SOC Simulation System")
st.markdown("### Upload a CSV file or paste CSV data to see alerts")

# Two tabs: Upload file OR Paste CSV
tab1, tab2 = st.tabs(["📂 Upload CSV File", "📋 Paste CSV Data"])

df = None

# Tab 1: File uploader
with tab1:
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success(f"✅ Loaded {len(df)} log entries from file!")

# Tab 2: Paste CSV text
with tab2:
    st.markdown("Paste your CSV data below. The first row must contain column headers: `Source_IP, Attack_Type, Timestamp`")
    pasted_csv = st.text_area("📝 Paste CSV here", height=200)
    if st.button("🔍 Load Pasted CSV"):
        if pasted_csv:
            try:
                df = pd.read_csv(io.StringIO(pasted_csv))
                st.success(f"✅ Loaded {len(df)} log entries from pasted data!")
            except Exception as e:
                st.error(f"Error reading CSV: {e}")
        else:
            st.warning("Please paste some CSV data first.")

# If no data loaded yet, use sample data
if df is None:
    try:
        df = pd.read_csv("network_logs.csv")
        st.info("📊 Using sample data. Upload a file or paste CSV to see your own alerts.")
    except:
        st.error("No data file found. Please upload or paste CSV data.")
        st.stop()

# Check required columns
required_cols = ["Attack_Type", "Source_IP", "Timestamp"]
missing = [col for col in required_cols if col not in df.columns]
if missing:
    st.error(f"Missing required columns: {missing}. Your CSV must have: Attack_Type, Source_IP, Timestamp")
    st.stop()

# Show alerts (Attack_Type != "Normal")
alerts = df[df["Attack_Type"] != "Normal"]

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("🚨 Total Alerts", len(alerts))
col2.metric("📊 Total Logs", len(df))
col3.metric("⚠️ Attack Rate", f"{(len(alerts)/len(df))*100:.1f}%")

st.divider()

# Alerts table
st.subheader("🔴 Live Security Alerts")
st.dataframe(alerts[["Source_IP", "Attack_Type", "Timestamp"]].head(20), use_container_width=True)

# Chart
st.subheader("📈 Attack Type Distribution")
attack_counts = df["Attack_Type"].value_counts()
st.bar_chart(attack_counts)

st.divider()
st.caption("🔐 SOC Simulation System | Paste CSV or upload file to analyze your logs")
