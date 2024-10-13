import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Set the Streamlit page configuration
st.set_page_config(page_title="Kenya Weather Dashboard", layout="wide")

# Load weather data
@st.cache_data
def load_data():
    return pd.read_csv("kenya_weather_data.csv")

df = load_data()

# Sidebar filters
st.sidebar.header("Filter the Data")

# Select town
towns = df['town'].unique().tolist()
selected_town = st.sidebar.multiselect("Select Town(s)", towns, default=towns)

# Select date range
# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Select date range
min_date = df['date'].min().to_pydatetime()  # Convert to native Python datetime
max_date = df['date'].max().to_pydatetime()  # Convert to native Python datetime

selected_date_range = st.sidebar.slider(
    "Select Date Range",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date),
    format="MM/DD/YY"  # Optional: customize date format
)



# Filter data based on user selections
filtered_df = df[(df['town'].isin(selected_town)) & 
                 (df['date'] >= selected_date_range[0].strftime("%Y-%m-%d")) & 
                 (df['date'] <= selected_date_range[1].strftime("%Y-%m-%d"))]

# Display filtered data
st.write(f"### Weather Data ({len(filtered_df)} rows)")
st.dataframe(filtered_df)

# Create plots for analysis
st.write("## Weather Analysis")

# Average temperature by town
st.write("### Average Temperature by Town")
avg_temp_by_town = filtered_df.groupby('town')['avg_temp_c'].mean().reset_index()

# Plot using Plotly for interactive visualization
fig_avg_temp = px.bar(avg_temp_by_town, x='town', y='avg_temp_c', title="Average Temperature by Town", labels={'avg_temp_c': 'Average Temperature (C)'})
st.plotly_chart(fig_avg_temp)

# Distribution of max temperature
st.write("### Distribution of Max Temperature")
fig, ax = plt.subplots()
sns.histplot(filtered_df['max_temp_c'], bins=20, kde=True, ax=ax)
ax.set_title('Distribution of Max Temperature')
st.pyplot(fig)

# Scatter plot for avg temperature vs humidity
st.write("### Avg Temperature vs Humidity")
fig_temp_humidity = px.scatter(filtered_df, x='avg_temp_c', y='humidity', color='town', title='Avg Temperature vs Humidity')
st.plotly_chart(fig_temp_humidity)

# Line chart for temperature trends over time
st.write("### Temperature Trends Over Time")
fig_temp_trends = px.line(filtered_df, x='date', y='avg_temp_c', color='town', title='Temperature Trends Over Time')
st.plotly_chart(fig_temp_trends)

# Scatter plot for Avg Temperature vs Precipitation
st.write("### Avg Temperature vs Precipitation")
fig_temp_precip = px.scatter(filtered_df, x='avg_temp_c', y='precipitation_mm', color='town', title='Avg Temperature vs Precipitation')
st.plotly_chart(fig_temp_precip)

# Correlation heatmap
st.write("### Correlation Heatmap")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(filtered_df[['max_temp_c', 'min_temp_c', 'avg_temp_c', 'humidity', 'precipitation_mm', 'wind_kph']].corr(), annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
st.pyplot(fig)
