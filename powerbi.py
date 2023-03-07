def run():

    import streamlit as st
    from PIL import Image
    import requests
    from io import BytesIO

    st.write("<h1 style='text-align: center; color: #00000; font-size: 70px;background-color: #96e3cd;;font-family:Tilt Warp;'>POWER BI PROJECT. </h1>", unsafe_allow_html=True)



    st.write("## Home Page")
    #image = Image.open(r"C:\Users\hrith\Desktop\powerbi images\slide1.png")
    #st.image(image)

    url = "https://raw.githubusercontent.com/Hrithik-K-S/portfolio/main/slide1.png"
    #https://github.com/Hrithik-K-S/portfolio/blob/main/slide1.png
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    st.image(img)

    st.write(" ")

    st.write("## Second Page")
    #image2 = Image.open(r"C:\Users\hrith\Desktop\powerbi images\slide2.png")
    #st.image(image2)
    url = "https://raw.githubusercontent.com/Hrithik-K-S/portfolio/main/slide2.png"
    #https://github.com/Hrithik-K-S/portfolio/blob/main/slide1.png
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    st.image(img)


    st.write(" ")



    st.write("## Third Page")
    # image3 = Image.open(r"C:\Users\hrith\Desktop\powerbi images\slide3.png")
    # st.image(image3)

    url = "https://raw.githubusercontent.com/Hrithik-K-S/portfolio/main/slide3.png"
    #https://github.com/Hrithik-K-S/portfolio/blob/main/slide1.png
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    st.image(img)
