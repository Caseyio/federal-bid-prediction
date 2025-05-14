# eda_pipeline.R
# This script summarizes key R-based steps from the Health IT bid prediction case study

library(readr)
library(dplyr)
library(janitor)

# Load and clean award data
df <- read_csv("data/health_it_cleaned.csv") %>%
  clean_names()

# Preview structure
glimpse(df)

# Summary stats
summary(df$award_amount)

# Optional: NA check
colSums(is.na(df))
