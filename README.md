# Customer_Segmentation_Project
Customer Segmentation using clustering techniques for marketing insights

# 🧩 Customer Segmentation Project

Customer Segmentation Using Machine Learning Clustering Algorithms

Project Overview

This project focuses on identifying different groups of customers based on their purchasing behavior, demographics, and income patterns. Customer segmentation helps businesses understand their customers better and create targeted marketing strategies, personalized offers, and improved customer experiences.

The project uses a marketing campaign dataset and applies multiple clustering algorithms to divide customers into meaningful segments. Extensive data cleaning, exploratory data analysis (EDA), feature engineering, and model evaluation were performed to build an effective customer segmentation system.

Problem Statement

Businesses often have thousands of customers with different buying habits and preferences. Treating all customers the same can lead to ineffective marketing campaigns and reduced sales.

The goal of this project is to:

Analyze customer behavior.
Discover hidden customer groups.
Identify high-value and low-value customers.
Help businesses make data-driven marketing decisions.
Dataset Information

The dataset contains customer demographic and purchasing information such as:

Income
Education
Marital Status
Year of Birth
Recency
Product Spending
Web Purchases
Store Purchases
Catalog Purchases
Number of Children and Teenagers at Home

Project Workflow
1. Data Cleaning
Checked dataset structure and data types.
Identified and handled missing values.
Removed duplicate records.
Dropped unnecessary columns such as Customer ID.
Detected and removed outliers using the IQR method.

3. Exploratory Data Analysis (EDA)
Analyzed customer income distribution.
Examined education and marital status patterns.
Created histograms and count plots.
Generated correlation heatmaps.
Visualized relationships between important variables.

5. Feature Engineering

Created new features to improve clustering performance:

Age from Year of Birth.
Total_Spent by combining spending across all product categories.

4. Data Preprocessing
Applied One-Hot Encoding to categorical variables.
Standardized numerical features using StandardScaler.
Prepared the final dataset for clustering.

6. Clustering Models

Implemented and compared multiple clustering algorithms:

K-Means Clustering
Used Elbow Method to determine optimal clusters.
Created customer segments based on purchasing behavior.
Gaussian Mixture Model (GMM)
Generated probabilistic customer clusters.
Captured more flexible cluster shapes.
Agglomerative Clustering
Built hierarchical customer groups.
Produced the best clustering performance.
DBSCAN
Detected dense customer groups.
Identified noise and outlier customers.

6. Model Evaluation

Used Silhouette Score to evaluate clustering quality.

Model	Silhouette Score

* K-Means	0.116
* Gaussian Mixture Model	0.099
* Agglomerative Clustering	0.183
* DBSCAN	Evaluated

Best Performing Model: Agglomerative Clustering

Key Insights
Customers with higher income generally spend more on products.
Customer spending behavior varies significantly across segments.
Agglomerative Clustering provided better separation between customer groups.
Distinct customer segments can be targeted with customized marketing strategies.
Customer demographics and purchasing patterns strongly influence segmentation results.
Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-Learn
Jupyter Notebook
Business Impact

This project can help businesses:

Improve customer targeting.
Increase marketing campaign effectiveness.
Identify high-value customers.
Enhance customer retention strategies.
Optimize promotional offers based on customer behavior.
GitHub Repository Description
Customer Segmentation Using Machine Learning

Developed a machine learning-based customer segmentation system using clustering techniques to group customers according to demographics, purchasing behavior, and spending patterns. Performed data cleaning, exploratory data analysis, feature engineering, outlier treatment, and feature scaling. Implemented K-Means, Gaussian Mixture Model (GMM), Agglomerative Clustering, and DBSCAN algorithms and evaluated their performance using Silhouette Score. The project helps businesses identify customer groups, improve marketing strategies, and make data-driven decisions.

Resume Project Points (ATS Friendly)
Customer Segmentation Project
Developed a customer segmentation model using K-Means, GMM, Agglomerative Clustering, and DBSCAN algorithms.
Performed data cleaning, feature engineering, outlier detection, and exploratory data analysis on marketing campaign data.
Evaluated clustering performance using Silhouette Score and identified Agglomerative Clustering as the best-performing model.
Generated actionable customer insights to support targeted marketing and business decision-making.

## 🛠️ Tech Stack
- Python, Pandas, Numpy, Scikit-learn, Matplotlib, Seaborn

