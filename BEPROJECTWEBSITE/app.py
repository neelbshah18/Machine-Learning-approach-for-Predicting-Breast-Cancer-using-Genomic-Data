from flask import Flask, render_template, request
import pickle
import numpy as np
app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
	int_features = [float(x) for x in request.form.values()]
	final = [np.array(int_features)]
	output = model.predict(final)

	if(output[0] == 1):
		return render_template('index.html', pred=' High Risk')
	elif(output[0] == 0):
		return render_template('index.html', pred=' Low Risk')


if __name__ == "__main__":
	app.run(debug=True)

