from flask import Flask, render_template, request
import pickle
import numpy as np
app = Flask(__name__)

model = pickle.load(open('model1.pkl', 'rb'))

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
	int_features = [float(x) for x in request.form.values()]
	final = np.array(int_features)
	example = final.reshape(1, -1)
	output = model.predict(example)

	if(output[0] == 0):
		return render_template('index.html', pred='Low Risk')
	elif(output[0] == 1):
		return render_template('index.html', pred='High Risk')


if __name__ == "__main__":
	app.run(host= '127.0.0.1', port=5001, debug=True)


