import streamlit as st
import pandas as pd

from src.pipeline.prediciton_pipeline import PredictionPipeline

st.title("Loan Default Prediction")
st.write("""
This app predicts if a customer would default their loan or not
""")
st.write("---")

numerical_features = ['Loan Amount', 'Funded Amount', 'Funded Amount Investor', 'Term',
       'Interest Rate', 'Employment_Duration', 'Debit to Income',
       'Delinquency - two years', 'Inquires - six months', 'Open Account',
       'Public Record', 'Revolving Balance', 'Revolving Utilities',
       'Total Accounts', 'Total Received Interest', 'Total Received Late Fee',
       'Recoveries', 'Collection Recovery Fee', 'Collection 12 months Medical',
       'Last week Pay', 'Total Collection Amount', 'Total Current Balance',
       'Total Revolving Credit Limit']



entered_values = {}
st.sidebar.title('Numerical Inputs')

# Loop through each feature and create a numerical input bar
for feature in numerical_features:
    value = st.sidebar.number_input(feature, value=0.0)
    entered_values[feature] = value

col1, col2 = st.columns([1,2])


categorical_options = {"Grade" :['','b' ,'c', 'f', 'a' ,'g', 'e', 'd'],
"Sub Grade": ['','c4', 'd3', 'd4' ,'c3', 'g5', 'c5', 'a5', 'c2', 'b5', 'b1', 'b4', 'a4', 'b2', 'd2',
 'c1', 'f3', 'd1', 'f2', 'a2', 'a3', 'f1', 'e5', 'b3', 'f4', 'g1', 'f5', 'e1', 'e2',
 'd5', 'g2', 'e4', 'a1', 'g3', 'e3', 'g4'],
"Home_Ownership": ['','mortgage' ,'rent', 'own'],
"Verification Status": ['','not verified', 'source verified', 'verified'],
"Loan Title": ['','debt consolidation' ,'credit card refinance', 'home improvement',
 'credit consolidation', 'green loan', 'other', 'moving and relocation',
 'credit card', 'medical', 'refinance', 'lending club',
 'debt consolidation loan', 'major purchase', 'vacation', 'business'
 'personal' ,'loan' ,'consolidation' ,'car financing', 'debt', 'home buying',
 'freedom', 'house', 'credit loan', 'payoff', 'credit pay off', 'wedding loan',
 'credit', 'pool', 'conso', 'lending loan', 'relief' 'bills'],
"Initial List Status" : ['','w', 'f'],
"Application Type": ['','individual', 'joint']}


col1.subheader('Enter Categorical Inputs')
    
# Loop through each categorical feature and create a dropdown menu
for feature, options in categorical_options.items():
    value = col1.selectbox(feature, options= options)
    entered_values[feature] = value

if col2.button("GET PREDICTION"):
    data_frame = pd.DataFrame(entered_values, index = [0])
    obj = PredictionPipeline(data= data_frame)
    prediction = obj.predict()

    col2.header("Loan Status Prediction")
    if prediction == 1:
        prediction = "DEFAULT"
    else:
        prediction = "Not Default"
        
    col2.write(prediction)