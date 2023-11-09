import streamlit as st
import numpy as np
import pandas as pd
import pickle
import yaml


st.title('Fact check Nutrition')
st.header('Calculate kCal')

with open(r'C:\Users\Sahil\.spyder-py3\nutrition\nutritionLR.pkl', 'rb') as f:
    model = pickle.load(f)



with open(r'C:\Users\Sahil\.spyder-py3\nutrition\nutrition_columns.yml', 'r') as f:
    nutrition_columns = yaml.safe_load(f)

all_columns = nutrition_columns['num_columns'] + nutrition_columns['category']

pro = st.sidebar.number_input('Protein', 0.0, 100.0, 1.0)
carb = st.sidebar.number_input('Carbohydrate', 0.0, 100.0, 1.0)
fat = st.sidebar.number_input('Total fat', 0.0, 100.0, 1.0)
chl = st.sidebar.number_input('Chloresterol', 0.0, 3100.0, 1.0)
fib = st.sidebar.number_input('Fiber', 0.0, 100.0, 1.0)
wat = st.sidebar.number_input('Water', 0.0, 100.0, 1.0)
alc = st.sidebar.number_input('Alcohol', 0.0, 50.0, 1.0)
vitC = st.sidebar.number_input('Vitamin C', 0.0, 2300.0, 1.0)
cat = st.sidebar.selectbox('Enter category',  nutrition_columns['category'])

a = np.zeros(len(all_columns), dtype = float)

for i in range(0, len(all_columns)):
    if all_columns[i] == 'Protein':
        a[i] = pro
    if all_columns[i] == 'Carbohydrate':
        a[i] = carb
    if all_columns[i] == 'Total fat':
        a[i] = fat
    if all_columns[i] == 'Cholesterol':
        a[i] = chl
    if all_columns[i] == 'Fiber':
        a[i] = fib
    if all_columns[i] == 'Water':
        a[i] = wat
    if all_columns[i] == 'Alcohol':
        a[i] = alc
    if all_columns[i] == 'Vitamin C':
        a[i] = vitC
    if all_columns[i] == cat:
        a[i] = 1

if st.button('Calculate calories'):
    b = np.expand_dims(a, axis=0)
    res = model.predict(b)
    st.write(f'The predicted calories is {round(res[0], 2)} kCal')

