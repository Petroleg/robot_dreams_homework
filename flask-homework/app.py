from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/oleh")
def hello_world_json():
    return jsonify({"hello": "world!"})


@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/hello/html')
def hello_world_html():
    return "<strong>Hello world!</strong>"


if __name__ == '__main__':
    app.run(debug=True)
