import streamlit as st
import base64
import sklearn
import numpy as np
import pickle 






#Load the saved model
# APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# pk_path = os.path.join(APP_ROOT,'final_model.p') 
# model_a = open('final_model.pkl','rb')
# model = pkl.load(model_a)


xgb_pickle = open('final_model.p', 'rb')
xgb = pickle.load(xgb_pickle)
xgb_pickle.close()

# with open("final_model.pkl", "rb") as pickle_file:
#     model = pickle.load(pickle_file)
   
# model=pkl.load(open("final_model.p","rb"))



st.set_page_config(page_title="rct App",page_icon="⚕️",layout="centered",initial_sidebar_state="expanded")




def preprocess(sex,age,side,vas,time,trauma,flex,abd,er,ir,jobe,,erls,lift,belly,bear,ojobe,irls ):   
 
   
    if sex=="female":
        sex=1
    else: sex=0

        
    if side=="Yes":
        side=1 
    else: side=0
  
    

        
    if trauma=="Yes":
        trauma=1 
    else: trauma=0
    
    if jobe=="+":
        jobe=1 
    else: jobe=0
        
    if bear=="+":
        bear=1 
    else: bear= 0
        
    if belly=="+":
        belly=1 
    else: belly= 0
    
    if erls=="+":
        erls=1 
    else: erls= 0
      
    if ojobe=="+":
        ojobe=1 
    else: ojobe= 0
    
    if irls=="+":
        irls=1 
    else: irls= 0
      
    if lift=="+":
        lift=1 
    else: lift= 0
      
    

    
  
    
        
    user_input=[sex,age,side,vas,time,trauma,flex,abd,er,ir,jobe,erls,lift,belly,bear,ojobe,irls ]
    user_input=np.array(user_input)
    user_input=user_input.reshape(1,-1)
#     user_input=scal.fit_transform(user_input)
    prediction = xgb.predict(user_input,validate_features=False)
  

    return int(prediction)


 # front end elements of the web page 
html_temp = """ 
    <div style ="background-color:pink;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Diagnosis of RCT App</h1> 
    </div> 
    """

# display the front end aspect
st.markdown(html_temp, unsafe_allow_html = True) 
# following lines create boxes in which user can enter data required to make prediction
sex = st.radio("Select Gender: ", ( 'female','male'))
age = st.slider("Age",min_value=0,max_value=100,step=1)
side=st.radio("is the painful shoulder your dominant side?", ['Yes','No'])
vas = st.slider("VAS",min_value=0,max_value=10,step=1)
time = st.slider("Duration of symptoms, months",min_value=0,max_value=24,step=1)
trauma=st.radio("have you get injuried in your shoulder?", ['Yes','No'])
flex=st.sliderx('Flexion',min_value=0,max_value=180,step=10)
abd=st.slider('Abduction',min_value=0,max_value=180,step=10)
er=st.slider('External rotation',min_value=0,max_value=80,step=10)
ir=st.slider('Internal rotation,= thi,butt,S 1,L5,L 3,L 1,T 11,T 9,T 7,T 5,T 3,= 0,1,2,3,4,5,6,7,8,9,10',min_value=0,max_value=10,step=1)
jobe=st.radio("JOBE test", ['+','-'])
erls=st.radio("ERLS", ['+','-'])
lift= st.radio("Lift-off", ['+','-'])
belly=st.radio("BELLY PRESS", ['+','-'])
bear=st.radio("BEAR HUG", ['+','-'])
ojobe= st.radio("0-Jobe", ['+','-'])
irls = st.radio("IRLS", ['+','-'])




# cp = st.selectbox('Chest Pain Type',("Typical angina","Atypical angina","Non-anginal pain","Asymptomatic")) 
# trestbps=st.selectbox('Resting Blood Sugar',range(1,500,1))
# restecg=st.selectbox('Resting Electrocardiographic Results',("Nothing to note","ST-T Wave abnormality","Possible or definite left ventricular hypertrophy"))
# chol=st.selectbox('Serum Cholestoral in mg/dl',range(1,1000,1))
# fbs=st.radio("Fasting Blood Sugar higher than 120 mg/dl", ['Yes','No'])
# thalach=st.selectbox('Maximum Heart Rate Achieved',range(1,300,1))
# exang=st.selectbox('Exercise Induced Angina',["Yes","No"])
# oldpeak=st.number_input('Oldpeak')


#user_input=preprocess(sex,cp,exang, fbs, slope, thal )
pred=preprocess(sex,age,side,vas,time,trauma,flex,abd,er,ir,jobe,,erls,lift,belly,bear,ojobe,irls )

if st.button("Predict"):              
  if pred == 1:
    st.success('Warning! You have high risk of getting rct!)
    st.info("Caution: This is just a prediction and not doctoral advice. Kindly see a doctor if you feel the symptoms persist.")
   
  else:
    st.success('You have lower risk of getting rct!)
    st.info("Caution: This is just a prediction and not doctoral advice. Kindly see a doctor if you feel the symptoms persist.") 

#  else:
#     st.error('Warning! You have high risk of getting a rct!')
    
#     st.info("Caution: This is just a prediction and not doctoral advice. Kindly see a doctor if you feel the symptoms persist.") 



st.sidebar.subheader("About App")

st.sidebar.info("This web app is helps you to find out whether you are at a risk of developing a RCT.")
st.sidebar.info("Enter the required fields and click on the 'Predict' button to check whether you have a healthy shoulder")







  
