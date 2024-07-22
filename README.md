# YTToAppleMusic

## Description

This is a python script that allows you to choose a song/podcast from youtube and add it to your Apple Music library. The script will download the video, convert it to an audio file, add the metadata into the audio file and then add it to your iTunes library so you can listen to it on your Apple Music library. 

This project has been made for Windows and hasn't been tested on other operating systems.

## Setup
1. Clone the repository
2. Run the virtual environment by running 
```bash   
python -m venv venv
```
and 
```bash
.\venv\Scripts\activate
```
3. Install the packages: 
```bash
pip install -r requirements.txt
```
4. You need to have iTunes installed on your computer
5. Put the path to your `Automatically Add to iTunes` folder in the `main.py` file at line 12
```python
itunes_folder = r"C:\Users\<user>\Music\iTunes\iTunes Media\Automatically Add to iTunes"
```
6. Create a new file called `.env` at the root of the project and fill in the values
```env
USERNAME=yourusername
PASSWORD=yourpassword
```

## How to use 

1. Run the server by running (make sure the virtual environment is activated)
```bash
python server.py
```
2. Open the web application by going to `http://yourlocalip:5000` (you can get your local ip by entering `ipconfig` in the terminal and selecting the IPV4 address) on your browser if you are on another device, or `http://127.0.0.1:5000` if you are on the same device running the server
3. Fill in the values and click on the `Submit` button and make sure the image is a `.jpg` or `.jpeg` file and the aspect ratio is 1:1 or else the image won't get uploaded to the iTunes library
<p align="center">
  <img src="misc/fill.jpg" alt="Main Image" width="400">
</p>
4. The script will download the video, convert it to an audio file, add the metadata into the audio file and then add it to your iTunes library so you can listen to it on your Apple Music library. In the process, your iTunes application will open, so make sure to not close it until the song is added to your library, if you close it, the song won't be added to your library and will stay offline in your iTunes library until you open the application again.
   
## Preview 

Here is a preview of the song in my Apple Music library:
<p align="center">
  <img src="misc/preview.jpg" alt="Main Image" width="700">
</p>

