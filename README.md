
# Care Continuity & Provider Workload Analysis  
### Operational Analytics Project Using Patient Encounter Data  
**Author:** Josephine  
**Role:** Healthcare Data Analyst  
**Last Updated:** June 2026  

---

## 📌 Project Overview

This project analyzes **provider workload**, **care continuity**, and **operational efficiency** using a patient encounter dataset.  
The goal is to identify:

- Workload imbalances across providers  
- Fragmented care patterns  
- Misalignment between staffing and patient demand  
- High-utilizer patient groups  
- Operational bottlenecks affecting throughput and patient experience  

This project demonstrates real-world healthcare analytics skills including SQL, Python, data modeling, operational KPIs, and dashboard design.

---

## 🏥 Business Problem

Hospitals struggle with:

- Uneven provider workloads  
- Long wait times during peak hours  
- Poor continuity of care  
- Inefficient scheduling  
- High-utilizer patients driving disproportionate demand  

This project provides a **data-driven framework** to optimize staffing, improve continuity, and enhance operational performance.

---

## 🎯 Objectives

1. **Measure provider workload**  
   - Encounters per provider  
   - Encounter duration  
   - Utilization index  
   - Peak workload hours  

2. **Evaluate continuity of care**  
   - UPC (Usual Provider Continuity)  
   - Number of unique providers per patient  
   - Fragmentation patterns  

3. **Analyze operational flow**  
   - Encounter volume by hour/day  
   - Staffing vs. demand alignment  
   - Wait-time proxies  

4. **Identify high-utilizer patients**  
   - Encounter frequency  
   - Care fragmentation  
   - Provider assignment patterns  

---

## 📂 Repository Structure


---

## 🧠 Key Metrics

### **Provider Workload**
- Encounters per provider  
- Average encounter duration  
- Utilization index  
- Workload distribution (Pareto analysis)  

### **Continuity of Care**
- UPC (Usual Provider Continuity)  
- Unique providers per patient  
- Continuity score distribution  

### **Operational Flow**
- Encounter volume by hour/day  
- Staffing vs. demand mismatch  
- Wait-time proxy metrics  

### **High-Utilizer Identification**
- ≥4 encounters in 90 days  
- Provider consistency  
- Encounter clustering  

---

## 🛠️ Tools & Technologies

- **Python:** pandas, numpy, matplotlib, seaborn  
- **SQL:** Window functions, aggregations, time-based analysis  
- **Power BI / Tableau:** Dashboard design  
- **Jupyter Notebooks:** Reproducible analysis  
- **GitHub:** Version control & documentation  

---

## 📊 Dashboard (Power BI / Tableau)

The dashboard includes:

- Provider workload heatmap  
- Encounter volume by hour/day  
- Continuity of care score distribution  
- High-utilizer patient tracker  
- Staffing vs. demand alignment chart  

Wireframes are included in the `dashboard/` folder.

---

## 📈 Example SQL Queries

### Provider Workload
```sql
SELECT 
    provider_id,
    COUNT(*) AS encounter_count,
    AVG(DATEDIFF(minute, start_time, end_time)) AS avg_encounter_duration
FROM encounters
GROUP BY provider_id;
