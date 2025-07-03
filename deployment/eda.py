# import libraries
import streamlit as st
import pandas as pd
from PIL import Image

def run():
    # title section
    st.title('Exploratory Data Analysis')

    # first eda
    st.subheader("A. Correlation Between Numerical Columns to Churn")
    eda_a = Image.open('img/eda_a.png')
    st.image(eda_a)
    with st.expander("Explanation"):
        st.caption("Based on the correlation heatmap above, we can see that customer monthly charges and customer total charges have a weak correlation to " \
        "influence customer churn, and customer tenure has a moderate correlation to customer churn. Tenure and customer total charges have a negative correlation value. " \
        "It means that the longer customers stay to use our products and the higher the total charges, the higher the chance that our customers " \
        "to not leave our company. Customers monthly charges have a positive correlation value. It means that the higher the monthly charges, " \
        "there's a higher chance that customers to leave our company.Tenure has the most influence among the three of them since customers monthly " \
        "charges and customers total charges have a weak correlation to churn. We can focus more on improving tenure to reduce customer churn. " \
        "To improve our customers tenure, we can check the correlation between tenure and all of the columns in the data.")

    # second eda
    st.subheader("B. Correlation Between Numerical Columns to Churn")
    eda_b1 = Image.open('img/eda_b1.png')
    eda_b2 = Image.open('img/eda_b2.png')
    st.image(eda_b1)
    with st.expander("Explanation"):
        st.caption("Based on the correlation value above, we can see that customer monthly charges have a weak correlation to customer tenure, and " \
        "customer total charges have a very strong correlation to customer tenure. Because customer total charges have a strong and positive correlation " \
        "to customer tenure, we can conclude that the higher the total customer charges, the longer customers stay using our services.")
    st.imiage(eda_b2)
    with st.expander("Explanation"):
        st.caption("Based on heatmap correlation above, customer contract type have strong correlation to customer tenure. Customer has a partner "
        "or not and customers payment method type have moderate correlation to customer tenure. We can focus our attention to customer contract type to " \
        "improve our customer tenure, and then we can focus on how customer has a partner or not and payment method type influence to customer tenure.")


    # third eda
    st.subheader("C. Distribution of Tenure Based On Customer Contract Type")
    eda_c1 = Image.open('img/eda_c1.png')
    eda_c2 = Image.open('img/eda_c2.png')
    eda_c3 = Image.ipen('img/eda_c3.png')
    st.image(eda_c1)
    st.image(eda_c2)
    st.image(eda_c3)
    with st.expander("Explanation"):
        st.caption("Based on the tenure distribution for each customer contract type, we can see that customers with a two-year contract type have the most customers in " \
        "the range between 65-72 months. Customers with shorter tenure are mostly low on this histogram. Most customers on customers with a one-year contract " \
        "type are in the range between 52-58 months. This histogram has a quite mixed spread of customers between shorter and longer tenure. " \
        "Tenure distribution of customers with month-to-month contract type has its most customers in the range between 2-6 months. Customers with this " \
        "contract type have a shorter tenure than the other two contract types. The frequency of customers with month-to-month contract type is the " \
        "largest than the other customers.From that analysis, we can conclude that we have the potential to improve customers with one-year contract type. " \
        "We need to improve the number of customers on the longer tenure and decrease customers on shorter tenure on customers with this contract type.")

    # fourth eda
    st.subheader("D. Distribution of Tenure Based on Whether Customers Have Partner or Not")
    eda_d1 = Image.open('img/eda_d1.png')
    eda_d2 = Image.open('img/eda_d2.png')
    st.image(eda_d1)
    st.image(eda_d2)
    with st.expander("Explanation"):
        st.caption("Based on histogram above, tenure on customers that has a partner have their most customers on the range between 65-72 months. " \
        "Most of the customers on this type of customer are long=term loyalty. Customers who don't have a partner have their most customers on the " \
        "tenure range between 1-9 months. Customer with this type mostly are customer with short-term loyalty.From the analysis, " \
        "we can conclude that we need to improve our customer tenure on customer that have a partner, because we can decrease the the number " \
        "of short-term customers that on the range between 1-24 months.")
        
    # fifth eda
    st.subheader("E. Customer Comparison Based On Payment Method")
    eda_e = Image.open('img/eda_e.png')
    st.image(eda_e)
    with st.expander("Explanation"):
        st.caption("Based on the bar chart above, customers prefer to make payment with electronic check. Payment with credit card that " \
        "automatically decrease bank balance is the least preferable for our customers. Both bank transfer and credit card payment system " \
        "automatically decrease bank balance customers account. The reason why both of them is the least preferable option, because not all " \
        "of our customers have credit card, and payment that automatically decrease bank balance made customers unable to plan their household bills.")

    # sixth eda
    st.subheader("F. Distribution of Tenure Based On Whether Customers Have Partner or Not")
    eda_f1 = Image.open('img/eda_f1.png')
    eda_f2 = Image.open('img/eda_f2.png')
    st.image(eda_f1)
    st.image(eda_f2)
    with st.expander("Explanation"):
        st.caption("Customers who make their payments with bank transfers and credit cards have their largest total customers in the tenure range " \
        "between 65-72 months. Most of the customers with both payment methods are customers with long-term loyalty. Customers who make their payment " \
        "with electronic checks and mail checks have their largest total customers in the tenure range between 1-9 months. Most of the customers who make " \
        "their payments with electronic and mailed checks are customers with short-term loyalty.We can use this as an indicator where we can monitor improvement "
        "in customer loyalty based on the payment method they choose. Customers who use automatic payment means our services are priorities to them. We want " \
        "more customers who will make their payments using automatic payment either bank transfer or credit card, because most of the customers using their " \
        "payment have long-term loyalty.")
    
    # seventh eda
    st.subheader("G. Correlation Between Categorical Columns to Churn")
    eda_g = Image.open('img/eda_g.png')
    st.image(eda_g)
    with st.expander("Explanation"):
        st.caption("We use the chi-squared test to measure a correlation between the categorical column and to churn column. From the calculation, " \
        "we found that gender and phone_service p-value are bigger than the critical value (critical value is 0.05). It means that customer gender "
        "and customers using phone service or not are not influenced by customer churn. On the other hand, the contract, dependents, internet_service, " \
        "multiple_lines, online_security, paperless_billing, partner, payment_method, senior_citizen, and streaming_tv columns are correlated to the churn " \
        "column, because their p-value is smaller than the critical value.From this, we can identify problems and read the patterns " \
        "that can make customers leave the company.")

    # ninth eda
    st.subheader("H. Percentage of Churned Customers and Not")
    eda_h = Image.open('img/eda_h.png')
    st.image(eda_h)
    with st.expander("Explanation"):
        st.caption("Based on the pie chart above, 73 percent of our customers are not churned and 27 percent are churned. Average of customer churn "
        "for telecommunication industry on 2025 are 31%, so we are below it. The target that we set to decrease the churn rate to below 22 percent "
        "is realistic and can be achieved.")

    # tenth eda
    st.subheader("I. Comparison of Churned Based on Contract Type")
    eda_i = Image.open('img/eda_i.png')
    st.image(eda_i)
    with st.expander("Explanation"):
        st.caption("Based on the comparison above, we can see that most of our churned customers are month-to-month customers. " \
        "It can happen because customers with month-to-month are trial customers and customers that are still unsure if " \
        "it's worth continuing for the longer term. We need to improve this by converting customers on month-to-month contracts to one-year contracts.")

    # eleventh eda
    st.subheader("J. Comparison of Churned Customers Based on Dependents")
    eda_j = Image.open('img/eda_j.png')
    st.image(eda_j)
    with st.expander("Explanation"):
        st.caption("We can see that mostly churned customers are customer who don't have dependents. Customer who don't have dependents either " \
        "still a single or have partner but doesn't have kids. We analyse this before on tenure distribution based on customer who have partner "
        "or not, and the result is customer who doesn't have a partner tend to be a customer with short-term loyalty. We can consider to " \
        "prioritise more on customers who have a partner and customers who have dependents and a partner.")
    
    # twelfth eda
    st.subheader("K. Comparison of Senior Citizen")
    eda_k = Image.open('img/eda_k.png')
    st.image(eda_k)
    with st.expander("Explanation"):
        st.caption("The chart on the left is churned customer comparison of senior citizens. We can see that we have good customer retention for " \
        "customers who are categorised as senior citizens. The chart on the right is a comparison of senior customers based on whether they prefer " \
        "paperless billing or not, since in general senior citizens have the tendency to paper billing. For our senior customers, we found that they " \
        "prefer paperless billing. We can conclude that our billing system is senior-friendly and we can continue to improve that in the future.")

    # thirteenth eda
    st.subheader("L. Comparison Senior Customer Based on Paperless Billing")
    eda_l = Image.open('img/eda_l.png')
    st.image(eda_l)
    with st.expander("Explanation"):
        st.caption("Based on the bar chart above, customers who don't have a partner are likely to churn that customers who have a partner. " \
        "It is aligned with our analysis of tenure distribution based on customers who have a partner or not. " \
        "Single customers are more likely to have short-term loyalty. It is influenced by single customers who are prone to moving a lot, " \
        "so they have the tendency to change providers a lot too. The reason they move is that they are either not " \
        "interested in marriage or still searching for a partner.")

    # fourteenth eda
    st.subheader("M. Comparison of Churned Customers Based On Have Antivirus or Not")
    eda_m = Image.open('img/eda_m.png')
    st.image(eda_m)
    with st.expander("Explanation"):
        st.caption("Based on the bar chart above, customers who don't have antivirus are likely to churn." \
        " It means that it just happens customers who don't subscribe to our antivirus product are the most churned customers.")

    # fifteenth eda
    st.subheader("N. Distribution of Monthly Charges of Churned Customers")
    eda_n = Image.open('img/eda_n.png')
    st.image(eda_n)
    with st.expander("Explanation"):
        st.caption("Based on the bar chart above, the customers who churn have the largest total customers in the price range between " \
        "65 - 105 dollars per month. If we check the churned customers' feedback, we find that a lot of them find that the quality of " \
        "our internet service products is not worth charging that much. Most of the customers that churn too are customers with month-to-month " \
        "contracts. We can fix the pricing of our internet service products to reduce customer churn.")

    # sixteenth eda
    st.subheader("O. Overall Customers Word Cloud")
    eda_o = Image.open('img/eda_o.png')
    st.image(eda_o)
    with st.expander("Explanation"):
        st.caption("Based on the word cloud of all customers, most of our customers have great experiences and are happy with our services, but the 'don't' " \
        "words have a quite large proportion on the data. After we check the context for this word, it means that the customer experiencing a " \
        "negative experience. They don't like the auto contract renewal that comes with different terms. We need to evaluate on terms that " \
        "we applied on how customer contract renewal works.")

    # seventeenth eda
    st.subheader("P. Churned Customers Word Cloud and Top 10 Words")
    eda_p1 = Image.open('img/eda_p1.png')
    eda_p2 = Image.open('img/eda_p2.png')
    st.image(eda_p1)
    st.image(eda_p2)
    with st.expander("Explanation"):
        st.caption("Based on wordcloud, we can see that the tokens (don't), (monthly charge), and (switch) frequently appear. It means " \
        "that customers often talk about Telco monthly charges and the tendency to switch providers and leave the company. From the top " \
        "10 words that frequently appear on feedback from churned customers, we can see that the words (don't) are the most frequently " \
        "appear on feedback from churned customers. If we look at the feedback that contains the word (don't), " \
        "most of the customers feel not satisfied with auto contract renewal with different terms. The word (overall) is " \
        "also in the top 10. Most of the feedback that contains the word (overall) has a mixed sentiment explaining customer experience " \
        "when using our service. There's a strange word in the top 10, and that word is (better). That word is supposed to have a tendency to " \
        "have positive sentiment, but here that word has a tendency towards switching to a better provider.We can conclude that we need to " \
        "improve our auto contract renewal terms and improve our services.")

    # eighteenth eda
    st.subheader("Q. Churned Customers Word Cloud and Top 10 Words")
    eda_q1 = Image.open('img/eda_q1.png')
    eda_q2 = Image.open('img/eda_q2.png')
    st.image(eda_q1)
    st.image(eda_q2)
    with st.expander("Explanation"):
        st.caption("Based on the word cloud of retained customers, most of the feedback is positive, except the word (don't) " \
        "that frequently appeared. We take a look at the top 10 words that frequently appeared in customer feedback, and we can see that the words " \
        "(don't), (overall), and(suppor) frequently appeared in the feedback. Most of the feedback that contains the word (don't) has the same meaning " \
        "as the word (don't) that appeared on most feedback from churned customers. Most of the feedback that contains the word (overall) " \
        "has mixed sentiment. Customers with positive feedback often praise the quality of internet service and reasonable monthly payments. " \
        "Customers with negative feedback often complain about the speed of the internet services and the lack of support from customer service. " \
        "Most feedback that contains the word (support) from retained customers often complains about the quality of customer service. We can " \
        "conclude that we need to improve the quality of our customer service, internet speed, and terms of contract renewal. Our customer retention " \
        "can be worse if we don't overcome these problems.")


