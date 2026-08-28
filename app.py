import pandas as pd
import joblib
import streamlit as st

model=joblib.load('bike_demand_model.pkl')
scaler=joblib.load('bike_demand_scaler.pkl')
expected_cols=joblib.load('bike_expected_cols.pkl')

st.title('Bike Demand Prediction')
st.markdown('Enter the weather and calendar information to predict bike rental demand.')

st.subheader('Date and Time')
date = st.date_input(
    'Date',
    min_value=pd.Timestamp('2011-01-01').date(),
    max_value=pd.Timestamp('2012-12-31').date(),
    value=pd.Timestamp('2012-01-01').date()
)
time=st.time_input('Time')
date_time=pd.Timestamp.combine(date,time)

year=date_time.year
month=date_time.month
day=date_time.day
hour=date_time.hour
day_of_week=date_time.dayofweek

st.subheader('Calender Information')

season=st.selectbox('Season',['Spring','Summer','Fall','Winter'])
season={
    'Spring':1,
    'Summer':2,
    'Fall':3,
    'Winter':4
}[season]

holiday=st.selectbox('Holiday',['Yes','No'])
holiday={
    'Yes':1,
    'No':0
}[holiday]

workingday=st.selectbox('Working Day',['Yes','No'])
workingday={
    'Yes':1,
    'No':0
}[workingday]

st.subheader('Weather Information') 
weather = st.selectbox( 'Weather', [ 'Clear / Partly Cloudy', 'Mist / Cloudy', 'Light Rain / Snow', 'Heavy Rain / Snow' ] ) 
weather = { 'Clear / Partly Cloudy': 1, 'Mist / Cloudy': 2, 'Light Rain / Snow': 3, 'Heavy Rain / Snow': 4 }[weather]

temp = st.number_input( 'Temperature', min_value=0.0, value=20.0 ) 
atemp = st.number_input( 'Feeling Temperature', min_value=0.0, value=20.0 ) 
humidity = st.slider( 'Humidity', min_value=0, max_value=100, value=50 ) 
windspeed = st.number_input( 'Windspeed', min_value=0.0, value=10.0 )

if st.button('Predict Count'):
    input_data=pd.DataFrame({
        'season': [season], 
        'holiday': [holiday], 
        'workingday': [workingday], 
        'weather': [weather], 
        'temp': [temp], 
        'atemp': [atemp], 
        'humidity': [humidity], 
        'windspeed': [windspeed], 
        'year': [year], 
        'month': [month], 
        'day': [day], 
        'hour': [hour], 
        'day_of_week': [day_of_week]
    })

    for col in expected_cols: 
        if col not in input_data.columns: 
            input_data[col] = 0 
    input_data = input_data[expected_cols] 
    prediction = model.predict(input_data)[0] 
    prediction = max(0, prediction) 
    st.success( f'🚲 Predicted Bike Rentals: **{prediction:.0f}**' )