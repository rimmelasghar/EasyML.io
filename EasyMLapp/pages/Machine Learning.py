import streamlit as st
import numpy as np
from easyml.helper import get_db


db = get_db()

st.title('Machine Learning')
st.write("Machine learning is a subfield of artificial intelligence (AI) that focuses on the development of algorithms and models that allow computers or machines to learn from and make predictions or decisions based on data, without being explicitly programmed to perform specific tasks.")
st.subheader("Let's Starts the cool Stuff,Be Ready! 🚀")
file = st.file_uploader("Please upload a CSV, Excel, JSON, SQL, HDF5, Parquet, Feather, HTML, or Pickle file.")
model_sidebar = st.sidebar.selectbox('Pick type of ML Models', ["Select Type",'Supervised',"Unsupervised"])
placeholder = st.empty()
placeholder2 = st.empty()
model_placeholder = st.empty()

# container insde place holder
main_container = placeholder.container()
second_container = placeholder2.container()
model_container = model_placeholder.container()

if model_sidebar == "Supervised":
    print()
    main_container.title("Supervised Learning")
    main_container.write("Supervised learning is a type of machine learning in which the algorithm is trained on a labeled dataset, meaning the input data is paired with corresponding output labels. The goal of supervised learning is to learn a mapping function from the input variables to the output variables, so that the algorithm can make predictions on new, unseen data.")
    selected_model = main_container.selectbox("Pick one of the Supervised Models",["Select Any One",'Linear Regression', 'Logistic Regression', 'Support Vector Machines', 'Decision Trees', 'Random Forest', 'Gradient Boosting Machines', 'Naive Bayes', 'K-Nearest Neighbors', 'Neural Networks', 'Linear Discriminant Analysis', 'Gradient Boosting Trees']
)
    if selected_model != "Select Any One":
        second_container.title(selected_model)
        second_container.write(db[selected_model])
elif model_sidebar == "Unsupervised":
    main_container.title("Unsupervised Learning")
    main_container.write(db["Unsupervised"])
    selected_model = main_container.selectbox("Pick one of the Supervised Models",["Select Any One","Model1"])
    if selected_model != "Select Any One":
        second_container.title(selected_model)
else:
    main_container.warning("Please Pick the type of ML Models")
    
    
with model_container:
    st.write("this is where the Models will be loaded")