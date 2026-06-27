# 🏥 NFHS-5 Health Analysis using Python

## 📌 Project Overview

This project presents an in-depth analysis of India's **National Family Health Survey (NFHS-5)** state-level health indicators using Python. The objective is to explore regional health trends through data cleaning, exploratory data analysis (EDA), statistical correlation, and interactive geographic visualization.

The project focuses on key public health indicators, including **Obesity, Anaemia, Hypertension, and High Blood Sugar**, to better understand health disparities across Indian states.

---

## 🎯 Objectives

* Load and preprocess the NFHS-5 state-level dataset.
* Clean and transform health indicator data into numeric format.
* Compare obesity levels among men and women.
* Calculate the **Gender Obesity Gap** for each state.
* Analyze the relationship between anaemia and obesity using Pearson correlation.
* Visualize health indicators using informative charts.
* Build an interactive geographic dashboard using Folium.

---

## 📂 Dataset

This project uses the **National Family Health Survey (NFHS-5) 2019–21** state-level dataset along with an India States GeoJSON file for geographic visualization.

---

## 🛠️ Technologies Used

* Python 3
* Pandas
* NumPy
* Matplotlib
* Folium
* Jupyter Notebook

---

## 📊 Project Workflow

### 🔹 Phase 1: Data Preparation

* Imported the NFHS-5 dataset.
* Renamed columns for readability.
* Removed missing records and handled missing values.
* Converted string values to numeric using `pd.to_numeric()`.
* Created a new feature:

  * **Gender_Obesity_Gap = Women Obesity − Men Obesity**

### 🔹 Phase 2: Exploratory Data Analysis (EDA)

* Pearson Correlation Analysis
* Correlation Matrix Heatmap
* Grouped Bar Chart (Hypertension: Men vs Women)
* Scatter Plot (Anaemia vs Obesity)
* State-wise comparison of major health indicators

### 🔹 Phase 3: Geographic Visualization

* Developed an interactive Folium dashboard.
* Displayed obesity prevalence using a Choropleth map.
* Added interactive markers showing:

  * State Name
  * Blood Sugar Rate
  * Anaemia Rate

---

## 📈 Key Visualizations

* 📌 Correlation Matrix Heatmap
* 📌 Hypertension Comparison (Men vs Women)
* 📌 Anaemia vs Obesity Scatter Plot
* 📌 Interactive Folium Health Dashboard

---

## 🚀 How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/shivdev79/NFHS-5-Health-Analysis.git
```

2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Open the Jupyter Notebook:

```bash
jupyter notebook
```

4. Run all notebook cells to reproduce the analysis and generate the visualizations.

---

<img width="1000" height="800" alt="Figure_1anaemia" src="https://github.com/user-attachments/assets/36486c6c-72c1-4675-96c4-30dc3c9dc536" />



<img width="1200" height="600" alt="Figure_1statewise" src="https://github.com/user-attachments/assets/e2d8ee44-2863-48ea-928f-823b577f36d6" />




<img width="1000" height="800" alt="Figure_1 nowrightnow" src="https://github.com/user-attachments/assets/50429a1f-361c-47de-bea7-35409befc23e" />



<img width="1869" height="955" alt="Screenshot 2026-06-26 233615" src="https://github.com/user-attachments/assets/7bc257c2-5b3e-4cb2-8a1f-1722a3e8cb38" />


## 📌 Key Insights

* Identified differences in obesity prevalence between men and women across Indian states.
* Examined the relationship between child anaemia and adult obesity to explore the double burden of malnutrition.
* Compared hypertension prevalence among men and women.
* Built an interactive geographic dashboard to visualize state-level public health indicators.
* Demonstrated the application of Python for public health data analysis and visualization.

---

## 👨‍💻 Author

**Shivanshu Sinha**

**GitHub:** https://github.com/shivdev79

---

## ⭐ Support

If you found this project helpful or interesting, please consider **starring ⭐ the repository**. Your support is greatly appreciated!
