from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/hello')
def stop():
    return "NO"

if __name__ == '__main__':
    app.run(debug=True)
