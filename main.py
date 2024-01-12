import pandas as pd
from flask import Flask,render_template,request
import pickle 
import numpy as np

app=Flask(__name__)
df=pd.read_csv('./Cleaned_Data.csv')
pipe=pickle.load(open("Model.pkl",'rb'))


# we have set bath,bhk and size as number in the input field of the html form..
# if any confusion or error then change it back asap

@app.route('/predict',methods=['POST'])
def predict():
    
    locations=request.form.get('location')
    bhk = float(request.form.get('bhk'))
    bath = float(request.form.get('bath'))
    sqft = request.form.get('sqft')
    
    
    input=pd.DataFrame([[locations,bhk,sqft,bath]],columns=['location','size','total_sqft','bath'])
    
    prediction = pipe.predict(input)[0]*1e5;

    # reduced_prediction = prediction.reduce_precision(prediction,2)
    return str(np.round(prediction,2))


@app.route('/')
def index():
    locations = sorted(df['location'].unique())
    return render_template('index.html',locations=locations)


if __name__ == "__main__":
    app.run(debug=True,port=5001)