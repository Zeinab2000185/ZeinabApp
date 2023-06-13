import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go

df = pd.read_csv('heart stroke data.csv')

# Drop rows with missing values
df = df.dropna()

# Set custom colors
color_female = "#FF69B4"  # Pink
color_male = "#4169E1"    # Blue

# Create a Streamlit app
st.title("Stroke Dataset Dashboard")

# Add overview section
st.header("Overview")
st.write("This dataset contains several predictors that may or not be associated with the likelihood of having a stroke, which are: Gender, Age, Hypertension, Heart Disease, Work Type, Residence Type, Marital Status, Smoking Status, Average Glucose, and BMI.")

# Create tabs
tabs = ["Gender", "Age", "Hypertension", "Heart Disease", "Work Type", "Residence Type", "Marital Status", "Smoking Status", "Average Glucose Level", "BMI"]
selected_tab = st.radio("Select a tab", tabs)

# Bar plot for stroke vs. selected feature
if selected_tab == "Gender":
    fig = px.bar(df, x='gender', color='stroke', barmode='group', color_discrete_sequence=[color_female, color_male])
elif selected_tab == "Age":
    fig = px.box(df, x='stroke', y='age', color='stroke', color_discrete_sequence=[color_female, color_male])
elif selected_tab == "Hypertension":
    fig = px.bar(df, x='hypertension', color='stroke', barmode='group', color_discrete_sequence=[color_female, color_male])
elif selected_tab == "Heart Disease":
    fig = px.bar(df, x='heart_disease', color='stroke', barmode='group', color_discrete_sequence=[color_female, color_male])
elif selected_tab == "Work Type":
    fig = px.bar(df, x='work_type', color='stroke', barmode='group', color_discrete_sequence=[color_female, color_male])
    fig.update_layout(xaxis={'categoryorder':'total descending'})
elif selected_tab == "Residence Type":
    fig = px.bar(df, x='Residence_type', color='stroke', barmode='group', color_discrete_sequence=[color_female, color_male])
elif selected_tab == "Marital Status":
    fig = px.bar(df, x='ever_married', color='stroke', barmode='group', color_discrete_sequence=[color_female, color_male])
elif selected_tab == "Smoking Status":
    fig = px.bar(df, x='smoking_status', color='stroke', barmode='group', color_discrete_sequence=[color_female, color_male])
    fig.update_layout(xaxis={'categoryorder':'total descending'})
elif selected_tab == "Average Glucose Level":
    fig = px.scatter(df, x='avg_glucose_level', y='stroke', color='stroke', color_discrete_sequence=[color_female, color_male])
elif selected_tab == "BMI":
    fig = px.scatter(df, x='bmi', y='stroke', color='stroke', color_discrete_sequence=[color_female, color_male])

# Plot the figure
st.plotly_chart(fig)

# Display the dataset as a table
st.header("Dataset")
st.dataframe(df)

# Save the Streamlit app
st.button("Save Dashboard")
