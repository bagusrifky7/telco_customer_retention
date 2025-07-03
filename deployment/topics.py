import pandas as pd
import streamlit as st
import os
os.environ["NUMBA_CACHE_DIR"] = "/tmp/numba_cache"
os.makedirs("/tmp/numba_cache", exist_ok=True)
import bertopic
import openai
    
def run():

    # import model
    model = bertopic.BERTopic.load("src/bertopic_model")

    st.title("Customer Insight")
    st.write("")
    # variable for input 
    review = st.text_input(label = 'Input customer feedback', value = "")  # input for customer_id column

    # create function for show sentiment and best topics
    def show_best_topic(text):
        # transform process
        topics, probs = model.transform([text])

        # get top topic index
        topic_index = topics[0]

        # get top keywords
        main_topic_words = model.get_topic(topic_index)
        main_keywords = [word for word, _ in main_topic_words[:5]]  # top 5 keywords

        st.write("- Suggested Topic")
        if topic_index == -1:
            st.write("Customers satisfied with the product")
        elif topic_index == 0:
            st.write("Customers satisfied with internet experience.")
        elif topic_index == 1:
            st.write("Customers complaining about internet connectivity, customer support, and buggy payment app.")
        elif topic_index == 2:
            st.write("Customers complaining about added extras with extra charges without warning.")
        elif topic_index == 3:
            st.write("Customers complaining with overly technical customer support email.")
        elif topic_index == 4:
            st.write("Customers complaining about renewed contract with different terms.")
        elif topic_index == 5:
            st.write("Customers complaining about slow respond from customer support.")
        elif topic_index == 6:
            st.write("Customers complaining about buffering video streaming.")
        elif topic_index == 7:
            st.write("Customers satisfied with customer support, but with minimal user-friendly documentation.")
        else:
            st.write("Customers complaining about confusing bills and reconsider to cancelling their subscriptions.")
        st.write(f"Keywords: {', '.join(main_keywords)}\n")

        st.write("")
        
        # find related topic
        st.write("- Related Topics (Keywords):")
        similar_topic_indices, _ = model.find_topics(text, top_n=5)
        for id in similar_topic_indices:
            if id == topic_index:
                continue  # skip the main topic
            related_words = model.get_topic(id)
            related_keywords = [word for word, _ in related_words[:5]]

            if id == -1:
                st.write("Customers satisfied with the product")
            elif id == 0:
                st.write("Customers satisfied with internet experience.")
            elif id == 1:
                st.write("Customers complaining about internet connectivity, customer support, and buggy payment app.")
            elif id == 2:
                st.write("Customers complaining about added extras with extra charges without warning.")
            elif id == 3:
                st.write("Customers complaining with overly technical customer support email.")
            elif id == 4:
                st.write("Customers complaining about renewed contract with different terms.")
            elif id == 5:
                st.write("Customers complaining about slow respond from customer support.")
            elif id == 6:
                st.write("Customers complaining about buffering video streaming.")
            elif id == 7:
                st.write("Customers satisfied with customer support, but with minimal user-friendly documentation.")
            else:
                st.write("Customers complaining about confusing bills and reconsider to cancelling their subscriptions.")
            st.write(f"Keywords: {', '.join(related_keywords)}")

    if st.button(label = 'extract'):
        if review == "":
            st.write('No review been inserted')
        else:
           show_best_topic(review)