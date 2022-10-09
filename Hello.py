import streamlit as st
import pandas as pd

st.title("Railway timing and filtering system:")
st.subheader("Welcome to the portal")

source = st.text_input("Enter current station:")
dest = st.text_input("Enter station where you want to go:")

df = pd.read_csv("train_data.csv")
df1 = df
df1['Station Name'] = df1['Station Name'].str.rstrip()

df2 = df1[df1['Station Name'] == source]
df3 = df1[df1['Station Name'] == dest]['Arrival time']

df_ans = pd.DataFrame(columns=['Train number', 'Train name', 'Arrival time at current station', 'Departure time from current station', 'Arrival time at destination'])

if st.button('Find trains'):
    df_ans['Train number'] = df2['Train No.']
    df_ans['Train name'] = df2['train Name']
    df_ans['Arrival time at current station'] = df2['Arrival time']
    df_ans['Departure time from current station'] = df2['Departure time']
    df_ans['Arrival time at destination'] = df3

if len(df2) == 0 or len(df3) == 0:
    df_ans = pd.DataFrame()

st.dataframe(df_ans)
