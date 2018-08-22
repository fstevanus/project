import requests
from flask import render_template, redirect, url_for, request
from . import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/asem')
def asem():
    return render_template('tets.html')

@app.route('/asem', methods = ['POST', 'GET'])
def aseasm():
    if request.method == 'POST':
        user = request.form['nm']
        return requests.get('https://heygaron.serveo.net/getLocationxrequestx3nux1x0').content
