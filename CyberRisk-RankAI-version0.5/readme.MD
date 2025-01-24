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
   git clone https://github.com/rankiteo/riskmind-ai.git
   cd riskmind-ai 

2. **Install dependencies**:
   ```bash 
   pip install -r requirements.txt


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
