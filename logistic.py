def run():

    import streamlit as st
    import pickle
    import numpy as np
    import pandas as pd
    import json


    st.write("<h1 style='text-align: center; color: #ec9a00; font-size: 50px;text-decoration: underline #000000;; font-family:Secular One;'>Coronary heart heart disease prediction</h1>", unsafe_allow_html=True)

    # st.set_page_config(layout="wide") 
    left,right = st.columns(2, gap='large')




    def load_model():
        with open(r"C:\Users\hrith\AppData\Local\Programs\Python\Python311\logisticreg.pickle","rb") as file:
            data = pickle.load(file)
        return data

    data = load_model()
    knn_model = data["model"]
    scaler= data["normalization"]

    # st.radio('Type of Cab you want to Book', options=['Mini', 'Sedan', 'XL', 'Premium', 'Rental'])


    age  = st.slider("13 ) Enter your ***age***", min_value=10, max_value=120, step=1)

    with left:  

        education_map = {'None': 0, 'Primary': 1, 'PUC': 2, 'Bachelors': 3, 'Masters': 4}
        educate_str = st.radio('1 ) Select your ***education***', options=['None', 'Primary', 'PUC', 'Bachelors', 'Masters'],horizontal=True)
        education = education_map[educate_str]

        cigsPerDay = st.slider("3 ) How many ***cigerates*** do you smoke per day", min_value=0, max_value=100, step=1)
        

        sex =  { 'Male':1,'Female':0}
        st.radio('5 ) Select your ***gender***',sex,horizontal=True)


        totChol = st.slider("7 ) What is your ***cholestrol level***",min_value = 107, max_value=696,step =1)

        BPMeds = ['Yes' , 'No']
        bp = st.radio('9 ) Are you taking ***BP medication***?',BPMeds,horizontal=True)


        BMI  = st.slider("11 ) Enter your ***BMI*** ", min_value=16, max_value=60, step=1)

    with right: 
        prevalentStroke = ['Yes','No']
        pS = st.radio('2 ) Have you had a ***stroke*** before?',prevalentStroke,horizontal=True)

        
        heartRate = st.slider("4 ) Enter your ***heart rate***", min_value=45, max_value=143, step=1)

        prevalentHyp = ['Yes','No']
        prev = st.radio('6 ) Do you have ***hypertension***?',prevalentStroke,horizontal=True)

        glucose = st.slider("8 ) Enter your ***glucose levels***", min_value=40, max_value=394, step=1)

        
        diabetes = ['Yes','No']
        dia = st.radio('10 ) Do you have #diabetes#?',diabetes,horizontal=True)

        
        pulse_pressure = st.slider("12 ) Enter your ***pulse pressure***", min_value=10, max_value=200, step=1)

















    newfile = json.load(open(r"C:\Users\hrith\AppData\Local\Programs\Python\Python311\columns10.json","r"))
    hrt = pd.DataFrame(newfile)




    x = np.zeros(len(hrt))
    x[0] = age
    x[3] = cigsPerDay
    x[8] = totChol
    x[9] = BMI
    x[10] = heartRate
    x[11] = glucose
    x[12] = pulse_pressure

    if sex == 'Male':
        x[2] = 1
    else:
        x[2] = 0

    if education == 1:
        x[1] = 1
    elif education == 2:
        x[1] = 2
    elif education == 3:
        x[1] = 3
    elif education == 4:
        x[1] = 4


    if BPMeds == 'No':
        x[4] = 0
    elif BPMeds == 'Yes':
        x[4] = 1


    if prevalentStroke == 'No':
        x[5] = 0
    elif prevalentStroke == 'Yes':
        x[5] = 1
        

    if prevalentHyp == 'No':
        x[6] = 0
    elif prevalentHyp == 'Yes':
        x[6] = 1
        
    if diabetes == 'No':
        x[7] = 0
    elif diabetes == 'Yes':
        x[7] = 1


    x[0]                 = np.log10(x[0]+1)
    x[3]                 = np.log10(x[3]+1)
    x[8]                 = np.log10(x[8]+1)
    x[9]                 = np.log10(x[9]+1)
    x[10]                = np.log10(x[10]+1)
    x[11]                = np.log10(x[11]+1)
    x[12]                = np.log10(x[12]+1)



    x = np.array([x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12]])




    sumx = x.reshape(1, -1)
    # sumex = scaler.transform(sumx)

    # prec = knn_model.predict(sumex)[0]

    # if prec == 1:
    #     st.subheader('Yes')
    # elif prec == 0:
    #     st.subheader('No')



    predict_button = st.button('Predict')

    if predict_button:
        sumex = scaler.transform(sumx)
        prec = knn_model.predict(sumex)[0]
        if prec == 1:
            st.subheader('The probablity of having a stroke is high.')
        elif prec == 0:
            st.subheader('The probablity of having a stroke is low.')

