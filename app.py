#*************************************************
# Kiarra Lavache
# kal2241
# ENGI1006
# Final Project
#*************************************************

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

@app.route("/The Real Talk Initiative")
def real_talk():
    return render_template('realtalk.html')

#start the server
if __name__ == "__main__":
    app.run()