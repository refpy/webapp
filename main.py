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
st.sidebar.title("Number of Pipelines")
slider_value = st.sidebar.slider("Select a value", min_value=1, max_value=5, value=2)

# Sample data for DataFrame
data = {
    'Outer Diameter': np.full(slider_value, np.nan),
    'Wall Thickness': np.full(slider_value, np.nan),
    'Coating Thickness': np.full(slider_value, np.nan)
}
df = pd.DataFrame(data)

# Columns
st.write("### Inputs")
col1, col2, col3 = st.columns(3)
with col1:
    for index, row in df.iterrows():
        df.at[index, 'Outer Diameter'] = st.number_input(f'Outer Diameter for Row{index+1}',
                                                         value=row['Outer Diameter'],
                                                         format="%.4f")
with col2:
    for index, row in df.iterrows():
        df.at[index, 'Wall Thickness'] = st.number_input(f'Wall Thickness for Row{index+1}',
                                                         value=row['Wall Thickness'],
                                                         format="%.4f")
with col3:
    for index, row in df.iterrows():
        df.at[index, 'Coating Thickness'] = st.number_input(f'Coating Thickness for Row{index+1}',
                                                            value=row['Coating Thickness'],
                                                            format="%.4f")

df['Inner Diameter'] = df.apply(
    lambda x: rp.inner_diameter(x['Outer Diameter'], x['Wall Thickness']),
    axis = 1)
df['Total Outer Diameter'] = df.apply(
    lambda x: rp.total_outer_diameter(x['Outer Diameter'], x['Coating Thickness']),
    axis = 1)

# Outputs
st.write("### Outputs")
st.dataframe(df)
