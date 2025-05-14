# Makefile for Health IT Bid Prediction

# Run the Python model pipeline
model:
	python model_pipeline.py

# Run the R EDA script
eda:
	Rscript eda_pipeline.R

# Install Python requirements
install:
	pip install -r requirements.txt
