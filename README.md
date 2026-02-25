# Insurance_Risk_Analytics_Dashboard_PBI
# **📊 Insurance Risk & Underwriting Analytics Dashboard**
# **🔎 Project Overview**

This project analyzes an insurance portfolio to assess risk exposure, underwriting effectiveness, and pricing adequacy using Power BI.

The dashboard evaluates policyholder risk distribution, claims behavior, and loss performance across multiple customer segments to identify high-risk drivers and portfolio profitability challenges.

# **🎯 Business Objective**

The goal of this analysis is to:

Identify high-risk policyholders

Evaluate claims frequency and severity

Assess pricing adequacy using Loss Ratio

Analyze risk concentration by Region, Age Band, and Income Band

Provide actionable insights to improve underwriting decisions

# **🏗️ Data Model**

The report is built using a structured star schema model:

Fact Table

Fact_Risk_Premium (Premium, Claims, Risk Score, Policy-level metrics)

Dimension Tables

Dim_Customer (Age, Gender, Income Band, Region)

Dim_Health (BMI, Chronic Condition, Smoker)

Dim_Driving (Driving Experience, Traffic Violations, Accidents)

Key modeling practices:

One-to-many relationships

Single-direction filtering

Calculated columns (Age Band, Risk Group)

Optimized DAX measures

# **📌 Key KPIs**

Total Policies

Total Premium 

Total Claims 

Loss Ratio

High Risk %

Claim Frequency

Claim Severity

High Risk Claim %

# **📄 Dashboard Structure**
### **Page1 Overview**

High-level portfolio performance:

Policy distribution by Risk Category

Loss Ratio by Region

Loss Ratio by Risk Category

Average Risk Score by Age Band

### **page2 Claims & Risk Drivers**

Explains the cause of high loss ratios:

Premium vs Claims by Risk Category

Claim Frequency & Severity

Loss Ratio by Income Band

Age Band Risk Profile

High-Risk Customer Summary

### **page3 Deep Dive**

Policy-level investigation:

Customer Risk Score

Driving Experience Band

Claims Count

Premium vs Claims comparison

Conditional formatting for risk identification

## **📊 Key Insights**

Over 52% of the portfolio falls under High Risk.

High Risk customers contribute ~96% of total claims.

Overall Loss Ratio exceeds 170%, indicating pricing inadequacy.

Certain regions show significantly higher loss exposure.

Lower driving experience and specific age bands correlate with higher risk scores.

## **🛠️ Tools & Technologies**

Power BI Desktop

DAX

Power Query

Star Schema Data Modeling

## **🚀 How to Use**

Download the .pbix file from this repository.

Open in Power BI Desktop.

Use slicers to filter by Region, Age Band, Income Band, or Risk Category.

Navigate across pages (Overview → Claims → Deep Dive) for layered insights.
## **🖼️ Dashboard Preview**
### **Page 1 – Page1 Overview**
<img width="1329" height="737" alt="Overview" src="https://github.com/user-attachments/assets/30c576c6-f409-4e7d-9618-a0ced6dee47b" />


### **Page 2 – Claims & Risk Drivers**
<img width="1323" height="741" alt="Claims " src="https://github.com/user-attachments/assets/f674d176-c39f-4705-86aa-176ae865fc15" />


### **Page 3 – Deep Dive**

<img width="1325" height="739" alt="DeepDive" src="https://github.com/user-attachments/assets/6fe62feb-7073-41a4-b5d9-8f818fc7e8c6" />


### **Data Model**

<img width="1161" height="704" alt="Model_View" src="https://github.com/user-attachments/assets/c9990214-5e74-49ac-9bee-8ebd6d8256e4" />



## **👤 Author**
# **Aravind Teja Bastipadu**
Designed and built using Power BI 
2026 FEB
