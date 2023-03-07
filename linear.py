def run():

    import streamlit as st
    import pickle
    import numpy as np
    from sklearn.preprocessing import LabelEncoder
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.linear_model import LinearRegression
    import requests
    import io


    # def load_model():

        # with open(r"C:\Users\hrith\AppData\Local\Programs\Python\Python311\carlinreg.pickle","rb") as file:
        #     data = pickle.load(file)
        # return data

    response = requests.get('https://raw.githubusercontent.com/Hrithik-K-S/portfolio/main/carlinreg.pickle')
    #https://github.com/Hrithik-K-S/portfolio/blob/main/carlinreg.pickle
    file = io.BytesIO(response.content)
    data = pickle.load(file)


   # data = load_model()

    lr = data["model"]
    scalar= data["normalization"]
    le_car = data["company"]
    le_eng = data["enginee"]
    le_trans = data["transmission"]


    #"C:\Users\hrith\Desktop\stearmlit.py"

        # build the main app
    st.write("<h1 style='text-align: center; color: #ffffff; background-color: #000000; font-size: 70px; font-family: Tilt Warp;'>Feel new pre owns</h1>", unsafe_allow_html=True)

    st.title("Pre Owned Auto Price Predictor.")

    st.write("""### Car description""")

    comp_name = (
        "Abarth",
        "Alfa-Romero",
        "Audi",
        "BMW",
        "Bentley",
        "Chevrolet",
        "Chrysler",
        "Citroen",
        "DS",
        "Dacia",
        "Fiat",
        "Ford",
        "Honda",
        "Hyundai",
        "Infiniti",
        "Isuzu",
        "Jaguar",
        "Jeep",
        "Kia",
        "Land-Rover",
        "Lexus",
        "MG",
        "Maserati",
        "Mazda",
        "Mercedes-Benz",
        "Mini",
        "Mitsubishi",
        "Nissan",
        "Peugeot",
        "Porsche",
        "Renault",
        "Seat",
        "Skoda",
        "Smart",
        "Subaru",
        "Suzuki",
        "Toyota",
        "Vauxhall",
        "Volkswagen",
        "Volvo",
    )


    engines = ("Diesel", "Electric", "Hybrid", "Petrol", "  ")

    transmissions = ("Automatic", "Manual", "Semiautomatic")

    comp_name = st.selectbox("Make" , comp_name)
    age = st.slider("Age of Car", 1, 50, 1)
    mileage = st.number_input("Mileage", min_value=0, max_value=999999, value=0)
    engine = st.selectbox("Engine", engines)
    transmission = st.selectbox("Transmission", transmissions)



    # def input(mileage,engine,transmission,comp_name,age):   
            # manufacturer, age, mileage, engine, transmission
    new_data = [[mileage,engine,transmission,comp_name,age]]
    # convert to array
    new_data = np.array(new_data)
    new_data[:,3] = le_car.transform(new_data[:,3]) 
    new_data[:,1] = le_eng.transform(new_data[:,1])
    new_data[:,2] = le_trans.transform(new_data[:,2])
    new_data = scalar.transform(new_data)
    price = lr.predict(new_data)
    act_price = np.exp(price)+1
    act_price = round(act_price[0])

    text = "{}".format(act_price)
    txt = '&pound'


    ok = st.button("Predict Price")
    st.write('')
    if ok:
        st.write(
            """
            <div style="position: relative; height: 5px; width: 100%;">
                <h1 style="position: relative; top: -35px; left: 0%; color:#1974D2; font-size:35px; font-style: Bold">{}</h1>                
            </div>
            """.format(text),
            unsafe_allow_html=True)
        
        st.write(
            """
            <div style="position: relative; height: 5px; width: 100%;">
                <h1 style="position: relative; top: -50px; left: 10%; color:#000000; font-size:34px; font-style: Bold">{}</h1>                
            </div>
            """.format(txt),
            unsafe_allow_html=True)
        

        #st.subheader(act_price)        

    #     pounds = "\u00A3"
    # st.write(f"This product costs {pounds}10.")

