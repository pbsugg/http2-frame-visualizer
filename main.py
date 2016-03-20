from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/start')
def stop():
    return "NO"

if __name__ == '__main__':
    app.run(debug=True)
