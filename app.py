from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('note-pad.html')

if __name__ == '__main__':  
   app.run('0.0.0.0', port=5000, debug=True)