from flask import Flask
app = Flask(__name__)

@app.route('/')
def start():
    return '<h1>Python HTTP2 Visualizer<h1>'

@app.route('/hello')
def stop():
    return "NO"

if __name__ == '__main__':
    app.run(debug=True)
