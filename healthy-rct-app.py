import streamlit as st
import base64
import sklearn
import numpy as np
import pickle 
from sklearn.preprocessing import MinMaxScaler
scal=MinMaxScaler()
import os





#Load the saved model
# APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# pkl_path = os.path.join(APP_ROOT,'final_model.pkl') 
# model_a = open('final_model.pkl','rb')
# model = pkl.load(model_a)


xgb_pickle = open('final_model.pkl', 'rb')
xgb = pickle.load(xgb_pickle)
xgb_pickle.close()

# with open("final_model.pkl", "rb") as pickle_file:
#     model = pickle.load(pickle_file)
   
# model=pkl.load(open("final_model.p","rb"))



st.set_page_config(page_title="rct App",page_icon="⚕️",layout="centered",initial_sidebar_state="expanded")




def preprocess(sex,age,side,trauma,jobe,bear,belly,erls,ss,ISs,ssc,ases,const,ucla,flex,abd,er,ir,vas,time ):   
 
   
    if sex=="female":
        sex=1
    else: sex=0
    
    #age
        
    if side=="Yes":
        side=1 
    else: side=0
        
    if vas=="0-4":
        vas=0
    elif vas == "5-7":
        vas=1
    else: vas=2
    
    if time=="0-3":
        time=0
    elif time == "3-6":
        time=1
    elif time == "6-12":
        time=2
    else: time = 3
        
    if trauma=="Yes":
        trauma=1 
    else: trauma=0
        
    if flex=="0-45":
        flex=0
    elif flex == "45-90":
        flex=1
    elif flex == "90-135":
        flex=2
    else: flex = 3
        
    if abd=="0-45":
        abd=0
    elif abd == "45-90":
        abd=1
    elif abd == "90-135":
        abd=2
    else: abd = 3
        
    if er=="0-20":
        er=0
    elif er == "20-40":
        er=1
    elif er == "40-60":
        er=2
    else: er = 3
        
    if ir=="below S1":
        ir=0
    elif ir == "L1-L5":
        ir=1
    else: ir = 2
    
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
        
    # ss is ssc ases const ucla
    
  
    

    user_input=[age,sex,side,trauma,jobe,bear,belly,erls,ss,ISs,ssc,ases,const,ucla,flex,abd,er,ir,vas,time ]
    user_input=np.array(user_input)
    user_input=user_input.reshape(1,-1)
    user_input=scal.fit_transform(user_input)
    prediction = xgb.predict(user_input)
   

    return prediction


 # front end elements of the web page 
html_temp = """ 
    <div style ="background-color:pink;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Diagnosis of RCT App</h1> 
    </div> 
    """

# display the front end aspect
st.markdown(html_temp, unsafe_allow_html = True) 
# following lines create boxes in which user can enter data required to make prediction
age=st.selectbox ("Age",range(1,121,1))
sex = st.radio("Select Gender: ", ( 'female','male'))
side=st.radio("is the painful shoulder your dominant side?", ['Yes','No'])
trauma=st.radio("have you get injuried in your shoulder?", ['Yes','No'])
jobe=st.radio("JOBE test", ['+','-'])
bear=st.radio("BEAR HUG", ['+','-'])
belly=st.radio("BELLY PRESS", ['+','-'])
erls=st.radio("ERLS", ['+','-'])
ss=st.selectbox('the strength of supraspinatus ',range(0,5,1))
ISs=st.selectbox('the strength of infraspinatus',range(0,5,1)) 
ssc=st.selectbox('the strength of subscapularis ',range(0,5,1))
ases=st.selectbox ("ASES",range(1,100,1))
const=st.selectbox ("Constant-Murley",range(1,100,1))
ucla=st.selectbox ("UCLA",range(1,100,1))

flex=st.selectbox('Flexion',("0-45°","45-90°","90-135°","135-180°"))
abd=st.selectbox('Abduction',("0-45°","45-90°","90-135°","135-180°"))
er=st.selectbox('External rotation',("0-20°","20-40°","40-60°","60-80°"))
ir=st.selectbox('Internal rotation',("below S1","L1-L5","above T12"))
vas=st.selectbox('VAS',("0-4","5-7","8-10°"))
time=st.selectbox('Duration of symptoms/months',("<3","3-6","6-12",">12"))



# cp = st.selectbox('Chest Pain Type',("Typical angina","Atypical angina","Non-anginal pain","Asymptomatic")) 
# trestbps=st.selectbox('Resting Blood Sugar',range(1,500,1))
# restecg=st.selectbox('Resting Electrocardiographic Results',("Nothing to note","ST-T Wave abnormality","Possible or definite left ventricular hypertrophy"))
# chol=st.selectbox('Serum Cholestoral in mg/dl',range(1,1000,1))
# fbs=st.radio("Fasting Blood Sugar higher than 120 mg/dl", ['Yes','No'])
# thalach=st.selectbox('Maximum Heart Rate Achieved',range(1,300,1))
# exang=st.selectbox('Exercise Induced Angina',["Yes","No"])
# oldpeak=st.number_input('Oldpeak')


#user_input=preprocess(sex,cp,exang, fbs, slope, thal )
pred=preprocess(age,sex,side,trauma,jobe,bear,belly,erls,ss,ISs,ssc,ases,const,ucla,flex,abd,er,ir,vas,time)


if st.button("Predict"):    
 if pred[0] == 0:
    st.error('Warning! You have high risk of getting a rct!')

 else:
    st.success('You have lower risk of getting a rct!')


st.sidebar.subheader("About App")

st.sidebar.info("This web app is helps you to find out whether you are at a risk of developing a RCT.")
st.sidebar.info("Enter the required fields and click on the 'Predict' button to check whether you have a healthy shoulder")
st.sidebar.info("Don't forget to rate this app")



feedback = st.sidebar.slider('How much would you rate this app?',min_value=0,max_value=5,step=1)

if feedback:
  st.header("Thank you for rating the app!")
  st.info("Caution: This is just a prediction and not doctoral advice. Kindly see a doctor if you feel the symptoms persist.") 
