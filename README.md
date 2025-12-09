# Olist E-commerce Analytics — Power BI Dashboard  
### Created by **Rahim Rzayev**

This project provides a complete end-to-end Business Data Analytics solution using the **Olist Brazilian E-commerce Dataset**.  
The goal is to analyze sales performance, customer behavior, product categories, and forecast future revenue using Python and Power BI.

---

## 📌 Key Features
### 🔹 1. Executive Overview Dashboard
A high-level summary showing:
- Total Revenue  
- Average Order Value  
- Total Sales  
- Total Quantity  
- Order Count  
- Customer Count  
- Monthly Revenue Trend  
- Top Product Categories  

### 🔹 2. Category & Revenue Insights
This section explores:
- Yearly revenue comparison  
- Top 10 revenue-generating categories  
- Monthly trend for top categories  
- Seasonality heatmap to observe demand patterns  

### 🔹 3. Customer Segmentation (RFM Analysis)
Performed RFM segmentation using:
- Recency  
- Frequency  
- Monetary Value  

Key customer groups identified:
- Potential Loyalists  
- Lost Customers  

Custom visuals include:
- RFM donut chart  
- Average Monetary per segment  
- Average Recency per segment  
- Customer-level RFM table  

### 🔹 4. Revenue Forecast (Python — SARIMAX Model)
A 6-month revenue forecast was generated using Python:
- SARIMAX time-series model  
- Forecast line with confidence intervals  
- KPIs including YoY Growth % and MAPE  

The forecast is imported into Power BI and displayed through custom visuals.

---

## 📸 Dashboard Screenshots

### 1. Executive Overview  
![Executive Overview](screenshots/Executive%20Overview%20dashboard.png)

### 2. Category & Revenue Insights  
![Category & Revenue Insights](screenshots/Category%20%26%20Revenue%20Insights%20dashboard.png)

### 3. Customer Segmentation (RFM)  
![Customer Segmentation (RFM)](screenshots/Customer%20Segmentation%20(RFM)%20dashboard.png)

### 4. Revenue Forecast (Python)  
![Revenue Forecast](screenshots/Revenue%20Forecast%20(Python)%20dashboard.png)

### 5. Data Model (Star Schema)  
![Data Model](screenshots/Data%20Model%20view.png)

---

## 📁 Project Structure

📦 Olist-Ecommerce-Analytics-PowerBI
│
├── 📊 Olist_Project.pbix → Power BI dashboard
├── 📄 Business Data Analytics Project Report.pdf
├── 📘 README.md → Project documentation

---

## 🧠 Tools & Technologies
- **Power BI Desktop**
- **Python (Pandas, Statsmodels, Matplotlib)**
- **DAX Measures**
- **Data Modeling (Star Schema)**
- **Time-Series Forecasting (SARIMAX)**

---

## 🔍 Dataset
The dataset originates from **Olist Brazilian E-commerce public dataset** and contains:
- Orders & items  
- Customers  
- Payments  
- Products & categories  
- Reviews  
- Geolocation  

More than 110k orders over multiple years.

---

## 🎯 Core Business Questions Solved
- How did total revenue perform year-over-year?  
- Which product categories generate the highest revenue?  
- What customer segments exist and how valuable are they?  
- What is the expected revenue for the next 6 months?  
- Which months and categories show strong seasonality?  

---

## 📈 Forecasting Model (Python SARIMAX)
The forecasting script generates:
- 6-month prediction  
- Upper/lower confidence intervals  
- MAPE accuracy metric  

Output is merged into Power BI for visualization.

---

## 🛠 How to Use the Dashboard
1. Download the `.pbix` file  
2. Open it in Power BI Desktop  
3. Interact with filters for year, category, and RFM segment  
4. Explore insights across all dashboards  

---

## 👨‍💻 Author
**Rahim Rzayev**  
Business Data Analyst | Power BI | Python |

---
