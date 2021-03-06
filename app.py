from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hi everyone. Want to present my app !</h1>'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, threaded=True, debug=True)