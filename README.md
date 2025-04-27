A/B Testing - Control vs Test Group Analysis

This project demonstrates a simple A/B testing process using Python.
We check whether there is a statistically significant difference between the purchasing behaviors of two groups: Control Group and Test Group.

📄 Project Content
	•	Data Reading (pandas)
	•	Hypothesis Setting
	•	Normality Test (Shapiro-Wilk Test)
	•	Variance Homogeneity Test (Levene Test)
	•	Independent Two-Sample T-Test (equal variance assumed)
	•	Final Decision and Interpretation

🛠 Tools & Libraries
	•	Python 3
	•	pandas
	•	numpy
	•	matplotlib
	•	scipy.stats

📊 Dataset

The dataset contains:
	•	Impression (Number of Ad Views)
	•	Click (Number of Clicks)
	•	Purchase (Number of Purchases)
	•	Earning (Revenue)

Two groups were analyzed separately:
	•	Control Group (Old Ad Strategy)
	•	Test Group (New Ad Strategy)

🧪 Hypotheses
	•	H0 (Null Hypothesis): The mean Purchase values of the Control and Test groups are equal.
	•	H1 (Alternative Hypothesis): The mean Purchase values of the Control and Test groups are different.

📈 Conclusion
	•	Both groups were normally distributed and had equal variances.
	•	Based on the t-test results, the p-value > 0.05.
	•	Therefore, we fail to reject the null hypothesis.
	•	Result: There is no statistically significant difference between the purchase means of the control and test groups.
