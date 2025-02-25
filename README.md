# Brent Oil Price Analysis & Interactive Dashboard

Welcome to the **Brent Oil Price Analysis** project by Birhan Energies! This repository contains the code, analysis, and tools to explore how major events—like political decisions, conflicts, sanctions, and OPEC policies—impact Brent oil prices. Our mission? To deliver actionable insights for investors, policymakers, and energy companies tackling the ups and downs of the oil market.

## Project Overview

At Birhan Energies, we turn messy data into smart strategies. This project dives into historical Brent oil prices (1987–2022) and uncovers how global events drive price changes. We’ve got statistical models, exploratory analysis, and plans for a slick interactive dashboard to make sense of it all.

### What’s the Goal?
- **Analyze**: Link key events (political, economic, regulatory) to Brent oil price fluctuations.
- **Measure**: Quantify how much these events shake up prices.
- **Guide**: Provide clear insights for investment, policy, and operational decisions.

### Why It Matters
Oil prices are a rollercoaster. Investors need help managing risks, policymakers need data for stability, and energy companies need forecasts to keep operations humming. We’re here to light the way!

---

## What’s Inside?

### 1. Data
- **Dataset**: Historical Brent oil prices (daily, May 20, 1987 – September 30, 2022)
- **Fields**:
  - `Date`: Day-month-year (e.g., 20-May-87)
  - `Price`: USD per barrel
- **Future Additions**: Economic indicators, tech advancements, political events (from sources like World Bank, IMF, IEA).

### 2. Analysis Workflow
We’re breaking this into three tasks:

#### Task 1: Define the Workflow
- Planned the steps: data cleaning, exploratory analysis, and modeling.
- Explored time series models (ARIMA, GARCH) and Bayesian tools (PyMC3).
- Set assumptions and thought about how to share findings with stakeholders.

#### Task 2: Analyze Brent Oil Prices
- Built models to spot trends and event impacts:
  - **Time Series**: ARIMA, GARCH, VAR, Markov-Switching ARIMA
  - **Machine Learning**: LSTM for deeper patterns
- Considered factors like:
  - Economic indicators (GDP, inflation, USD rates)
  - Tech changes (fracking, renewables)
  - Political moves (sanctions, regulations)
- Validated with metrics like RMSE, MAE, and R².

#### Task 3: Build an Interactive Dashboard
- **Backend**: Flask APIs to serve data and results.
- **Frontend**: React interface with interactive charts (planned).
- **Features** (in progress):
  - Show price trends, forecasts, and event correlations.
  - Add filters for dates, events, and metrics.

---

## Folder Structure
Here’s how the project is organized:

```
AI-powered-analysis-for-Brent-oil-prices/
├── app.py              # Main Flask application (backend entry point)
├── notebooks/          # Jupyter notebooks for exploratory analysis
├── README.md          # You’re reading it!
├── requirements.txt    # Python dependencies
├── scripts/            # Additional scripts for data processing or utilities
├── src/                # Core source code
│   ├── brent-oil-analysis.py   # Main analysis script (Task 1 & 2)
│   ├── brent-oil-analysis2.py  # Alternative or extended analysis script
│   └── __init__.py             # Makes src a Python package
├── tests/              # Unit tests (if any)
```

---

## Getting Started

### Prerequisites
- **Python 3.8+**: For analysis and backend.
- **TensorFlow Environment**: Looks like you’re using a `tf_env`—great for ML models!
- **Git**: To clone this repo.

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/AI-powered-analysis-for-Brent-oil-prices.git
   cd AI-powered-analysis-for-Brent-oil-prices
   ```

2. **Set Up the Python Environment**:
   If using your `tf_env`:
   ```bash
   source ~/path-to-tf_env/bin/activate  # Activate your TensorFlow env
   pip install -r requirements.txt
   ```

3. **Run the Analysis**:
   ```bash
   cd src
   python brent-oil-analysis.py
   ```
   Check out `brent-oil-analysis2.py` for alternative approaches!

4. **Start the Flask App** (if ready):
   ```bash
   python app.py
   ```

---

## How to Use It

1. **Explore the Notebooks**: Head to `/notebooks` for EDA and early findings.
2. **Run the Analysis**: Use `/src/brent-oil-analysis.py` to dig into the data—modify it as you see fit!
3. **Check the Backend**: `app.py` is your Flask hub—run it to test API endpoints (if implemented).
4. **Add Your Touch**: Drop new scripts in `/scripts` or tests in `/tests`.

---

## Next Steps
- **Data**: Add external datasets (economic, political) to `src` or `notebooks`.
- **Models**: Expand `brent-oil-analysis.py` with VAR, LSTM, or Bayesian methods.
- **Dashboard**: Build out the React frontend—stay tuned for updates!

---

## Contributing
Got ideas? Fork this repo, make your changes, and submit a pull request. Let’s make this project even better together!

## Contact
Questions? Reach out to the Birhan Energies team (or your GitHub handle: @your-username).

Happy analyzing! 🚀

