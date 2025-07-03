# **Telco Customer Retention: Churn Prediction and Feedback Insights Using Classification and Topic Modelling**

## How To Use
- Put bertopic_model and best_model on the same directory as ml_model, topic model, and inference notebook

## Project Background
Currently, the telecommunication industry is experiencing an average annual churn of 30% to 35%. Customer churn in the telecom industry is important because when we want to bring or maintain existing customers, it is impacted the acquisition cost and retention costs. The acquisition cost is 5 times the retention cost. It is dangerous if we spend it on the customers that we will leave to the competitors. Nowadays, we can predict customer churn with machine learning, analyse what customer truly wants with Natural Language Processing, and do cluster analysis on clusters that on risk of churn.

## Objectives
The main objectives of this project is Telco customer churn below 22 percent and helping marketing team decide business decision andreduce customer churn so it is below 22%

## Conclusion
Based on our analysis, customers who are still on a month-to-month contract were primarily disappointed by the high prices and the automatic contract renewal with contract different terms without prior notice. Our competitor offers a much better price for their higher-tier packages compared to ours, indicating a need to improve our pricing strategy to enhance customer retention. Our model performs well in predicting churn and extracting topics from customer reviews, so we can improve our customers churn to below 22%.

## Further Recommendations
We can achieve our churn reduction target by improving the quality of our higher-tier packages. It’s essential that our premium package delivers better quality, as customers in this segment expect high performance for the price they pay. If we intend to maintain our current pricing, enhancing the quality of our services is crucial. We must avoid situations where we invest in customer acquisition, only to lose those customers shortly after—especially since acquisition costs can be up to five times higher than retention costs. In addition to improving the premium package, we need to enhance the automatic contract renewal process. This can be done by providing customers with prior notice when contract terms are set to change. Doing so can reduce customer dissatisfaction, regardless of whether they choose to churn. With the rise of social media, unresolved issues like these can seriously damage our brand reputation if not addressed properly.Regarding our model, we can consider using the Qwen 3 embedding model instead of all-MiniLM, as it achieves significantly better on sentence similarity scores. By using Qwen 3 embeddings, we can improve the performance of our system in identifying topic similarity based on user-input sentences or paragraphs.

## URL
- Dataset URL: https://www.kaggle.com/datasets/beatafaron/telco-customer-churn-realistic-customer-feedback
- Deployment URL: https://huggingface.co/spaces/bagusrifky7/telco_customer_retention

## Journal References
- https://www.emerald.com/insight/content/doi/10.1108/07363760710773085/full/html
- https://www.aeaweb.org/conference/2023/program/paper/rNDY23Q6
- https://customergauge.com/blog/average-churn-rate-by-industry#:~:text=Telecom%20churn%20averages%2015%E2%80%9325,price%20sensitivity%2C%20and%20customer%20experience.


