### **Version 0.3: AdaptAI**

AdaptAI marks a turning point with **context-aware adaptability**. Accounting for sector-specific risks, policy lengths, revenue, number of employees, and number of LinkedIn followers improves predictions significantly. This version also enhances interpretability for business users through clear adjustments based on real-world factors.

**Key Features**:
- **Sector-specific context** and adaptability.
- Dynamic scaling for **policy length** and **security score**.
- Early-stage user-friendly output and explainability.

---


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rankiteo.git
   cd rankiteo/CyberRisk-RankAI-version0.3

2. Install the required dependencies
   ```bash
   pip install -r requirements.txt

3. **Run the model**:
   To execute the model, use the following command:

   ```bash
   python main.py --sector "Healthcare" --policy_length 6 --security_score 850 --revenue 1000000 --employees 500 --followers 10000

 
*Note*:

The model **requires** the following inputs:
- *`sector`*: The business sector (e.g., Healthcare, Finance, etc.).
- *`policy_length`*: The policy duration in months (6 or 12, or other customized months).
- *`security_score`*: A numerical security score from Rankiteo Cyberscoring Platform (e.g., 350).

The other inputs (*`revenue`*, *`employees`*, *`followers`*) are *optional* but can significantly enhance the prediction accuracy.



### **Sample Outputs**

### **Breach Types**

| **Breach Type** | **Probability**  | **Predicted Severity (number of breached records)**  
| --------------- | ---------------  | ---------------  
| Cyber Attack | 0.2588  |14,092 records
| Human&System Error | 0.2228  | 5,320 records
| Others | 0.1795  | 3,707 records 

---

### **License**
This project is licensed under the MIT License.
