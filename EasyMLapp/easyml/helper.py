# file that Includes all helper functions for the EasyMlApp
import pandas as pd
import streamlit as st
import json
from settings import BASE_DIR
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def get_db():
    file_path = str(BASE_DIR) + "\EasyMLapp\data\db.json"
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    return data

@st.cache_data
def file_identifier(file,mime_type):
        if mime_type == "text/csv":
            # Read the user-uploaded CSV file
            df = pd.read_csv(file)
        # Check if the file type is Excel
        
        elif mime_type == "application/vnd.ms-excel" or mime_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            if mime_type == "application/vnd.ms-excel":
                df = pd.read_csv(file)
            else: 
                try:
                    # Read the user-uploaded file
                    df = pd.read_excel(file, engine="openpyxl")
                except Exception as e:
                    st.error("Error: Unable to read the file. Please make sure it is a valid CSV or Excel file.")
                    st.stop()
        # Check if the file type is JSON
        elif mime_type == "application/json":
            # Read the user-uploaded JSON file
            df = pd.read_json(file)
        # Check if the file type is SQL
        elif mime_type == "application/sql" or mime_type == "application/x-sql":
            # Assuming the file is in SQL format and can be directly read using the Pandas read_sql function
            df = pd.read_sql(file)
        # Check if the file type is HDF5
        elif mime_type == "application/x-hdf":
            # Assuming the file is in HDF5 format and can be directly read using the Pandas read_hdf function
            df = pd.read_hdf(file)
        # Check if the file type is Parquet
        elif mime_type == "application/parquet":
            # Assuming the file is in Parquet format and can be directly read using the Pandas read_parquet function
            df = pd.read_parquet(file)
        # Check if the file type is Feather
        elif mime_type == "application/x-feather":
            # Assuming the file is in Feather format and can be directly read using the Pandas read_feather function
            df = pd.read_feather(file)
        # Check if the file type is HTML
        elif mime_type == "text/html":
            # Read the tables from the user-uploaded HTML file
            df = pd.read_html(file)
            # Note that read_html returns a list of DataFrames, so you may need to handle it accordingly based on your use case
            if df:
                df = df[0]  # Select the first DataFrame in the list (you can adjust this based on your specific use case)
            else:
                st.warning("No tables found in the HTML file.")
                st.stop()
        # Check if the file type is Pickle
        elif mime_type == "application/pickle" or mime_type == "application/x-pickle":
            # Assuming the file is in Pickle format and can be directly read using the Pandas read_pickle function
            df = pd.read_pickle(file)
        else:
            st.warning("Unsupported file type. Please upload a CSV, Excel, JSON, SQL, HDF5, Parquet, Feather, HTML, or Pickle file.")
            st.stop()
        return df
    
    
@st.cache_data
def generate_plots(dataframe):
    # Iterate through columns and generate appropriate plots
    
    for column in dataframe.columns:
        if dataframe[column].dtype == 'object':
            # For categorical data (object datatype) with relatively few unique categories, generate a count plot
            if len(dataframe[column].unique()) <= 10:
                st.subheader(f"Plots for {column}")
                plt.figure(figsize=(8, 5))
                sns.countplot(x=column, data=dataframe)
                plt.title(f'Count Plot for {column}')
                plt.xticks(rotation=45)
                st.pyplot(plt)  # Use st.pyplot() to display Matplotlib figures in Streamlit
            else:
                # For categorical data with many unique categories, generate a bar plot
                st.subheader(f"Plots for {column}")
                plt.figure(figsize=(12, 5))
                sns.barplot(x=dataframe[column].value_counts().index, y=dataframe[column].value_counts())
                plt.title(f'Bar Plot for {column}')
                plt.xticks(rotation=45)
                st.pyplot(plt)  # Use st.pyplot() to display Matplotlib figures in Streamlit
        elif dataframe[column].dtype == 'datetime64[ns]':
            # For datetime data, generate a line plot with time as the x-axis
            st.subheader(f"Plots for {column}")
            plt.figure(figsize=(12, 5))
            plt.plot(dataframe[column], dataframe.select_dtypes(include='number'))
            plt.title(f'Line Plot: {column}')
            plt.xlabel('Time')
            plt.legend(dataframe.select_dtypes(include='number').columns)
            st.pyplot(plt)  # Use st.pyplot() to display Matplotlib figures in Streamlit
        else:
            # For numerical data, generate a histogram, box plot, and scatter plot
            st.subheader(f"Plots for {column}")
            plt.figure(figsize=(12, 5))
            plt.subplot(1, 3, 1)
            sns.histplot(dataframe[column], kde=True)
            plt.title(f'Histogram for {column}')

            plt.subplot(1, 3, 2)
            sns.boxplot(y=column, data=dataframe)
            plt.title(f'Box Plot for {column}')

            # Scatter plot with other numeric columns
            for numeric_column in dataframe.select_dtypes(include='number').columns:
                if numeric_column != column:
                    plt.subplot(1, 3, 3)
                    sns.scatterplot(x=column, y=numeric_column, data=dataframe)
                    plt.title(f'Scatter Plot: {column} vs {numeric_column}')
                    break  # Show only one scatter plot

            plt.tight_layout()
            st.pyplot(plt)  # Use st.pyplot() to display Matplotlib figures in Streamlit

    # Generate violin plots for numeric columns
    for column in dataframe.select_dtypes(include='number').columns:
        st.subheader(f"Voilin Plot for {column}")
        plt.figure(figsize=(8, 5))
        sns.violinplot(x=dataframe[column], data=dataframe)
        plt.title(f'Violin Plot: {column}')
        st.pyplot(plt)  # Use st.pyplot() to display Matplotlib figures in Streamlit
