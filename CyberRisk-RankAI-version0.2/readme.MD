### **Version 0.2: RiskSphere AI**

RiskSphere AI introduces more **dynamic relationships** by incorporating **machine learning techniques** such as **Random Forests**. This version provides better accuracy and starts quantifying **severity** alongside probabilities, enabling actionable insights for businesses.

**Key Features**:
- **Random Forests** for non-linear relationships.
- First integration of **severity prediction models**.
- Simple decision-making rules for policy adjustments.



## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rankiteo.git
   cd rankiteo/CyberRisk-RankAI-version0.1

2. Install the required dependencies
   ```bash
   pip install -r requirements.txt

3. Run the script using the command line with the following arguments:
   ```bash
   python main.py --sector <sector> --policy_length <policy_length> --security_score <security_score> 



### **Sample Outputs**

### **Breach Types**

| **Breach Type** | **Probability**  | **Predicted Severity (number of breached records)**  
| --------------- | ---------------  | ---------------  
| Cyber Attack | 0.2588  |14,092 records
| Human&System Error | 0.1352  | 5,320 records
| Others | 0.0456  | 3,707 records 


---

### **License**
This project is licensed under the MIT License.
