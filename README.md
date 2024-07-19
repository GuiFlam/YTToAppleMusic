# YTToAppleMusic

## How to use (Local version)

1. Clone the repository
2. Run the virtual environment by running `python -m venv venv` and then `venv\Scripts\activate` on Windows or `source venv/bin/activate` on MacOS/Linux
3. Run `pip install -r requirements.txt`
Here is the custom song cover I will use for this example:
<p align="center">
  <img src="misc/example.jpg" alt="Main Image" width="300">
</p>

1. Put the song cover in the `image` folder (make sure it is a `.jpg` file and the aspect ratio is 1:1)
2. Put your iTunes library path in the `main.py` file
```python
itunes_folder = r"C:\Users\user\Music\iTunes\iTunes Media\Automatically Add to iTunes"
```
3. Save the file and run the `main.py` with the following arguments:
```bash
python main.py https://www.youtube.com/videolink --title "TheFatRat - Monody (feat. Laura Brehm)" --artist "TheFatRat" --album "Monody" --genre "Electronic"
```
1. The script will download the video, convert it to an audio file, add the metadata into the audio file and then add it to your iTunes library so you can listen to it on your Apple Music library

## Preview 

Here is a preview of the song in my Apple Music library:
<p align="center">
  <img src="misc/preview.jpg" alt="Main Image" width="700">
</p>

## How to use (Server version)

1. Create a new file called `.env` and fill in the values
```env
USERNAME=yourusername
PASSWORD=yourpassword
```
1. Run the server by running `python server.py`
2. Connect to the server by going to `http://yourlocalip:5000` on your browser
3. Fill in the values and click on the `Submit` button