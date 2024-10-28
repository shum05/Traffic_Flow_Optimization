# Final Project Report
# Traffic Flow Optimization: Final Report

## 1. Project Overview

### Objective
The objective of this project was to optimize traffic flow using data-driven insights. Our goals included analyzing traffic patterns, identifying peak congestion times, and developing algorithms for traffic signal optimization, real-time route adjustments, and congestion management.

### Data Sources
We collected and processed real-time traffic data that included variables such as:
- **Traffic volume**: Hourly vehicle counts.
- **Day of the week and hour of the day**: Indicators of traffic flow variations.
- **Weather conditions**: Temperature, precipitation, and visibility, as potential influencing factors.
- **Road-specific metrics**: Information on intersections, lane capacity, and traffic signals.

## 2. Methodology

### Data Collection and Preparation
1. **Data Ingestion**: Data was gathered from multiple sources, including municipal traffic data APIs and sensors, and stored in the `data/raw` directory.
2. **Data Cleaning and Processing**: Missing values, inconsistencies, and duplicates were handled. Outliers were checked and removed when necessary. The cleaned data was stored in `data/processed/traffic_data_cleaned.csv`.
3. **Fe
