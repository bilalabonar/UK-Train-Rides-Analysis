<div align="center">
  <h1>🚆 UK Railway Performance & Passenger Behavior Dashboard</h1>
  <p>An end-to-end Data Analysis project analyzing UK train rides, from data cleaning in Python to a fully interactive Star Schema Power BI dashboard.</p>

  ![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
  ![DAX](https://img.shields.io/badge/DAX-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)
</div>

---

## 📌 Introduction
Railway transportation systems generate large volumes of operational and ticketing data that provide valuable insights into passenger demand, revenue patterns, and service performance. Analyzing this data helps transportation authorities better understand travel behavior and improve operational planning.

This project performs an end-to-end data analysis of UK railway ticket sales and journey data to explore ridership trends, revenue patterns, ticket class demand, and service performance using data analysis and interactive dashboarding techniques.

---

## 👥 Team Members & Contributions
* **Bilal Abo Nar** (Team Leader) - *Advanced Data Cleaning, Star Schema Modeling, DAX (50+ Measures), and Full Interactive Power BI Dashboard Design.*
* **Shehab El-Din Mohamed Ali** - *Initial Data Understanding, Basic Data Cleaning, Feature Engineering, and Python EDA (Matplotlib/Seaborn).*
* **Esraa Nagy Nabih**
* **Zeyad Shaaban**
* **Youssef Khalifa**

**Instructor:** Dina Ezzat

### 🌟 Core Project Achievements
Throughout the development process, the team accomplished the following:
- **Data Understanding & Cleaning:** Handled missing values, standardized delay reasons, and formatted datetime columns using Python (Pandas).
- **Data Preprocessing & Feature Engineering:** Extracted critical features such as `Purchase Lead Days`, `Is Peak Hour`, and `Passenger Persona`.
- **Data Modeling:** Designed and built a highly optimized **Star Schema** in Power BI (1 Fact table, 6 Dimension tables) handling active and inactive relationships.
- **DAX & Business Logic:** Developed over 50 advanced DAX measures for KPIs and Time Intelligence.
- **Data Visualization:** Designed the complete 6-page interactive Dark Theme Power BI Dashboard, including custom Page Navigation and Bookmark-driven Filter Panels.

---

## 🛠️ Tech Stack & Workflow
* **Data Cleaning:** Python (Pandas)
* **Data Modeling & Visualization:** Power BI
* **Business Logic:** DAX, Power Query (M Code)

---

## 🖼️ Dashboard Preview
*(Add your screenshots or GIFs here)*

### 1. 🏠 Cover Page (Navigation)
> *An app-like landing page using Power BI buttons and page navigation actions.*
![Cover Page](Cover.png)

### 2. 📊 Executive Overview
> *High-level KPIs, Monthly Revenue Trend, and Top Routes summary.*
![Overview](Overview.png)

### 3. 💰 Executive & Revenue Analysis
> *Deep dive into revenue by ticket class, peak hours, and payment methods.*
![Revenue](Revenue.png)

### 4. 🗺️ Route & Network Analysis
> *Analyzing the most profitable and busiest routes across the UK.*
![Routes](Routes.png)

### 5. ⏱️ Operations & Performance
> *Tracking delays, cancellations, and operational bottlenecks (Weather, Signal Failures).*
![Operations](Operations.png)

### 6. 🎫 Tickets & Pricing
> *Analysis of ticket types (Advance vs. Walk-up), price distributions, and Railcard impact on revenue.*
![Tickets](Tickets.png)

### 7. 👥 Passenger Experience & Behavior
> *A unique behavioral analysis focusing on refund rates, passenger personas (Business Commuters vs. Casual), and booking habits.*
![Passenger Behavior](Passenger_Experience_&_Behavior.png)

---

## 💡 Key Business Insights

1. **Revenue Concentration:** The `London Kings Cross → York` route is the most profitable (£183K), driven by high volume and premium pricing.
2. **Peak Hour Dominance:** Peak hours generate **60.8% of total revenue** despite covering only 6 hours of the day.
3. **Operational Bottlenecks:** **Weather (32.9%)** and **Signal Failures (23.3%)** are the leading causes of train delays.
4. **Refund Impact:** Tracked the exact revenue lost to refunds caused by operational failures, providing a direct financial metric for passenger dissatisfaction.
5. **Passenger Booking Habits:** Advance tickets are planned days ahead, while Anytime/Off-Peak tickets are exclusively "walk-up" (0 lead days), dictating when marketing campaigns should be launched.

---

## 🚀 How to Run the Project
1. Clone the repository.
2. Download the `Final Project.pbix` file.
3. Open it using **Power BI Desktop**.
4. Use the Cover Page to navigate through the 6 analytical pages.
5. Click the **Filter Icon** to open the custom pop-up slicer panel (built with Bookmarks).
