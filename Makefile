# Makefile for Health IT Bid Prediction

model:
	python pipelines/model_pipeline.py

eda:
	Rscript pipelines/eda_pipeline.R

install:
	pip install -r requirements.txt
