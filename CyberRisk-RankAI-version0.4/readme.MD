### **Version 0.1: StatGuard AI**
**Story**:  
StatGuard AI lays the foundation of risk modeling using traditional **statistical methods**. It leverages **regression models** to predict the likelihood of incidents based on structured historical data. This version demonstrates the power of data-driven decision-making, replacing intuition with numbers.

**Key Features**:
- Simple **logistic regression** and **GLM** models.
- Early exploration of **probability predictions**.
- Focus on baseline accuracy for breach detection.

---


### **Sample Outputs**

### **Key Metrics**

| **Metric** | **Value** |
| ---------- | --------- |
| **Adjusted Probability** | 0.2588 |
| **Predicted Severity** | 29,819 records |
| **Cost Based on Severity** | $14,938,126.24 |
| **Cost 95% Prediction Interval** | [$50,112, $400,174]|
| **Cost Based on VaR (99%)** | $337,663,571.68 |
| **Cost Based on ES (99%)** | $423,513,218.21 |


### **Detailed Breach Types**

| **Breach Type** | **Probability** | **Severity** | **Cost** |
| --------------- | --------------- | ------------ | -------- |
| Cyber Attack | 0.2588 | 29,819 records | $14,938,126.24 |
| Human&System Error | 0.1352 | 10,182 records | $5,091,089.00 |
| Physical Cause | 0.0456 | 5,019 records | $2,509,540.00 |


---

### **License**
This project is licensed under the MIT License.
