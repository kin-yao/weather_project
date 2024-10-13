<h1 align = center>Weather Data Collection and Analysis for Major Towns in Kenya</h1>
Welcome to the **Weather Data Collection and Analysis for Major Towns in Kenya** project! This repository demonstrates the process of collecting, storing, and analyzing weather data for five major towns in Kenya: **Nairobi, Mombasa, Kisumu, Nakuru, and Eldoret**. The goal is to provide valuable insights into the weather patterns of these towns over a one-year period using API data, MySQL for storage, and various Python-based tools for data analysis and visualization.

## Project Overview

The project includes:

- Collecting historical weather data from an API
- Converting the JSON data into CSV format
- Storing the data in a MySQL database
- Performing exploratory data analysis (EDA) on the weather data
- Visualizing weather patterns, trends, and relationships between variables
- Creating geospatial visualizations using `Folium`
- Building an interactive dashboard with `Streamlit`

## Table of Contents

1. [Technologies Used](#technologies-used)
2. [Data Collection](#data-collection)
3. [Data Storage](#data-storage)
4. [Data Analysis](#data-analysis)
5. [Geospatial Visualization](#geospatial-visualization)
6. [Streamlit Dashboard](#streamlit-dashboard)
7. [How to Run the Project](#how-to-run-the-project)
8. [Future Enhancements](#future-enhancements)

## Technologies Used

- **Python** for data processing, analysis, and visualization
- **MySQL** for storing weather data
- **Streamlit** for building the interactive dashboard
- **Folium** and **Plotly** for geospatial and interactive visualizations
- **Weather API** for historical weather data
- **SQLAlchemy** for database interaction

## Data Collection

Weather data was collected using the [Weather API](https://www.weatherapi.com/) for five towns in Kenya (Nairobi, Mombasa, Kisumu, Nakuru, and Eldoret) between **January 2023** and **January 2024**.

## Data Storage

The weather data collected from the API is transformed and saved into a **MySQL** database for structured storage and easy retrieval. The data is stored in a table that contains key weather attributes such as temperature, humidity, wind speed, and more.

### MySQL Database Schema

The database contains a table named `weather`, which stores the following columns:

- **id**: Unique identifier for each record
- **town**: The name of the town (e.g., Nairobi, Mombasa)
- **date**: The date of the weather record
- **max_temp_c**: Maximum temperature (in °C)
- **min_temp_c**: Minimum temperature (in °C)
- **avg_temp_c**: Average temperature (in °C)
- **humidity**: Average humidity percentage
- **precipitation_mm**: Precipitation level (in mm)
- **wind_kph**: Wind speed (in kilometers per hour)
- **condition_text**: A textual description of the weather condition (e.g., "Clear", "Rainy")

### SQL Example

```sql
CREATE DATABASE weather_data_db;
USE weather_data_db;

CREATE TABLE weather (
    id INT AUTO_INCREMENT PRIMARY KEY,
    town VARCHAR(100),
    date DATE,
    max_temp_c FLOAT,
    min_temp_c FLOAT,
    avg_temp_c FLOAT,
    humidity FLOAT,
    precipitation_mm FLOAT,
    wind_kph FLOAT,
    condition_text VARCHAR(255)
);
```

## Data Analysis

The data analysis phase aims to uncover insights and trends from the weather data collected across various towns in Kenya. This process involved several steps: data cleaning, exploratory data analysis (EDA), and visualization of weather attributes such as temperature, humidity, precipitation, and wind speed.

### 1. Data Cleaning

Before performing any analysis, the dataset underwent several cleaning steps:

- **Handling missing values**: Any missing data was either filled using imputation methods (such as forward fill for time-series data) or removed if deemed irrelevant.
- **Date formatting**: The `date` column was converted into a `datetime` format to facilitate proper time-series analysis.
- **Data type conversions**: Numerical fields like temperature, humidity, and wind speed were cast to appropriate data types (e.g., `float`) to ensure smooth analysis.

### 2. Exploratory Data Analysis (EDA)

EDA was performed to better understand the structure of the weather data and the relationships between different variables.

#### 2.1 Temperature Trends

The first step in the analysis was to examine temperature patterns across different towns. By plotting **maximum**, **minimum**, and **average temperatures** over time, we identified significant seasonal trends and variations between towns.

```python
import matplotlib.pyplot as plt

# Plot maximum temperature trends for each town
plt.figure(figsize=(10,6))
for town in df['town'].unique():
    town_data = df[df['town'] == town]
    plt.plot(town_data['date'], town_data['max_temp_c'], label=town)

plt.title('Maximum Temperature Trends Across Towns')
plt.xlabel('Date')
plt.ylabel('Maximum Temperature (°C)')
plt.legend()
plt.grid(True)
plt.show()
```

## Streamlit Dashboard

The project includes an interactive **Streamlit Dashboard** to provide users with an intuitive interface to explore the weather data for the five major towns in Kenya. The dashboard was designed to present data insights and visualizations in an accessible way, allowing users to interact with the data and customize their views based on their preferences.

### Key Features of the Dashboard


![Interactive Dashboard](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7ob8hmdo3pc8ktbpuej9.png)

1. **Interactive Visualizations**:
   The dashboard features interactive charts and graphs, allowing users to dynamically explore weather trends across different towns. Users can select the towns of interest and view data such as temperature, humidity, wind speed, and precipitation over time. These interactive elements help users visualize how weather parameters change throughout the year.

2. **Town Comparison**:
   Users can compare weather conditions across the five major towns (Nairobi, Mombasa, Kisumu, Nakuru, and Eldoret). The dashboard enables side-by-side comparisons of average temperatures, humidity levels, and wind speeds, providing insights into how different regions experience varied climatic conditions.

3. **Date Range Selection**:
   The dashboard includes a feature to filter the data based on a specific date range. Users can select a start and end date, and the visualizations will update accordingly to show the weather trends during the selected period. This allows users to focus on specific timeframes, such as seasonal changes or yearly trends.

![Data Filters](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/hg514uxg79x8d8qe2ysu.png)

4. **User-Friendly Interface**:
   The dashboard was designed with ease of use in mind, ensuring that both technical and non-technical users can navigate it without difficulty. Clear labels, intuitive controls, and informative tooltips help guide users through the process of selecting towns, filtering data, and interacting with the visualizations.

5. **Downloadable Reports**:
   The dashboard includes an option for users to download the analyzed weather data in CSV format. This feature is useful for those who wish to perform further analysis on their own or store the data for offline use.

![Downloadable reports](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qvl021ntm0oo0fmrxsbr.png)

### Insights and Applications

The interactive dashboard provides valuable insights into Kenya’s weather patterns, allowing users to:

- **Track seasonal trends**: Understand how temperature, humidity, and precipitation vary throughout the year and across different regions.
- **Compare climatic conditions**: Compare the weather conditions of multiple towns to inform decision-making, such as agricultural planning or infrastructure development.
- **Monitor real-time weather**: Stay up-to-date with the latest weather conditions, especially during periods of extreme weather or changing seasons.(**I consider this as a Future Enhancements**)

The Streamlit dashboard serves as a practical tool for individuals and organizations seeking to make data-driven decisions based on weather patterns. By offering real-time data, customizable views, and easy-to-understand visualizations, the dashboard makes weather analysis accessible and actionable for a wide range of users.

---

## How to Run This Project

To run the **Weather Data Collection and Analysis for Major Towns in Kenya** project, follow these steps:

### Prerequisites

Ensure that you have the following installed on your machine:
- **Python 3.8+**
- **MySQL Server** (for storing the weather data)
- **Git** (to clone the repository)
- **Virtual Environment** (optional but recommended)

### Step 1: Clone the Repository

First, clone the project repository from GitHub using the following command:

```bash
git clone https://github.com/your-username/weather-data-kenya.git

```
