# Predicting Competitive Bid Amounts for Federal Health IT Contracts

A strategic case study using machine learning and federal procurement data to support smarter pricing decisions in the Civilian Health IT contracting space.

> Built by [Casey Ortiz](https://www.linkedin.com/in/kco1) to support roles in **capture strategy**, **Health IT proposal development**, and **data-informed price-to-win (PTW)** analysis.

---

## Project Overview

This project explores how data analytics can support capture managers by predicting the bid amount most likely to win a federal contract. Using over **43,000 historical awards** from HHS, VA, and NIH, I trained a regression model to estimate award values based on NAICS, set-aside, pricing type, and competitive context.

---

## Business Context

> *"How can we use historical federal procurement data to inform smarter, more competitive bids in high-stakes Health IT contracting?"*

Capture teams often operate with limited budget insight or price transparency. By analyzing award history from USAspending.gov, this model offers a **data-driven edge** to inform bid/no-bid decisions, estimate competitive ranges, and tailor pricing strategies by agency and contract type.

---

## Project Goals

- Predict award amounts using past contract data
- Identify key drivers of pricing variation across NAICS and agencies
- Deliver interpretable outputs to support Price-to-Win planning
- Deploy interactive apps to support capture decision-making

---

## Data Sources

- [USAspending.gov](https://www.usaspending.gov/) — Awards from HHS, VA, CMS, and NIH  
- 2018–2025, filtered for NAICS 541511, 541512, 541519  
- Variables: Award Amount, NAICS, Set-Aside, Pricing Type, Agency, Bidders, Dates

---

## Data Preparation

- Cleaned 43,000+ Health IT-related federal awards  
- Engineered features like:
  - Competitive density (bids per contract)
  - NAICS family grouping
  - Contract pricing type logic
  - Seasonal timing (Q1–Q4)

**View the R-based data cleaning and exploration:**  
🔗 [federal_bid_prediction.html](docs/federal_bid_prediction.html)

---

## Modeling Approach

- **Models Used**: XGBoost, Random Forest, Lasso (log-transformed target)  
- **Top Model**: XGBoost with RMSE ≈ 1.71 | R² ≈ 0.35  
- **Model Insights**: SHAP values, PDP++, feature interaction maps  
- **Output**: Predicted award amount or bid range with ±RMSE confidence

---

## Key Insights

- NAICS 541512 + Firm Fixed Price awards were most predictable  
- Competitive contracts (5+ offers) had tighter award distributions  
- Set-aside types (e.g., 8A, SDVOSB) had significant pricing variance  
- VA vs. HHS agencies showed distinct award size patterns

---

## Strategic Takeaways for Capture Teams

- **Price-to-Win Estimation**: Predict award amounts by scenario  
- **Bid/No-Bid Support**: Model outputs help de-risk pursuit decisions  
- **Agency-Specific Strategy**: Adapt pricing by agency or NAICS profile

---

## Streamlit Demo Apps

These tools allow capture teams to simulate opportunity inputs and view pricing predictions.

- 🔗 [Award Amount Estimator](https://ay7jcdeztbpknhyxxbn5h3.streamlit.app)  
- 🔗 [Bid Range Predictor](https://federal-healthit-bid-predictor-mzxes68t2cusms5kmjuyyr.streamlit.app)

> *For model deployment code, see the companion repo:*  
- 🔗 [federal-healthit-bid-predictor](https://github.com/Caseyio/federal-healthit-bid-predictor)

---

## Project Structure

```bash
federal-bid-prediction/
├── data/           # Cleaned data and dictionary
│   ├── health_it_cleaned.csv
│   └── data_dictionary.md
├── docs/           # RMarkdown + rendered HTML
│   ├── federal_bid_prediction.Rmd
│   └── federal_bid_prediction.html
├── notebooks/      # Python notebook
│   └── federal_bid_prediction.ipynb
├── outputs/        # Visuals and plots
│   └── shap_*.png
├── pipelines/      # R + Python scripts
│   ├── eda_pipeline.R
│   └── model_pipeline.py
├── requirements.txt
├── Makefile
├── LICENSE
└── README.md
```

---

## About the Author

👤 **Casey Ortiz**  

📍 Annapolis, MD  
🎓 UVA Darden MBA | Google Data Analytics Certified  
🧠 Capture Strategy | Data Science | Federal Health IT  
📫 kcarlos.ortiz@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/kco1) | [GitHub](https://github.com/caseyio)
