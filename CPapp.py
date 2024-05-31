from flask import Flask, render_template, request, redirect
import pickle 

app = Flask(__name__)

# Assuming your saved model file is named 'model.pkl'
with open('model/modelrff.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Extract form data
            nitrogen = float(request.form['nitrogen'])
            phosphorus = float(request.form['phosphorus'])
            potassium = float(request.form['potassium'])
            temperature = float(request.form['temperature'])
            humidity = float(request.form['humidity'])
            ph_value = float(request.form['ph_value'])
            rainfall = float(request.form['rainfall'])

            features = [[nitrogen, phosphorus, potassium, temperature, humidity, ph_value, rainfall]]


            # Make prediction
            predicted_crop = model.predict(features)[0]

            return render_template('index.html', prediction=predicted_crop)
        except TypeError:
            prediction = "Type error ."
            return render_template('error.html', prediction=prediction)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
