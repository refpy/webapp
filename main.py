'''
Streamlit App for Pipeline Design
'''
import streamlit as st
import numpy as np
import pandas as pd
import refpy as rp

# Top container
with st.container():
    st.header('Welcome to the Pipeline Design App')
    st.write('Using RefPy, this app calculates the inner and total outer diameters of pipelines based on the outer diameter, wall thickness and coating thickness.')

# Sidebar with a slider for values ranging from 1 to 10
st.sidebar.image("logo.png")
st.sidebar.title("Pipeline Design App")
slider_value = st.sidebar.slider("Number of Cases", min_value=1, max_value=5, value=2)

# Sample data for DataFrame
data = {
    'OD': np.full(slider_value, np.nan),
    'WT': np.full(slider_value, np.nan),
    'ca': np.full(slider_value, np.nan),
    'Material': np.full(slider_value, 1),
    'SMYS': np.full(slider_value, np.nan),
    'SMTS': np.full(slider_value, np.nan),
    'Temperature': np.full(slider_value, np.nan),
    'alpha_u': np.full(slider_value, np.nan),
}
df = pd.DataFrame(data)

# Columns
st.write("### Inputs")
col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
with col1:
    for index, row in df.iterrows():
        df.at[index, 'OD'] = st.number_input(f'OD{index+1}',
                                             value=row['OD'],
                                             format="%.4f")
with col2:
    for index, row in df.iterrows():
        df.at[index, 'WT'] = st.number_input(f'WT{index+1}',
                                             value=row['WT'],
                                             format="%.4f")
with col3:
    for index, row in df.iterrows():
        df.at[index, 'ca'] = st.number_input(f'ca{index+1}',
                                             value=row['ca'],
                                             format="%.4f")
with col4:
    for index, row in df.iterrows():
        df.at[index, 'Material'] = st.number_input(f'Material{index+1}',
                                                   value=row['Material'],
                                                   format="%.4f")
with col5:
    for index, row in df.iterrows():
        df.at[index, 'SMYS'] = st.number_input(f'SMYS{index+1}',
                                               value=row['SMYS'],
                                               format="%.4f")
with col6:
    for index, row in df.iterrows():
        df.at[index, 'SMTS'] = st.number_input(f'SMTS{index+1}',
                                               value=row['SMTS'],
                                               format="%.4f")
with col7:
    for index, row in df.iterrows():
        df.at[index, 'Temperature'] = st.number_input(f'Temperat.{index+1}',
                                                      value=row['Temperature'],
                                                      format="%.4f")
with col8:
    for index, row in df.iterrows():
        df.at[index, 'alpha_u'] = st.number_input(f'alpha_u{index+1}',
                                                  value=row['alpha_u'],
                                                  format="%.4f")

df['Burst Pressure'] = df.apply(
    lambda x: rp.burst_pressure(x['OD'], x['WT'], x['ca'],
                                np.full(1, x['Material']), x['SMYS'], x['SMTS'],
                                np.full(1, x['Temperature']), x['alpha_u'])[0],
    axis = 1)
df['Burst Pressure'] = df['Burst Pressure'] / 1.0E+06

# Outputs
st.write("### Outputs - Summary Table")
st.dataframe(df)

# Create distplot
st.write("### Outputs - Plot")
st.bar_chart(df['Burst Pressure'],
             x_label = 'Case Number', y_label = 'Burst Pressure (MPa)')
