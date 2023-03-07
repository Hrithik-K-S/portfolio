import streamlit as st
import linear
import logistic
import powerbi

st.set_page_config(
    page_title="My Resume",
    page_icon=":memo:",
    layout="wide",
    #initial_sidebar_state="collapsed",
)


def show_main_page():
    # Set page style
   

    # Add custom CSS
    st.markdown(
        """
        <style>
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
        st.write("<div style='display: flex; justify-content: center; align-items: center; flex-direction: column; text-align: center; color: #ffffff; font-size:45px; background-color: #EBECF0; font-family: Franklin Gothic Medium (Headings); height: 50vh;'>\
                    <div>HRITHIK K S</div>\
                    <div style='font-size: 18px;'>hrithik.ks@outlook.com</div>\
                    <div style='font-size: 18px;'>K R Puram, Bangalore 560036</div>\
                    </div>", unsafe_allow_html=True)
        # st.write('Email: hrithik.ks@outlook.com')
        # st.write('Phone: 8546926069')

    with st.container():
        st.markdown('## Objective')
        st.write('A highly motivated and analytical data science professional seeking to leverage my strong technical skills, and passion for problem-solving to contribute to the success of an organization in the field of data science. I aim to generate valuable insights that drive decision-making and support business growth.')

    with st.container():
        st.markdown('## Skills & Abilities')
        st.write('Programming: Python')
        st.write('Libraries: Pandas, NumPy, Matplotlib, Scikit-learn.')
        st.write('Databases: MySQL, MS SQL')
        st.write('Visualization: Excel, PowerPoint, Power BI')
        st.write('Operating Systems: Windows')

    with st.container():
        st.markdown('## Projects')
        st.write('### Car price prediction using Linear regression.')
        st.write('### Heat attack prediction using logistic regression.')
        st.write('### Exploratory data analysis on Games sales with charts using POWERBI.')
        st.write('### Engineering Project - I designed a cassette ceiling air conditioning system that includes integrated lighting, speakers, and a projector, with voice-activated features.')

    with st.container():
        st.markdown('## Education')
        st.write('VEMANA INSTITUTE OF TECHNOLOGY')
        st.write('BACHELOR’S IN MECHANICAL ENGINEERING')
        st.write('Scored CGPA of 7.')

    with st.container():
        st.markdown('## Experience')
        st.write('CFD ENGINEER, MARUTEE DESIGN AND ENGINEERING')
        st.write('SEPT 22, 2021 – TO DATE')
        st.write('• Performed flow and thermal simulations to optimize designs and enhance performance.')
        st.write('• Proficient in Excel for efficient analysis and decision-making.')

    with st.container():
        st.markdown('## Courses')
        st.write('### Google Data Analytics Professional Certificate, Coursera')
        st.write('### Python 101 for Data Science, Cognitiveclass.ai, Powered by IBM')
        st.write('### Vehicle Dynamics - ETG')




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



