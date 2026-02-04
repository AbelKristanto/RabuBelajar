# Create appliation with Streamlit for Heart Disease Prediction
import streamlit as st
import pandas as pd
import pickle
import time
from PIL import Image
from sklearn.ensemble import RandomForestClassifier

# Load the model
location_filepath = "hasilgenerate.pkl"
with open(location_filepath, "rb") as f:
    heart_model = pickle.load(f)

# Set up page configuration
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)
# st.title("Heart Disease Prediction App")
# st.write("This app predicts the presence of heart disease based on user input. This is a demo application created for educational purposes and created by [DQlab](www.dqlab.id).")

# Function for heart disease prediction
def heart_disease():
    st.write("""
    # Heart Disease Prediction Form
    This app predicts whether a person has heart disease based on several health parameters. Please fill in the form below with your health data.
    Data obtained from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Heart+Disease).
""")
    # Image display
    img = Image.open("heart-disease.jpg")
    st.image(img, caption='Heart Disease', width=1000)
    st.sidebar.header("User Input Parameters")
    st.sidebar.markdown("*Please fill in the parameters below to predict heart disease.*")
    cp = st.sidebar.slider('Chest pain type', 1,4,2)
    if cp == 1.0:
        wcp = "Nyeri dada tipe angina"
    elif cp == 2.0:
        wcp = "Nyeri dada tipe nyeri tidak stabil"
    elif cp == 3.0:
        wcp = "Nyeri dada tipe nyeri tidak stabil yang parah"
    else:
        wcp = "Nyeri dada yang tidak terkait dengan masalah jantung"
    st.sidebar.write("Jenis nyeri dada yang dirasakan oleh pasien", wcp)
    thalach = st.sidebar.slider("Maximum heart rate achieved", 71, 202, 80)
    slope = st.sidebar.slider("Kemiringan segmen ST pada elektrokardiogram (EKG)", 0, 2, 1)
    oldpeak = st.sidebar.slider("Seberapa banyak ST segmen menurun atau depresi", 0.0, 6.2, 1.0)
    exang = st.sidebar.slider("Exercise induced angina", 0, 1, 1)
    ca = st.sidebar.slider("Number of major vessels", 0, 3, 1)
    thal = st.sidebar.slider("Hasil tes thalium", 1, 3, 1)
    sex = st.sidebar.selectbox("Jenis Kelamin", ('Perempuan', 'Pria'))
    if sex == "Perempuan":
        sex = 0
    else:
        sex = 1 
    age = st.sidebar.slider("Usia", 29, 77, 30)
    data = {'cp': cp,
            'thalach': thalach,
            'slope': slope,
            'oldpeak': oldpeak,
            'exang': exang,
            'ca':ca,
            'thal':thal,
            'sex': sex,
            'age':age}
    features = pd.DataFrame(data, index=[0])
    # button for prediction
    if st.sidebar.button("Predict"):
        st.subheader("User Input parameters")
        st.write(features)
        prediction = heart_model.predict(features)
        # Simulate processing time
        with st.spinner('Processing...'):
            time.sleep(3)
            st.balloons()
            if prediction == 0:
                st.success("The prediction result is: No Heart Disease")
            else:
                st.error("The prediction result is: Heart Disease Detected")

# Function for about section
def about_this_app():
    st.write("""
    ## About This App
    This Heart Disease Prediction App is developed using Streamlit, a powerful framework for building interactive web applications in Python. The app utilizes a machine learning model trained on the UCI Heart Disease dataset to predict the presence of heart disease based on user-provided health parameters.
    
    ### Features:
    - User-friendly interface for inputting health data.
    - Real-time prediction of heart disease risk.
    - Educational resource for understanding heart disease indicators.
    
    ### Disclaimer:
    This application is intended for educational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.
    
    ### Created by:
    [DQlab](www.dqlab.id)
    """)

# Function for about me section
def about_me():
    st.write("""
    ## About the Developer
    This Heart Disease Prediction App was developed by [DQlab](www.dqlab.id), a leading platform for data science and machine learning education. DQlab is dedicated to empowering individuals with the skills and knowledge needed to excel in the field of data science through comprehensive courses, hands-on projects, and expert guidance.
    
    ### Our Mission:
    - To provide high-quality education in data science and machine learning.
    - To foster a community of learners and professionals passionate about data.
    - To bridge the gap between theoretical knowledge and practical application.
    
    ### Connect with Us:
    - Website: [www.dqlab.id](www.dqlab.id)
    - Social Media: Follow us on [Twitter](https://twitter.com/dqlab_id), [LinkedIn](https://www.linkedin.com/company/dqlab/), and [Facebook](https://www.facebook.com/dqlab.id) for updates and resources.
    
    Thank you for using our app! We hope it serves as a valuable tool in your journey to understanding heart disease risk factors.
    """)

# Sidebar navigation
st.sidebar.title("Navigation")
options = st.sidebar.selectbox("Go to", ["Heart Disease Prediction", "About This App", "About Me"])
if options == "Heart Disease Prediction":
    heart_disease()
elif options == "About This App":
    about_this_app()
else:
    about_me()
