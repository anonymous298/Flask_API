from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/api/<string:name>')
def api(name):
    return jsonify({'name' : name})

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')