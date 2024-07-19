from flask import Flask, request, render_template_string
from flask_basicauth import BasicAuth
from dotenv import load_dotenv
import os
import subprocess

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = os.getenv('USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.getenv('PASSWORD')
basic_auth = BasicAuth(app)

@app.route('/')
@basic_auth.required
def index():
    return render_template_string('''
        <!doctype html>
        <title>Run Python Script</title>
        <h1>Upload and Run Python Script</h1>
        <form method=post enctype=multipart/form-data>
          <input type=file name=file>
          <input type=submit value=Run>
        </form>
        ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)