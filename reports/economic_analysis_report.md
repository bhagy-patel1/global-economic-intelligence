# Global Economic Intelligence – Economic Analysis Report

## 1. Project Overview

This project analyzes global economic indicators to understand patterns in economic growth, stability, and macroeconomic performance across countries.
Using publicly available World Bank datasets, we perform data preprocessing, clustering analysis, and visualization to derive insights about global economies.

The goal of the project is to build a **data-driven economic intelligence platform** that identifies economic clusters and highlights global macroeconomic trends.

---

## 2. Dataset Description

The dataset is derived from World Bank economic indicators and includes the following features:

| Indicator    | Description                                         |
| ------------ | --------------------------------------------------- |
| GDP Growth   | Annual GDP growth rate of a country                 |
| Inflation    | Consumer price inflation rate                       |
| Unemployment | Percentage of the labor force unemployed            |
| Exports      | Export of goods and services as a percentage of GDP |
| Population   | Total population of the country                     |

The dataset includes observations from multiple countries and is used to analyze global economic patterns.

---

## 3. Data Processing

The following preprocessing steps were performed:

1. **Data Collection**

   * Economic indicators were downloaded from the World Bank dataset.

2. **Data Cleaning**

   * Missing values were handled.
   * Inconsistent records were removed.

3. **Feature Preparation**

   * Relevant indicators were selected for analysis.
   * Numerical values were normalized where required.

4. **Dataset Integration**

   * Individual indicator datasets were merged into a unified dataset for analysis.

---

## 4. Clustering Analysis

To identify patterns among countries, **K-Means clustering** was applied to the economic indicators.

Three clusters were identified:

| Cluster Name             | Description                                                                       |
| ------------------------ | --------------------------------------------------------------------------------- |
| Stable Economies         | Countries with moderate GDP growth and relatively stable macroeconomic indicators |
| High Inflation Economies | Economies experiencing high inflation and economic instability                    |
| High Growth Economies    | Emerging economies with higher GDP growth rates                                   |

Clustering helps categorize countries based on economic behavior rather than geographical location.

---

## 5. Correlation Analysis

A correlation matrix was used to analyze relationships between economic indicators.

Key observations:

* GDP growth showed weak direct correlation with inflation and unemployment.
* Export-oriented economies tend to demonstrate relatively stable growth.
* Population size does not necessarily determine economic growth.

This suggests that GDP growth depends on multiple complex macroeconomic factors beyond the indicators used in this analysis.

---

## 6. Key Insights

Major findings from the analysis include:

* Global economies can be broadly categorized into three macroeconomic groups.
* High-growth economies are often emerging markets with higher economic volatility.
* Economies with persistent inflation tend to experience unstable growth patterns.
* Export-driven economies demonstrate more stable economic performance.

---

## 7. Interactive Dashboard

An interactive dashboard was developed to visualize global economic patterns.

Features of the dashboard include:

* Country-level economic indicator display
* Global GDP growth map visualization
* Economic cluster distribution
* Comparative economic analysis between countries

The dashboard allows users to explore macroeconomic data interactively.

---

## 8. Conclusion

This project demonstrates how economic indicators can be analyzed using data science techniques to extract meaningful insights.

By combining **data analysis, clustering algorithms, and visualization tools**, the project provides a structured approach to understanding global economic dynamics.

Future improvements could include:

* Adding more macroeconomic indicators
* Incorporating time-series analysis
* Developing predictive economic models
* Expanding the interactive dashboard

---

## 9. Tools and Technologies

* Python
* Pandas
* Scikit-learn
* Plotly
* Streamlit
* Jupyter Notebook

---

## 10. Author

Bhagy Tholiya
Computer Science Student – Data Science and Machine Learning Enthusiast
