from flask import render_template
from app import app

@app.route('/')
def home():
   return "Mi segundo Docker"

@app.route('/home')
def home2():
   return render_template('home.html')

