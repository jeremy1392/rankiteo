### **Version 0.4: QuantifyEdge AI**
 
QuantifyEdge AI brings **quantile-based predictions** into the spotlight, allowing for **confidence intervals** and **probabilistic insights**. It introduces **extreme event modeling**, enabling businesses to plan for rare but high-impact breaches. This version bridges the gap between predictions and actionable risk strategies.

**Key Features**:
- Quantile-based severity and confidence interval predictions.
- **Expected shortfall (ES)** metrics for extreme events.
- Advanced risk visualization and reporting.



## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rankiteo.git
   cd rankiteo/CyberRisk-RankAI-version0.4

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


| **Breach Type**       | **Adjusted Probability** | **Predicted Severity** | **95% Prediction Interval** | **99% Quantile Severity** | **Expected Shortfall (95%)** | **Expected Shortfall (99%)** |
|------------------------|--------------------------|-------------------------|-----------------------------|----------------------------|------------------------------|------------------------------|
| Cyber Attack           | 0.2588                  | 14,092 records          | [11,661, 16,878] records    | 17,472 records             | 16,472 records               | 37,557 records               |
| Human or System Error      | 0.2228                  | 5,320 records           | [4,402, 6,372] records      | 6,596 records              | 6,218 records                | 14,178 records               |
| Others                | 0.1788                  | 3,707 records           | [3,067, 4,440] records      | 4,596 records              | 4,333 records                | 9,879 records                |

---

### How to Interpret the Output
1. **Adjusted Probability**: Reflects the likelihood of a breach type occurring, adjusted for security score and other factors.
2. **Predicted Severity**: The expected number of records impacted in the event of a breach.
3. **95% Prediction Interval**: The range of likely severity values with 95% confidence.
4. **99% Quantile Severity**: Estimates of severity at extreme quantiles (99%).
5. **Expected Shortfall (95%)**: Highlights the average impact of the most severe breaches beyond the 95% quantile.
6. **Expected Shortfall (99%)**: Highlights the average impact of the most severe breaches beyond the 99% quantile.

---

### Notes:
- The **Others** category represents breaches that do not fall under "Cyberattack" or "Human or System Error."
- These metrics are crucial for understanding potential risks and planning effective mitigation strategies.

---

The results are saved in a CSV file for further analysis: `quantifyedge_predictions.csv`


### **License**
This project is licensed under the MIT License.
