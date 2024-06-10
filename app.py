from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/test', methods=["GET"])
def test():
    return jsonify({
        'message': 'It works!!'
    })

if __name__ == '__main__':
    app.run(debug=True)
