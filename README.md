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

## 🔍 Data Sources
- [USAspending.gov](https://www.usaspending.gov/) — Contract award data from HHS, CMS, NIH, and VA  
- FPDS or SAM.gov (optional): Enrichment from solicitations or contract details  
- Fields used: Award Amount, Number of Bidders, Set-Aside Type, NAICS, PSC, Agency, Award Type, Place of Performance, and more

---

## 🧹 Data Preparation
- Filtered dataset for awarded Health IT-related contracts from 2018–2024
- Cleaned inconsistent award formats and agency naming conventions
