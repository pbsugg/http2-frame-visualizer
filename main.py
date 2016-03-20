from flask import Flask, render_template, request
import json
from twisted_client import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/start')
def return_client_request():
    run()
    return("hello")

    
if __name__ == '__main__':
    app.run(debug=True)
