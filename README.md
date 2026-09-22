# Powertrain Reliability Analytics

A data science and engineering analytics project focussing on power-unit telemetry to identify performance trends, detect anomalous behaviour, and develop reliability focussed insights.

> Project status: In development
> Data: Synthetic telemetry for educational / portfolio purposes
---

## Overview

Powertrains generate large volumes of telemetry across testing and operation. The objective of this project is to develop and end-to-end analytics workflow which transforms telemetry into actionable engineering insight.

The project explores:

Data quality and validation
Exploratory data analysis
Statistical analysis
Time-series analysis
Anomaly detection
Reliability modelling
Machine learning
SQL-based analytics
Automated reporting
Power BI visualisation

The project is focussed around a simulated power-unit telemetry environment and does not make use of any Red Bull Racing or Red Bull Powertrains data.
---

## Objectives

The primary objectives are to:

1. Identify performance trends across power-unit test sessions.
2. Detect abnormal sensor behaviour and operating conditions.
3. Investigate relationships between telemetry variables.
4. Develop statistical and machine-learning techniques for fault detection.
5. Explore variables associated with potential reliability degradation.
6. Develop automated data-quality validation routines.
7. Develop an interactive engineering analytics dashboard.
8. Translate analytical results into engineering insights.
---

## Project Architecture

```text
Raw Telemetry
│
▼
Data Validation
│
▼
Data Cleaning
│
▼
Exploratory Data Analysis
│
▼
Statistical & Time-Series Analysis
│
├───────────────┐
▼        ▼
Anomaly Detection  Feature Engineering
│        │
└───────┬───────┘
▼
Reliability Models
│
▼
Model Evaluation
│
▼
Power BI Dashboard
│
▼
Engineering Insights
```
---

## Dataset

The project utilises synthetic power-unit telemetry generated for educational / portfolio purposes.

Planned variables:

| Variable       | Description        |
| --------------------- | -------------------------- |
| `timestamp`      | Telemetry timestamp    |
| `test_id`       | Test session identifier  |
| `rpm`         | Engine rotational speed  |
| `torque`       | Engine torque       |
| `power_output`    | Estimated power output   |
| `engine_temperature` | Engine temperature     |
| `oil_temperature`   | Oil temperature      |
| `oil_pressure`    | Oil pressure        |
| `coolant_temperature` | Coolant temperature    |
| `fuel_flow`      | Fuel-flow measurement   |
| `battery_voltage`   | Battery voltage      |
| `battery_current`   | Battery current      |
| `motor_temperature`  | Electric motor temperature |
| `vibration`      | Vibration measurement   |
| `ambient_temperature` | Ambient temperature    |

The dataset will contain intentional realistic data-quality issues and abnormal operating conditions for the analytical pipeline to tested under non-ideal conditions.
---

## Analytical Methods

### Exploratory Data Analysis

Distribution analysis
Correlation analysis
Outlier detection
Grouped statistics
Operating-condition analysis
Test-session comparisons

### Time-Series Analysis

Rolling statistics
Moving averages
Lag features
Rate-of-change analysis
Trend detection
Autocorrelation
Operating-window analysis

### Anomaly Detection

Planned approaches:

Statistical thresholds
Z-score
IQR-based detection
Isolation Forest
DBSCAN

### Reliability Modelling

Planned approaches:

Failure-event classification
Logistic regression
Random Forest
Gradient boosting
Failure-risk estimation
Feature importance analysis

Model evaluation considers the impact of false positives / negatives rather than overall accuracy.
---

## Data Quality

The pipeline will automatically detect:

Missing values
Duplicate records
Invalid sensor readings
Out-of-range measurements
Timestamp gaps
Sensor dropouts
Unexpected operating conditions
Data-type inconsistencies

The objective is to ensure analytical conclusions are formed from trustworthy data.
---

## Technology Stack

### Programming

Python
SQL

### Python Libraries

Pandas
NumPy
SciPy
Matplotlib
Scikit-learn

### Visualisation

Power BI
Matplotlib

### Development

Jupyter Notebook
Git
GitHub
---

## Repository Structure

```text
powertrain-reliability-analytics/
│
├── data/
│  ├── raw/
│  ├── processed/
│  └── README.md
│
├── notebooks/
│
├── src/
│  ├── data/
│  ├── features/
│  ├── models/
│  └── visualization/
│
├── sql/
│
├── dashboard/
│
├── reports/
│  └── figures/
│
├── tests/
│
├── requirements.txt
├── .gitignore
└── README.md
```
---

## Key Questions

The analysis aims to answer questions such as:

Which telemetry variables are most strongly associated with power output?
What constitutes normal operating behaviour?
Which observations represent statistically unusual behaviour?
Can abnormal conditions be detected automatically?
Which telemetry variables appear before a potential failure event?
Can reliability risk be estimated from sensor behaviour?
How does performance change across test sessions?
Which KPIs are most useful for monitoring power-unit performance and reliability?
---

## Engineering Perspective

The objective is not purely to develop the most accurate machine-learning model.

The analytical workflow is focussed on:

Data quality → statistical validity → model performance → interpretability → engineering relevance → actionable insight

A technically accurate model is only useful if its output can inform a real decision.
---

## Limitations

This portfolio simulation project is not intended to replicate the exact behaviour, architecture, telemetry, or operating limits of a Formula 1 power unit.

The synthetic dataset is intended to demonstrate analytical methodology rather than represent Red Bull Racing or Red Bull Powertrains data.
---

## Future Work

Planned extensions include:

Real-world motorsport datasets where legally available
Advanced time-series models
Survival analysis
Remaining Useful Life estimation
Signal-processing techniques
Automated anomaly alerts
Model monitoring
Expanded Power BI reporting
Real-time telemetry simulation
---

## Author

Rajvardhan Singh Bhandari

BSc (Hons) Data Science & AI
Data Analytics • Machine Learning • Statistical Modelling • Performance Analytics
---

## Disclaimer

This independent portfolio development project is not affiliated with, sponsored by, or endorsed by Red Bull Racing or Red Bull Powertrains.
