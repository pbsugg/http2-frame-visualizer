from flask import Flask, render_template, request
import json
from celery import Celery, result
from flask import jsonify, url_for
import time

from messageHandler import messageHandler


import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__)) 
# not sure if this is best practice for importing from other directories,
import sys
from twisted_client import *
from twisted_runner import *

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

#route to run http2 request and return its task ID
#runs the next method down, which depends on the task id
@app.route('/http2', methods=['POST'])
def start_http2_request():
    task = run_http2.apply_async()
    time.sleep(2)
    return http2request(task.id)
    # return jsonify({}), 202, {'Location': url_for('http2request',
    #                                                task_id=task.id) } 

@app.route('/http2request/<task_id>')
def http2request(task_id):
    print(task_id)
    task = run_http2.AsyncResult(task_id)
    print(task.state)
    return "done"
    # task.state = 'PENDING'

#celery function that runs my http2 server
@celery.task(bind=True)
def run_http2(self):
    bob = messageHandler()
    run(bob)
    if bob.responseFrames:
        print("yes")
    else:
        print("no")
    print(bob.responseFrames)

if __name__ == '__main__':
    app.run(debug=True)
