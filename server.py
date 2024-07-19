from flask import Flask, request, render_template_string, redirect, url_for
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

# Define the path to the 'image' folder
UPLOAD_FOLDER = 'image/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the image folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Path to the venv
path = os.path.join(os.getcwd(), 'venv', 'Scripts', 'python')

@app.route('/', methods=['GET', 'POST'])
@basic_auth.required
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        video_link = request.form.get('video_link')
        title = request.form.get('title')
        artist = request.form.get('artist')
        genre = request.form.get('genre')
        
        if file:
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            result = subprocess.run([
                path, "main.py",
                video_link, title, artist, genre
            ], capture_output=True, text=True)

            # Redirect to a different route after POST
            return redirect(url_for('result', result_stdout=result.stdout, result_stderr=result.stderr))

    return render_template_string('''
        <!doctype html>
        <h1>Youtube to Apple Music</h1>
        <form method=post enctype=multipart/form-data>
          <label for="file">Upload File:</label>
          <input type=file name=file><br><br>

          <label for="video_link">Video Link:</label>
          <input type=text name=video_link><br><br>

          <label for="title">Title:</label>
          <input type=text name=title><br><br>

          <label for="artist">Artist:</label>
          <input type=text name=artist><br><br>

          <label for="genre">Genre:</label>
          <input type=text name=genre><br><br>

          <input type=submit value=Submit>
        </form>
    ''')

@app.route('/result')
@basic_auth.required
def result():
    stdout = request.args.get('result_stdout', '')
    stderr = request.args.get('result_stderr', '')

    return f'''
        <h2>Form Submitted</h2>
        <h3>Script Output:</h3>
        <pre>{stdout}</pre>
        <h3>Errors (if any):</h3>
        <pre>{stderr}</pre>
        <br>
        <form action="/" method="get">
            <button type="submit">Back to Form</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
