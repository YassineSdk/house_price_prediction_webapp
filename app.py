import streamlit as st 
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import LabelEncoder
import numpy as np 
import joblib
import time

st.set_page_config(page_title="house price prediction 🏠︎ ",
                   page_icon="🏠",
                   layout='wide')

page_bg_img = '''
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://media.istockphoto.com/id/1781299198/photo/dark-blue-living-room-interior-with-cozy-leather-armchair.jpg?s=2048x2048&w=is&k=20&c=LMoEmm-4RGJyndqniq4FGKLht8JhyvOuIW0dSFw0M3g=");
background-size: cover;
}
[data-testid="stHeader"]{
background-color: rgba(0,0,0,0);
}
[data-testid="stSidebar"]{
background-color: rgba(0,0,0,0);
}
[data-testid="element-container"]{
background-color: rgba(0,0,0,0);
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Housing price prediction 🏠︎ ")
intro_markdown = """

Welcome to the **House Price Prediction App**! This application leverages machine learning to predict house prices based on various features such as area, number of bedrooms, number of bathrooms, and other property attributes.
## How to Use:
1. **Enter Property Details**: Fill in the property details such as area, number of bedrooms, number of bathrooms, and other features in the sidebar.
2. **Get Prediction**: Click the "Predict" button to get the estimated price for the property.
3. **Clear Inputs**: Use the "Clear Inputs" button to reset the form and enter new details.
---

Feel free to explore and make the most out of our House Price Prediction App!
"""
st.markdown(intro_markdown)



def clear_txt():
    st.session_state[1] =""
    st.session_state[2] =""
    st.session_state[3] =""
    st.session_state[4] =""


with st.sidebar :
    st.header('Enter Property Details',divider="gray")
    options_forms = st.form('independance variables')
    area = options_forms.text_input('area',key=1)
    bedrooms = options_forms.text_input('num of bedrooms',key=2)
    bathrooms = options_forms.text_input('num of bathrooms',key=3)
    stories = options_forms.text_input('stories',key=4)
    mainroad = options_forms.selectbox(label='mainroad',
                                   options=['Yes','No'])
    guestroom = options_forms.selectbox(label='guestroom',
                                   options=['Yes','No'])
    basement = options_forms.selectbox(label='basement',
                                   options=['Yes','No'])
    hotwaterheating = options_forms.selectbox(label='hot water heating',
                                   options=['Yes','No'])
    airconditioning = options_forms.selectbox(label='air conditioning',
                                   options=['Yes','No'])
    parking = options_forms.selectbox(label='parking',
                                   options=['Yes','No'])
    prefarea = options_forms.selectbox(label='pref area',
                                   options=['Yes','No'])
    furnishingstatus= options_forms.selectbox(label='furnishing status',
                                   options=['Yes','No'])
    predict = options_forms.form_submit_button("predict")
    clear = st.button("clear",on_click=clear_txt)



if predict :
        if len(area) == 0 :
            st.error('entre at last the area', icon="🚨")
        else :    
        
            new_data = {
            'area': int(area) if area else None,
            'bedrooms': int(bedrooms) if bedrooms else None,
            'bathrooms': int(bathrooms) if bathrooms else None,
            'stories': int(stories) if stories else None,
            'main road': mainroad,
            'guest room': guestroom,
            'basement': basement,
            'hot water heating': hotwaterheating,
            'air conditioning': airconditioning,
            'parking': parking,
            'preferred area': prefarea,
            'furnishing status': furnishingstatus
        }
            LE = LabelEncoder()

            data = pd.DataFrame([new_data])
            df = data.copy()
            for col in df.columns:
                if df[col].dtypes =='object':
                    df[col]=LE.fit_transform(df[col])
            features = df.values
            model = joblib.load('house_price.joblib')
            prediction =model.predict(features)
            prediction = np.round(prediction,2)
            prediction_value = prediction[0]
            with st.container(border=True):
                st.table(data)
                with st.spinner('Wait for it...'):
                    time.sleep(5)
                    st.success('Done!')
                st.markdown('the house price prediction is :')
                st.subheader(f"the estimated  price of this house : {prediction_value}$")
        
       
            

                    
                 
                   

        
        
        
        
       






























