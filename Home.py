import streamlit as st
import linear
import logistic
import powerbi
import requests
from PIL import Image
from io import BytesIO
import toml
#https://hrithik-k-s-portfolio-home-34095i.streamlit.app/
# Define repository and file paths

#     #https://github.com/Hrithik-K-S/portfolio/blob/main/slide1.png
# response = requests.get(url)

# # Get contents of file

# # Decode contents from base64 and load as TOML
# config = toml.loads(response.text)

# # Access config values
# my_value = config["section"]["my_key"]


st.set_page_config(
    page_title="My Resume",
    page_icon=":memo:",
    layout="wide"
    #initial_sidebar_state="collapsed",
)


def show_main_page():
    # Set page style
   

    # Add custom CSS
    st.markdown(
        """
        <style>
            .stSideBar {
                    position: relative !important;
            }
            .stApp > main {
                    position: relative;
            }
            .text {
                    position: absolute;
                    top: 50px;
                    left: 50px;
            }
            .header {
                font-size: 2.5rem;
                font-weight: bold;
                text-transform: uppercase;
                margin-bottom: 1rem;
            }

            .subheader {
                font-size: 1.5rem;
                font-weight: bold;
                margin-bottom: 0.5rem;
            }

            .section {
                margin-top: 2rem;
            }

            .section-header {
                font-size: 1.2rem;
                font-weight: bold;
                margin-bottom: 0.5rem;
            }

            .project-item {
                margin-bottom: 0.5rem;
            }

            .course-item {
                margin-bottom: 0.5rem;
            }
        </style>
    """,
        unsafe_allow_html=True,
    )

    # Display resume information
    #st.title('My Resume')

    with st.container():
       # st.markdown('# Personal Information #')
       
        background_image_path = r"C:\Users\hrith\Desktop\linear_regression\cover-image(1).png"

        st.write(
            f"""
            <div style='display: flex; justify-content: space-between; align-items: center; flex-direction: row; text-align: center; 
                        color: #ffb300; font-size: 45px; background-image: url("{background_image_path}"); 
                        background-repeat: no-repeat; background-size: cover; font-family: Franklin Gothic Medium (Headings); 
                        height: 50vh;'>
                <div>
                    <strong>HRITHIK K S</strong><br>
                    <div style='font-size: 18px;'>hrithik.ks@outlook.com</div>
                    <div style='font-size: 18px;'>+91 8546926069</div>
                </div>
                <div style='display: flex; justify-content: flex-end;'>
                    <img src='https://raw.githubusercontent.com/Hrithik-K-S/Portfolio/main/profile-pic(4).png' width=230>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


        # st.write('Email: hrithik.ks@outlook.com')
        # st.write('Phone: 8546926069')
    table_code = """
        <table style='border-collapse: collapse;'>
            <thread>
                <tr>
                    <th><div style="text-align:right"><h2>Skills & Abilities</h2></div></th>
                    <th><div style="text-align:left"><h2>Objective</h2></div</th>
                </tr>
            </thread>
            <thread>
                <tr>
                    <td>Programming: Python,Libraries: Pandas, NumPy, Matplotlib, Scikit-learn,Databases: MySQL, MS SQL,Visualization: Excel, PowerPoint, Power BI,Operating Systems: Windows</td>
                    <td> A highly motivated and analytical data science professional seeking to leverage my strong technical skills, and passion for problem-solving to contribute to the success of an organization in the field of data science.\
        I aim to generate valuable insights that drive decision-making and support business growth.</td>
                </tr>
            </thread>
            <thread>
                <tr>
                    <th><div style="text-align:right"><h2>Education</h2></div></th>
                    <th><div style="text-align:left"><h2>Projects</h2></div</th>
                </tr>
            </thread>
            <thread>
                <tr>
                    <td>VEMANA INSTITUTE OF TECHNOLOGY\
                        BACHELOR’S IN MECHANICAL ENGINEERING\
                        Scored CGPA of 7.</td>
                    <td>Car price prediction using Linear regression.\
                        Heat attack prediction using logistic regression.\
                        Exploratory data analysis on Games sales with charts using POWERBI.\
                        Engineering Project - I designed a cassette ceiling air conditioning system that includes integrated lighting, speakers, and a projector, with voice-activated features.</td>
                </tr>        
            </thread>
            <thread>
                <tr>
                    <th><div style="text-align:right"><h2>Courses</h2></div></th>
                    <th><div style="text-align:left"><h2>Experience</h2></div</th>
                </tr>
            </thread>
            <thread>
                <tr>
                    <td>
                    Google Data Analytics Professional Certificate, Coursera\
                    Python 101 for Data Science, Cognitiveclass.ai, Powered by IBM\
                    Vehicle Dynamics - ETG </td>

                    <td>
                    ok </td>
                </tr>
            </thread>

        </table>
    """
    st.write(table_code, unsafe_allow_html=True)
    #streamlit run import_streamlit_as_st.py
    left,right = st.columns(2, gap='small') 

    with right:

        st.markdown('<div style="text-align:left"><h2>Objective</h2></div>', unsafe_allow_html=True)
        st.write('<div style="display: flex; justify-content: left; align-items: left; text-align: left; text-wrap: avoid;">A highly motivated and analytical data science professional seeking to leverage my strong technical skills, and passion for problem-solving to contribute to the success of an organization in the field of data science.\
        I aim to generate valuable insights that drive decision-making and support business growth.</div>', unsafe_allow_html=True)
    
    with left:

        with st.container():
            st.markdown('<div style="text-align:right"><h2>Skills & Abilities</h2></div',unsafe_allow_html=True)
            st.write("<div style='text-align: right'>Programming: Python</div>", unsafe_allow_html=True)
            st.write("<div style = 'text-align:right'>Libraries: Pandas, NumPy, Matplotlib, Scikit-learn</div>",unsafe_allow_html=True)
            st.write("<div style = 'text-align:right'>Databases: MySQL, MS SQL</div>",unsafe_allow_html=True)
            st.write("<div style = 'text-align:right'>Visualization: Excel, PowerPoint, Power BI</div>",unsafe_allow_html=True)
            #st.write('Databases: MySQL, MS SQL')
            
            #st.write('Visualization: Excel, PowerPoint, Power BI')
            st.write("<div style = 'text-align:right'>Operating Systems: Windows</div>",unsafe_allow_html=True)
            #st.write('Operating Systems: Windows')
        
    with right:
  
        with st.container():
            st.markdown('## Projects')
            st.write("<div style='text-align: left'>Car price prediction using Linear regression.</div>", unsafe_allow_html=True)
            st.write("<div style='text-align: left'>Heat attack prediction using logistic regression.</div>", unsafe_allow_html=True)
            st.write("<div style='text-align: left'>Exploratory data analysis on Games sales with charts using POWERBI.</div>", unsafe_allow_html=True)
            st.write("<div style='text-align: left'>Engineering Project - I designed a cassette ceiling air conditioning system that includes integrated lighting, speakers, and a projector, with voice-activated features.</div>", unsafe_allow_html=True)


    with left:
        with st.container():
            st.markdown("<div style ='text-align:right'><h2>Education</h2></div>",unsafe_allow_html=True)
            st.write("<div style='text-align: right'>VEMANA INSTITUTE OF TECHNOLOGY</div>", unsafe_allow_html=True)
            st.write("<div style='text-align: right'>BACHELOR’S IN MECHANICAL ENGINEERING</div>", unsafe_allow_html=True)
            st.write("<div style='text-align: right'>Scored CGPA of 7.</div>", unsafe_allow_html=True)
        st.write("")
        st.write("")

    with right:
        with st.container():
            st.markdown('## Experience')
            st.write("<div style = 'text-align':left'>CFD ENGINEER, MARUTEE DESIGN AND ENGINEERING</div>",unsafe_allow_html=True)
            st.write("<div style = 'text-align:left'>SEPT 22, 2021 – TO DATE</div>",unsafe_allow_html=True)
            st.write("<div style ='text-align:left'> Performed flow and thermal simulations to optimize designs and enhance performance</div>",unsafe_allow_html=True)
            st.write("<div style = 'text-align:left'>Proficient in Excel for efficient analysis and decision-making</div>",unsafe_allow_html=True)
    with left:
        with st.container():
            st.markdown("<div style = 'text-align:right'><h2>Courses</h2></div>",unsafe_allow_html=True)
            st.write("<div style = 'text-align:right'>Google Data Analytics Professional Certificate, Coursera</div>",unsafe_allow_html=True)
            st.write("<div style = 'text-align:right'>Python 101 for Data Science, Cognitiveclass.ai, Powered by IBM</div>",unsafe_allow_html=True)
            st.write("<div style = 'text-align:right'>Vehicle Dynamics - ETG</div>",unsafe_allow_html=True)




def select_project():
    st.sidebar.title("My projects")    
    # project01 = st.sidebar.radio("Home", ["Home"])
    project = st.sidebar.selectbox('select', ["Home","Linear Regression", "Logistic Regression",'PowerBI'])
    return project




# Handle project selection
project = select_project()

if project == "Linear Regression":
    linear.run()
    # if show_back_to_main_button():
    #     project = None
    #     show_main_page()

elif project == "Logistic Regression":
    logistic.run()
    # if show_back_to_main_button():
    #     project = None
    #     show_main_page()

elif project == "PowerBI":
    powerbi.run()
    

else:
    show_main_page()



