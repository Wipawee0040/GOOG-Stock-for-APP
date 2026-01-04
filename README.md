# 📈 GOOG Stock Data Pipeline & App

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![API](https://img.shields.io/badge/Data%20Source-Yahoo%20Finance-purple)](https://pypi.org/project/yfinance/)
[![Status](https://img.shields.io/badge/Status-Active-success)]()

## 📝 Overview
This project demonstrates a streamlined **Data Extraction** process by interfacing with a real-time **Financial API**. It fetches, processes, and visualizes historical and current stock data for Google (GOOG/Alphabet Inc.).

While presented as a stock application, the core objective of this project is to showcase foundational **Data Engineering** skills, specifically handling external data sources, performing basic data transformations, and working with time-series data.

## 🚀 Key Features
* **API Integration:** Automated data fetching from Yahoo Finance (`yfinance`) to retrieve real-time market data.
* **Data Processing:** utilization of Pandas for cleaning and structuring raw JSON/Dictionary data into usable DataFrames.
* **Visualization:** Graphical representation of stock price trends and history.
* **User Interface:** Interactive elements to filter data by date ranges.

## 🛠 Tech Stack
* **Core Language:** Python
* **Data Source:** Yahoo Finance API (`yfinance`)
* **Data Manipulation:** Pandas (DataFrame handling)
* **Visualization/GUI:** Streamlit (or Matplotlib/Tkinter depending on your code)

## 📊 Data Flow
A simplified view of how data moves through the application:

```mermaid
graph LR
    A[External API\nYahoo Finance] -->|Fetch Raw Data| B(Data Extraction Script)
    B -->|Transform & Clean| C{Pandas DataFrame}
    C -->|Render| D[Dashboard / UI]
