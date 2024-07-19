from flask import Flask, request, render_template_string
from flask_basicauth import BasicAuth
from dotenv import load_dotenv
import os
import subprocess

# Load environment variables from .env file
load_dotenv()

print(f"USERNAME: {os.getenv('USERNAME')}")
print(f"PASSWORD: {os.getenv('PASSWORD')}")

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = os.getenv('USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.getenv('PASSWORD')
basic_auth = BasicAuth(app)

# Define the path to the 'image' folder
UPLOAD_FOLDER = 'image/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
        else:
            file_response = 'No file uploaded'

        return f'''
                <h2>Form Submitted</h2>
                <p>Video Link: {video_link}</p>
                <p>Title: {title}</p>
                <p>Artist: {artist}</p>
                <p>Genre: {genre}</p>
                <h3>Script Output:</h3>
                <pre>{result.stdout}</pre>
                <h3>Errors (if any):</h3>
                <pre>{result.stderr}</pre>
            '''

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)