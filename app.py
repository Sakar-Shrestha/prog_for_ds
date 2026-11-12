import streamlit as st
import pandas as pd
 
st.title("Hypertension Dataset - Basic Analysis")
 
df = pd.read_csv("hypertension_dataset_5000.csv")
 
st.header("First look")
st.write("Rows and columns:", df.shape)
st.dataframe(df.head())
 
st.header("Summary statistics")
st.dataframe(df.describe())
 
st.header("Missing values")
st.dataframe(df.isnull().sum())
 
number_cols = df.select_dtypes(include="number").columns
category_cols = df.select_dtypes(exclude="number").columns
 
st.header("Distribution of a number column")
num_col = st.selectbox("Pick a number column", number_cols)
counts = df[num_col].value_counts(bins=20).sort_index()
counts.index = counts.index.astype(str) 
st.bar_chart(counts)


# Counts of one category column
if len(category_cols) > 0:
    st.header("Counts of a category column")
    cat_col = st.selectbox("Pick a category column", category_cols)
    st.bar_chart(df[cat_col].value_counts())
 
# Correlation between number columns
st.header("Correlation")
st.dataframe(df[number_cols].corr())
