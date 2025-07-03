import os
os.environ["HOME"] = "/tmp"
import streamlit as st
import pandas as pd
import eda
import prediction
import topics

# Sidebar navigation
page = st.sidebar.selectbox(
    label='Select Page',
    options=['Introduction', 'Exploratory Data Analysis', 'Model Prediction', 'Extract Customer Reviews']
)

if page == 'Introduction':
    # project introduction page
    st.title(':signal_strength: Telco Customer Retention: Churn Prediction and Feedback Insights Using Classification and Topic Modelling')

    st.write("")
    
    # how to use the app
    st.write('**Page Information**')
    st.write('- Exploratory Data Analysis: This page is filled with data exploraton from the datasets')
    st.write('- Model Prediction: This page is use for predict customers churn')
    st.write('- Extract Customer Reviews: This is use for display related topic from customer reviews.')

    
    # project background
    with st.expander('Project Background'):
        st.caption(
           "Currently, the telecommunication industry is experiencing " \
           "an average annual churn of 30% to 35%. Customer churn in the telecom industry is important because when we want to bring or maintain existing customers, " \
           "it is impacted the acquisition cost and retention costs. The acquisition cost is 5 times the retention cost. It is dangerous if we spend it on the customers " \
           "that we will leave to the competitors. Nowadays, we can predict customer churn with machine learning, " \
           "analyse what customer truly wants with Natural Language Processing, "
           "and do cluster analysis on clusters that on risk of churn."
        )

    # project objective
    with st.expander('Objective'):
        st.caption(
            "The main objectives of this project is Telco customer churn below 22 percent and helping marketing team decide business decision and" \
            "reduce customer churn so it is below 22%"
        )

    # Conclusion
    with st.expander('Conclusion'):
        st.caption(
            "Based on our analysis, customers who are still on a month-to-month contract were primarily disappointed by the high prices and " \
            "the automatic contract renewal with contract different terms without prior notice. Our competitor offers a much better price for " \
            "their higher-tier packages compared to ours, indicating a need to improve our pricing strategy to enhance customer retention. Our " \
            "model performs well in predicting churn and extracting topics from customer reviews, so we can improve our customers churn to below 22%."
        )

    # Recommendation
    with st.expander('Recommendation'):
        st.caption(
            "We can achieve our churn reduction target by improving the quality of our higher-tier packages. It’s essential that our premium package " \
            "delivers better quality, as customers in this segment expect high performance for the price they pay. If we intend to maintain our " \
            "current pricing, enhancing the quality of our services is crucial. We must avoid situations where we invest in customer acquisition, " \
            "only to lose those customers shortly after—especially since acquisition costs can be up to five times higher than retention costs. " \
            "In addition to improving the premium package, we need to enhance the automatic contract renewal process. This can be done by " \
            "providing customers with prior notice when contract terms are set to change. Doing so can reduce customer dissatisfaction, regardless " \
            "of whether they choose to churn. With the rise of social media, unresolved issues like these can seriously damage our brand reputation "
            "if not addressed properly.Regarding our model, we can consider using the Qwen 3 embedding model instead of all-MiniLM, as it achieves " \
            "significantly better on sentence similarity scores. By using Qwen 3 embeddings, we can improve the performance of our system in identifying " \
            "topic similarity based on user-input sentences or paragraphs."
        )


elif page == 'Exploratory Data Analysis':
    eda.run()

elif page == 'Model Prediction':
    prediction.run()

elif page == 'Extract Customer Reviews':
    topics.run()