import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Stats 21 Participation Project")

file_upload = st.file_uploader("Upload a file")

if file_upload is not None:
    data = pd.read_csv(file_upload)
    st.write(f"Number of rows: {len(data)}")
    st.write(f"Number of columns: {len(data.columns)}")
    st.write(f"Number of numerical variables: {len(data.select_dtypes(include=['int', 'float']).columns)}")
    st.write(f"Number of categorical variables: {len(data.select_dtypes(include=['object']).columns)}")
    st.write(f"Number of boolean variables: {len(data.select_dtypes(include=['bool']).columns)}")

    selected_column = st.selectbox("Choose a column", data.columns)
    st.write(f"Chosen column: {selected_column}")

    if data[selected_column].dtype in ['int64', 'float64']:
        
        st.write("Five-Number Summary:")
        st.write(data[selected_column].describe())
        choose_color = st.color_picker('Pick a Color', "#69b3a2")
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.violinplot(data=data, y=selected_column, ax=ax)
        plt.ylabel(selected_column)
        plt.title(f"Violin Plot of {selected_column}")
        st.pyplot(fig)

    if data[selected_column].dtype == 'object':
        data[selected_column].fillna("None", inplace=True)
        st.write("Proportions of each category level:")
        st.write(data[selected_column].value_counts(normalize=True))
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.countplot(data=data, x=selected_column, ax=ax)
        plt.xlabel(selected_column)
        plt.ylabel("Count")
        plt.title(f"Bar Plot of {selected_column}")
        plt.xticks(rotation=45)
        st.pyplot(fig)
