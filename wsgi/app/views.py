from app import app
from flask import render_template, request
import unirest
from forms import MessageForm
from app import database, simple
from flask_navigation import Navigation
import os

@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html")

@app.route('/emotion/')
def emotion():
	return render_template("my_form.html",mood='Positive',form=MessageForm())

@app.route('/emotion/', methods=['POST'])
def emotion_post():
	msg = request.form['message']
	response = unirest.post("https://community-sentiment.p.mashape.com/text/",
	  headers={
	    "X-Mashape-Key": os.environ['APITOKEN'],
	    "Content-Type": "application/x-www-form-urlencoded",
    	"Accept": "application/json"
    	},
  		params={
    	"txt": msg
  		}
	)
	return render_template("my_form.html",mood=response.body['result']['sentiment'],form=MessageForm())

nav = Navigation(app)
nav.Bar('top', [
    nav.Item('Home','index'),
    nav.Item('Emotion App','emotion'),
    nav.Item('Visualization','polynomial'),
    nav.Item('Database','get_all_database_info')])
