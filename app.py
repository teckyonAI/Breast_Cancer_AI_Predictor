
import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle

app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    float_feature = [float(value) for value in request.form.values() ]

    final_features = [np.array(float_feature)]

    prediction = model.predict(final_features)

    return render_template('result.html', res=prediction)

if __name__=="__main__":
    app.run(debug=True)    
    
    

