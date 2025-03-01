import streamlit as st

st.title("VMC Machine Monitoring Dashboard")

st.header("Machine Parameter")

# Actual temperature from machine manual
actual_temperature = 50  # Fixed reference value

# Placeholder for real-time temperature (empty for now)
real_time_temperature = ""

# Display the temperature values
st.write("### Temperature (°C)")
col1, col2 = st.columns(2)
col1.metric(label="Actual Value", value=f"{actual_temperature} °C")
col2.metric(label="Real-Time Value", value=real_time_temperature)

st.info("🔄 Real-time data integration coming soon!")
