from xgboost import XGBClassifier
import pickle
from sklearn.preprocessing import LabelEncoder
import numpy as np

from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load models
with open('xgb_model.pickle', 'rb') as file:
    xgb_model = pickle.load(file)
with open('label_encoder.pickle', 'rb') as file:
    label_encoder = pickle.load(file)

answers = [0] * 60

@app.route('/api/test', methods=["GET"])
def test():
    return jsonify({
        'message': 'It works!!'
    })

@app.route('/api/submit', methods=['POST'])
def submit_answers():
    data = request.get_json()
    answers = data.get('answers', [])
    d = np.array(answers) # Get the data
    d = d.reshape(-1,60)
    pred = xgb_model.predict(d)
    result = label_encoder.inverse_transform(pred)
    
    return jsonify({
        'message': 'Result received',
        'result': str(result[0]),
    })


if __name__ == '__main__':
    app.run(debug=True)
