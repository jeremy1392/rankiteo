### **Version 0.5: TransformRisk AI**
 
TransformRisk AI integrates **transformer-based architectures** for risk modeling. Leveraging the power of **self-attention** and **sequence modeling**, this version excels at identifying patterns in large datasets, including **temporal trends**. It pushes the boundaries of prediction accuracy and handles complex cyber threat scenarios.

**Key Features**:
- Transformer models for **time-series and sequential data**.
- Enhanced feature extraction for **complex risk dependencies**.
- Significant improvements in prediction accuracy and speed.


---
### **How to Get Started**
1. **Clone the repository**:
   ```bash
   git clone https://github.com/jeremy1392/rankiteo.git
   cd rankiteo/CyberRisk-RankAI-version0.5

2. **Install dependencies**:
   ```bash 
   pip install -r requirements.txt
   
  Note: Python 3.9 may be needed to match the compatibility of the package.

3. **Run the model**:
   To execute the model, use the following command:

   ```bash
   python prediction_cost_all.py --sector "Healthcare" --policy_length 6 --security_score 850 --revenue 1000000 --employees 500 --followers 10000

 
*Note*:

The model **requires** the following inputs:
- *`sector`*: The business sector (e.g., Healthcare, Finance, etc.).
- *`policy_length`*: The policy duration in months (6 or 12).
- *`security_score`*: A numerical security score from Rankiteo Cyberscoring Platform (e.g., 750).

The other inputs (*`revenue`*, *`employees`*, *`followers`*) are *optional* but can significantly enhance the prediction accuracy.
 

---

### **Sample Outputs**

### **Key Metrics**

| **Metric** | **Value** |
| ---------- | --------- |
| **Breach Probability** | 0.2361 |
| **Predicted Severity** | 20,132 records |
| **Cost Based on Severity** | $12,452,231.43 |
| **Cost 95% Prediction Interval** | [$50,321, $387,154]|
| **Cost Based on VaR (99%)** | $327,563,234.45 |
| **Cost Based on ES (99%)** | $433,215,321.32|


### **Detailed Breach Types**

| **Breach Type** | **Probability** | **Severity** | **Cost** |
| --------------- | --------------- | ------------ | -------- |
| Cyber Attack | 0.2361 | 20,132 records | $12,452,231.43 |
| Human&System Error | 0.1123 | 15,124 records | $4,011,126.18 |
| Other Cause | 0.0016 | 3,019 records | $1,002,240.00 |


---

### **License**
This project is licensed under the MIT License.
