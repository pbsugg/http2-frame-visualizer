from flask import Flask, render_template, request
import json
# from twisted_client import *
from twisted_runner import *
from celery import Celery, result
from messageHandler import messageHandler

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379'

celery = Celery(app.name, backend=app.config['CELERY_RESULT_BACKEND'], broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task(bind=True)
def run_web_server():
    ## run()
    return("hello")

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/start')
def return_client_request():
    #task = run_web_server.apply_async()
    #print(task.task_id)
    #print(task.status)
    print(handler.responseFrames)
    run()
    return("goodbye")
    
if __name__ == '__main__':
    app.run(debug=True)
