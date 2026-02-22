# Saudi Market Performance Dashboard
## Risk vs Return Analysis (2016–2026)

##  Dashboard Preview

![Saudi Market Dashboard](dashboard_screenshots/SMP.PNG)
*Interactive dashboard built in Tableau analyzing risk-return dynamics of major Saudi market assets (2016–2026).*

---

## Executive Summary

This project presents a comprehensive risk–return analysis of selected Saudi market assets over the period 2016–2026. The objective is to evaluate how effectively major Saudi equities compensate investors for the level of risk undertaken, and to determine whether higher volatility consistently translates into superior returns.

By combining return metrics, volatility analysis, drawdown measurement, and cross-asset correlation, the dashboard provides a clear and accessible overview suitable for both technical and non-technical stakeholders.

---

## Project Objective

The primary goal of this analysis is to answer four core investment questions:

- Which asset delivered the strongest risk-adjusted performance?
- How volatile are leading Saudi blue-chip stocks over time?
- To what extent do these assets move together?
- What level of downside risk (maximum drawdown) did investors face?

Rather than focusing solely on raw returns, this project emphasizes risk-adjusted evaluation, which is critical in portfolio construction and capital allocation decisions.

---

## Data Source

Historical market data was retrieved using the Yahoo Finance API via the `yfinance` Python library.

The following instruments were analyzed:

- **2222.SR** — Saudi Aramco  
- **1180.SR** — Al Rajhi Bank  
- **2010.SR** — SABIC  
- **KSA** — iShares MSCI Saudi ETF  

The dataset includes adjusted daily closing prices beginning in 2015 to ensure sufficient lookback for rolling calculations and trend analysis.

---

## Methodology

The data preparation process involved downloading adjusted historical price data, removing missing values, and ensuring chronological consistency. Daily returns were calculated, followed by cumulative returns to measure long-term growth. Annualized return and volatility were computed using 252 trading days. Risk metrics such as maximum drawdown and Sharpe ratio were then derived. Finally, a correlation matrix was constructed to evaluate diversification potential across assets.

---

## Dashboard Design Philosophy

The dashboard was designed with clarity and executive communication in mind.

Key components include:

- **KPI Summary Cards** — Immediate snapshot of return, volatility, Sharpe ratio, and maximum drawdown.
- **Cumulative Return Chart** — Visual comparison of long-term capital growth.
- **Risk vs Return Scatter Plot** — Portfolio positioning framework.
- **Correlation Heatmap** — Diversification insight across assets.
- **Price with Moving Averages (20, 50, 200 days)** — Trend identification.
- **30-Day Rolling Volatility** — Detection of risk regime shifts.

Each visualization serves a distinct analytical purpose while remaining intuitive for decision-makers.

---

## Key Insights 

Over the past decade, the assets showed clear differences in how they balanced risk and return.

Al Rajhi Bank delivered the most consistent risk-adjusted performance overall. Although it experienced normal market fluctuations, it rewarded investors more efficiently relative to the level of volatility taken on. From a portfolio standpoint, it stands out as a strong core holding.

SABIC, in contrast, experienced higher volatility without delivering proportionally stronger long-term returns. This suggests that additional risk did not consistently translate into better performance during the period analyzed.

The 2020 market shock demonstrated how quickly volatility can increase and how significant drawdowns can become during periods of global uncertainty. It serves as a reminder that downside protection matters as much as return generation.

Correlations between the selected assets were moderate. While diversification within the Saudi market provides some risk reduction, the overall benefit remains limited due to shared macroeconomic exposure.

### Recommendations

Long-term investors may benefit from prioritizing assets with stronger risk-adjusted performance rather than focusing solely on absolute returns.

Diversification should remain part of the strategy, but monitoring volatility trends and drawdown risk is equally important, particularly during unstable market conditions.

In the end, sustainable portfolio growth depends not only on returns, but on consistent and disciplined risk management.
---

## Live Dashboard

🔗 https://public.tableau.com/views/SaudiMarketPerformance/Dashboard?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

The dashboard is interactive and allows users to explore performance metrics dynamically.

---

## Repository Structure

```
├── data_preparation.py
├── clean_stock_data.csv
├── correlation_matrix.csv
├── risk_summary.csv
├── README.md
```

---

## Assumptions & Limitations

- The risk-free rate is assumed to be 0% for Sharpe ratio calculations.
- The analysis is based solely on historical data.
- Adjusted prices account for corporate actions, but external macroeconomic factors are not explicitly modeled.
- Past performance does not guarantee future results.

---

## Tools & Technologies

- Python (Pandas, NumPy)
- yfinance API
- Data visualization platform (Tableau)
- GitHub for version control and project documentation

---

## Conclusion

This project demonstrates how structured financial analysis can support clearer investment decisions through practical and intuitive visual insights. By combining statistical rigor with thoughtful dashboard design, the analysis transforms raw market data into meaningful, decision-oriented intelligence.
