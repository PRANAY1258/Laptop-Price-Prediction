import streamlit as st
import pickle
import numpy as np
# importing the model
pipe = pickle.load(open('pipe.pkl','rb'))
data = pickle.load(open('data.pkl','rb'))

st.title('Laptop Prediction')

# brand
Company = st.selectbox('Brand',data['company'].unique())
# type of laptop

Type = st.selectbox('type', data['TypeName'].unique())

# Ram of laptop

Ram = st.selectbox('RAM(GB)',data['RAM'].unique())

# weight of laptop

Weight = st.number_input('weight of the laptop')

# TouchScreen

touchscreen = st.selectbox('TouchScreen',['YES','NO'])

# IPS
ips = st.selectbox('IPS',['YES','NO'])

# ppi

# Screen size

screen_size = st.number_input('Screen size')


# Resolution

resolution = st.selectbox('Screen Resolution',['1920x1080','1366x764','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])


# cpu

cpu = st.selectbox('CPU Brand',data['CpuBrand'].unique())

# hard drive

hdd = st.selectbox('HDD(IN GB)', [0,128,256,512,1024,2048])

SSD = st.selectbox('SSD(IN GB)', [0,128,256,512,1024])

gpu = st.selectbox('GPU',data['Gpu_brand'].unique())

# Op_system

os = st.selectbox('OS',data['Op_system'].unique())


if st.button('Predict Price'):
    #query 
    ppi = None 
    if touchscreen == 'YES':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'YES':
        ips = 1
    else:
        ips = 0
    
    x_res = int(resolution.split('x')[0])
    y_res = int(resolution.split('x')[1])
    ppi = [((x_res**2)+(y_res**2))**0.5/screen_size]
    query = np.arrray(['Company',
                       'TypeName',
                       'Ram',
                       'Weight',
                       'TouchScreen',
                       'IPS_Panal',
                       'ppi',
                       'cpu_Brand',
                       'HDD',
                       'SSD',
                       'Gpu_brand',
                       'Op_system'])
    query = query.reshape(1,12)
    st.title('The Predicted price of this Confiquration is '+(int(np.exp(pipe.predict(query)[0]))))