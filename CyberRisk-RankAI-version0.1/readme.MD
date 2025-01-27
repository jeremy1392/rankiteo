### **Version 0.1: StatGuard AI**
**Story**:  
StatGuard AI lays the foundation of risk modeling using traditional **statistical methods**. It leverages **regression models** to predict the likelihood of incidents based on structured historical data. This version demonstrates the power of data-driven decision-making, replacing intuition with numbers.

**Key Features**:
- **GLM** models.
- Early exploration of **probability predictions**.
- Focus on baseline accuracy for breach detection.

---

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

| **Breach Type** | **Probability**  
| --------------- | ---------------  
| Cyber Attack | 0.2588  
| Human&System Error | 0.1352  
| Others | 0.0456  


---

### **License**
This project is licensed under the MIT License.
