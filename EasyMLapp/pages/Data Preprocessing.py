import streamlit as st
import pandas as pd
import easyml.helper as hp
from settings import BASE_DIR
import time


db = hp.get_db()
# hp.set_png_as_page_bg()
st.title('Data Preprocessing')
st.write(db["dataPreprocessing"])
st.subheader('Getting Started with Data Preprocessing 🚀')
file = st.file_uploader("Please upload a CSV, Excel, JSON, SQL, HDF5, Parquet, Feather, HTML, or Pickle file.")
DATA_PREPROCESSING = False

if st.checkbox("Sample Data"):
    file = str(BASE_DIR) + "\EasyMLapp\data\sample.csv"

if file is not None:
    # Check if the file is a string (e.g., "sample.csv")
    if isinstance(file, str):
        # Read the sample CSV file from the base directory
        df = pd.read_csv(file)
    else:
        # Get the MIME type of the uploaded file
        mime_type = file.type
        print(mime_type)
        df = hp.file_identifier(file,mime_type)

    DATA_PREPROCESSING = True
else:
    st.warning("Please upload a file or select 'Sample Data'.")

if DATA_PREPROCESSING:
    st.subheader('Your DataFrame 🚀')
    st.write("Your DataFrame:")
    st.write(df)
    st.subheader('DataFrame Shape')
    st.code('df.shape')
    st.write(f'{df.shape}')
    st.write(f'This DataFrame Contains {df.shape[0]} Rows & {df.shape[1]} Columns')
    st.subheader("DataFrame Columns")
    st.write("lets Examine the Columns of the DataFrame")
    st.code('df.columns')
    st.write(f'{df.columns}')
    st.write("These are the Columns of the DataFrame")
    st.write("examining the Data types of the Columns")
    st.code("df.dtypes")
    st.write(df.dtypes)
    st.subheader("Descriptive Statistics")
    st.code("df.describe()")
    st.write(df.describe())
    st.subheader("Examining Missing Values")
    st.code("df.isnull().sum()")
    st.write(df.isnull().sum())
    st.subheader("First Five Rows of the DataFrame")
    st.write("Here are the First five rows of the DataFrame")
    st.code("df.head()")
    st.write(df.head())
    st.header("Exploratory Data Analysis - EDA 🚀")
    st.write("Here are Some Graphs for Examining the DataFrame")
    hp.generate_plots(df)

st.markdown("created by Rimmel Asghar with ❤️")