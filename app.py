from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/v1/ping')
def ping():
    return jsonify(message='Ping!')

if __name__ == '__main__':
    app.run(debug=True)