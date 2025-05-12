# Predicting Competitive Bid Amounts for Federal Health IT Contracts

## Overview
This project explores how data analytics can support capture managers in the Civilian Federal Health IT space by predicting the bid amount most likely to win a federal contract. Inspired by real procurement workflows at companies like DLH Corp, this case study applies regression modeling to past award data to guide price-to-win (PTW) strategies.

---

## Business Context

> *"How can we use historical federal procurement data to inform smarter, more competitive bids in high-stakes Health IT contracting?"*

Capture managers often operate under intense time pressure, with limited visibility into competitors’ pricing or government budgets. By leveraging award history from public datasets, we estimate optimal bid ranges and win likelihoods — enabling better bid/no-bid decisions and more strategic proposals.

---

## Project Objectives
- Estimate winning bid amounts for federal Health IT contracts using historical data
- Identify key drivers of award amounts across agencies, NAICS codes, and contract types
- Create interpretable outputs for price-to-win and capture planning
- Build a foundation for analytics-enabled bid strategy

---

## Data Sources
- [USAspending.gov](https://www.usaspending.gov/) — Contract award data from HHS, CMS, NIH, and VA  
- FPDS or SAM.gov (optional): Enrichment from solicitations or contract details  
- Fields used: Award Amount, Number of Bidders, Set-Aside Type, NAICS, PSC, Agency, Award Type, Place of Performance, and more

---

## Data Preparation
- Filtered dataset for awarded Health IT-related contracts from 2018–2024
- Cleaned inconsistent award formats and agency naming conventions
- Engineered features: average bids per NAICS, contract competitiveness score, seasonality, and more

---

## Modeling Approach
- Regression models: XGBoost, Random Forest, Lasso
- Evaluation: RMSE, MAE, cross-validation
- Model interpretation: SHAP feature importance, residual analysis

---

## Key Insights
- The top predictors of award amounts included agency, contract type, NAICS code, and number of bids received
- Health IT bids varied significantly by agency, with CMS and NIH showing tighter pricing thresholds
- Competitive awards (5+ bidders) tended to fall within a narrower bid range than sole source or set-asides

---

## Strategic Takeaways for Capture Managers
- **Price-to-Win Estimation Tool**: Outputs bid amount ranges likely to win under different scenarios
- **Bid/No-Bid Decision Support**: Predictive likelihood of success by opportunity type
- **Agency-Specific Strategy**: Tailor pricing strategy by department (e.g., HHS vs. VA)

---

## Demo (Optional)
_Try the model by inputting a sample opportunity to see a predicted winning bid range._  
_(Planned using Streamlit or Gradio – see below)_

---

## Project Structure

```bash
federal-bid-prediction/
 ┣ 📂data/               # Cleaned datasets & data dictionary
 ┣ 📂notebooks/          # EDA, modeling, and feature engineering
 ┣ 📂outputs/            # Visualizations, model artifacts
 ┣ 📂docs/               # Executive summary, deck, README assets
 ┣ 📄README.md
 ┗ 📄requirements.txt
