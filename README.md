# Brent Oil Price Analysis

## Overview
This project analyzes how significant political, economic, and regulatory events impact **Brent crude oil prices** over time. Using **time series analysis** and **machine learning models**, we identify trends and correlations to support **investors, policymakers, and energy companies** in decision-making.

## Business Objective
The primary goal is to study how **major events** (e.g., political decisions, conflicts, OPEC policy changes, sanctions) influence Brent oil prices. The insights help in:
- **Investment Strategies**: Helping investors anticipate price movements.
- **Policy Development**: Assisting policymakers in economic stability planning.
- **Operational Planning**: Enabling energy companies to forecast price fluctuations.

## Data Description
The dataset consists of **daily Brent oil prices** from **May 20, 1987, to September 30, 2022**.

### Data Fields:
- **Date**: The date of the recorded oil price (`day-month-year` format).
- **Price**: The price of Brent crude oil in **USD per barrel**.

## Project Tasks
### **Task 1: Defining the Data Analysis Workflow**
- Understand the dataset and how it's generated.
- Identify key assumptions and limitations.
- Select statistical models for time series analysis.
- Determine communication channels for results.

### **Task 2: Analyzing Brent Oil Prices**
- Use **ARIMA, GARCH**, and machine learning models (**LSTM, VAR**).
- Study external factors like GDP, inflation, trade policies, and technology.
- Validate models with historical data and predictive performance metrics.

### **Task 3: Interactive Dashboard Development**
- **Backend**: Flask API to serve analysis results.
- **Frontend**: React dashboard with interactive visualizations.
- **Key Features**: Historical trends, event-driven price changes, and forecast insights.

## Tech Stack
- **Python** (pandas, NumPy, matplotlib, statsmodels, PyMC3)
- **Machine Learning** (ARIMA, GARCH, LSTM, VAR)
- **Flask** (Backend API)
- **React** (Frontend Dashboard)
- **Git & GitHub** (Version Control)

## Installation & Setup
### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/brent-oil-analysis.git
cd brent-oil-analysis
```

### **2. Create a Virtual Environment**
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run the Analysis**
```bash
python analysis.py
```

### **5. Start the Dashboard**
```bash
cd dashboard
npm install
npm start
```

## Contribution Guidelines
1. **Fork the Repository**
2. **Create a Feature Branch** (`git checkout -b feature-branch`)
3. **Commit Changes** (`git commit -m "Added new analysis method"`)
4. **Push to GitHub** (`git push origin feature-branch`)
5. **Open a Pull Request**

