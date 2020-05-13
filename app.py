# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def main_page():
     return render_template('mainpage.html')
 
@app.route("/Pre-Med")
def pre_med():
    return render_template('pre-med.html')

#start the server
if __name__ == "__main__":
    app.run()