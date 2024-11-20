import streamlit as st
import pandas as pd

st.title('🎈 Machine Learning App')
st.info('This is an app built for machine learning')

with st.expander("data"):
  st.write('**raw data**')
  df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv")
  df

  st.write('**X**')
  X = df.drop('sspecies', axis=1)
  X

  st.write('**y**')
  y = df.species
  y
