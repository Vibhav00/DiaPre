import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS,cross_origin
import pickle
import json

app = Flask(__name__)
model = pickle.load(open('diabetes_model.sav', 'rb'))
CORS(app)
CORS(app, resources={r"/predict": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def home():
    return render_template('index.html')





@app.route('/predict',methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    print()
    print()
    print()
    print(request.form)
    print()
    print()
    print()
    
    
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 7)
    if(output==1):
         return render_template('index.html', prediction_text="having dia")
    else:
        return render_template('index.html', prediction_text="no dia")
    
    
@app.route('/pre',methods=['POST'])
def ab():
     input_data = request.json
     print()
     print(request.form)
     print()
     print(type(input_data))
     print("ljldjfsljlsfjlsjdlfjsljlfsjjdlfsjlfjl")
     print(input_data['Age'])
     print()
# =============================================================================
#      input_dictionary = json.load(input_data) 
# =============================================================================
    
     preg = input_data['pregnancies']
     glu = input_data['Glucose']
     bp = input_data['BloodPressure']
     skin = input_data['SkinThickness']
     insulin = input_data['Insulin']
     bmi = input_data['BMI']
     dpf = input_data['DiabetesPedigreeFunction']
     age = input_data['Age']
     
  
    
     input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]
     
     prediction = model.predict([input_list])
       

    
     if (prediction == 0):
        return  {'pre':"not dia"}
     else:
        return  {'pre':"dia"}

if __name__ == "__main__":
    app.run(debug=True)