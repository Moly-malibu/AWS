import streamlit as st
import pandas as pd
from legal_advisor import LegalAdvisor

def main():
    st.title("Legal Services Advisor")
    
    # Upload dataset
    uploaded_file = st.file_uploader("Upload your dataset", type=["csv", "xlsx"])
    
    if uploaded_file is not None:
        if uploaded_file.name.endswith('.csv'):
            data = pd.read_csv(uploaded_file)
        else:
            data = pd.read_excel(uploaded_file)
        
        st.write("Data Overview:")
        st.dataframe(data.head())
        
        # Initialize Legal Advisor
        advisor = LegalAdvisor(data)
        
        # User input for query
        user_query = st.text_input("Ask a legal question:")
        
        if st.button("Get Advice"):
            response = advisor.provide_advice(user_query)
            st.write(response)

if __name__ == "__main__":
    main()