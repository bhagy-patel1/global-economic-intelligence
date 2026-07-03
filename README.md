<div align="center">

# 🌍 Global Economic Intelligence Dashboard

**Clustering and visualizing macroeconomic patterns across countries using World Bank data**

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-K--Means-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?style=flat-square&logo=plotly&logoColor=white)](https://plotly.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

*K-Means Clustering · World Bank Indicators · Interactive Visualization · Macroeconomic Analysis*

</div>

---

## Overview

This project analyzes global economic indicators sourced from the World Bank to identify macroeconomic patterns across countries. Using K-Means clustering, countries are grouped by economic behavior — not geography  and the results are surfaced through an interactive Streamlit dashboard for dynamic exploration.

---

## Table of Contents

- [Features](#features)
- [Dataset](#dataset)
- [Project Workflow](#project-workflow)
- [Clustering Analysis](#clustering-analysis)
- [Key Insights](#key-insights)
- [Tech Stack](#tech-stack)
- [Repository Structure](#repository-structure)
- [Quick Start](#quick-start)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

## Features

| Feature | Description |
|---|---|
| 🗺️ Global GDP Map | Choropleth map of GDP growth by country |
| 📊 Country Indicators | Per-country view of all five economic metrics |
| 🔵 Cluster Visualization | Economic cluster distribution across the globe |
| 🔍 Comparative Analysis | Side-by-side country comparison tool |
| 📈 Interactive Charts | Powered by Plotly for dynamic exploration |

---

## Dataset

Sourced from publicly available **World Bank** economic indicators:

| Indicator | Description |
|---|---|
| GDP Growth | Annual GDP growth rate (%) |
| Inflation | Consumer price inflation rate (%) |
| Unemployment | % of labor force unemployed |
| Exports | Exports of goods & services as % of GDP |
| Population | Total population |

Observations span multiple countries and years, merged into a unified master dataset for analysis.

---

## Project Workflow

```
World Bank Raw Data
        │
        ▼
  01 · Data Collection
        │
        ▼
  02 · Data Cleaning & Preprocessing
  (missing values, normalization, merging)
        │
        ▼
  03 · Clustering Analysis (K-Means, k=3)
        │
        ▼
  04 · Correlation & Insight Generation
        │
        ▼
  05 · Interactive Streamlit Dashboard
```

Each stage maps to a dedicated notebook under `notebooks/`.

---

## Clustering Analysis

K-Means clustering (k=3) groups countries by economic behavior rather than geographic location:

| Cluster | Label | Description |
|---|---|---|
| 0 | 🟢 Stable Economies | Moderate GDP growth, low inflation, consistent macroeconomic indicators |
| 1 | 🔴 High Inflation Economies | Elevated inflation, economic instability, volatile growth patterns |
| 2 | 🟡 High Growth Economies | Emerging markets with strong GDP growth but higher volatility |

> Clustering results are saved to `data/processed/Economic_clusters.csv`.

---

## Key Insights

From the correlation and clustering analysis:

- **GDP growth has weak direct correlation** with inflation and unemployment individually — multi-factor dynamics drive growth.
- **Export-oriented economies** tend to show more stable and consistent growth.
- **Population size alone** is not a reliable predictor of economic performance.
- **High-inflation economies** consistently show unstable GDP patterns, independent of cluster.
- **Emerging markets** (High Growth cluster) carry more economic volatility alongside their higher growth rates.

---

## Tech Stack

| Category | Technologies |
|---|---|
| Language | Python 3.11 |
| Data Processing | Pandas, NumPy |
| Machine Learning | scikit-learn (K-Means) |
| Visualization | Plotly, Matplotlib, Seaborn |
| Dashboard | Streamlit |
| Notebooks | Jupyter |

---

## Repository Structure

```
global-economic-intelligence/
│
├── data/
│   ├── raw/                              ← Original World Bank CSVs
│   └── processed/
│       ├── economic_master_dataset.csv   ← Merged & cleaned dataset
│       ├── Economic_clusters.csv         ← K-Means cluster assignments
│       └── economic_health_scores.csv    ← Derived health score metrics
│
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_clustering_analysis.ipynb
│   ├── 04_economic_insights.ipynb
│   └── 05_economic_insights.ipynb
│
├── dashboard/
│   └── app.py                            ← Streamlit dashboard
│
├── reports/
│   └── economic_analysis_report.md       ← Full analysis write-up
│
├── models/                               ← Saved model artifacts
├── requirements.txt
└── README.md
```

---

## Quick Start

**1. Clone the repository**

```bash
git clone https://github.com/bhagy-patel1/global-economic-intelligence.git
cd global-economic-intelligence
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Run the notebooks** *(optional — processed data already included)*

```bash
jupyter notebook notebooks/
```

**4. Launch the dashboard**

```bash
streamlit run dashboard/app.py
```

Open your browser at `http://localhost:8501`

---

## Future Improvements

- [ ] Add more World Bank indicators (FDI, debt-to-GDP, trade balance)
- [ ] Time-series forecasting with ARIMA or LSTM
- [ ] Real-time data pipeline via World Bank API
- [ ] Docker deployment for reproducibility
- [ ] Cloud hosting on Streamlit Community Cloud

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Author

<div align="center">

**Bhagy Tholiya**

*Computer Science Student · Data Science & Machine Learning*

[![GitHub](https://img.shields.io/badge/GitHub-bhagy--patel1-181717?style=flat-square&logo=github)](https://github.com/bhagy-patel1)

---

⭐ If this project was useful, consider giving it a star!

*Made with ❤️ by Bhagy Tholiya*

</div>
