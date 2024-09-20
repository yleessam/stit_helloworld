import streamlit as st

from datetime import time, datetime

st.header('st.slider')

#예1
st.subheader('Slider')

age=st.slider('당신의 나이는?',0,130,25)
st.write('나는',age,'살입니다.')

#예2

st.subheader('범위 슬라이더')
values = st.slider('값의 범위를 선택하세요',
                   0.0, 100.0, (25.0, 75.0))
st.write('선택한 값 ', values)

#예3

st.subheader('시간 범위 슬라이더')
appoinment = st.slider(
    "약속시간은?",
    value = (time(11,30), time(12,45))
)
st.write('약속한 시간은? ',appoinment)

#예4
st.subheader('날짜와  시간 슬라이더')
start_time = st.slider(
    "시작 시간",
    value=datetime(2024,9,1,9,30),
    format="MM/DD/YY-hh:mm"
)
st.write('시작 시간은..',start_time)