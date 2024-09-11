from mutagen.mp3 import MP3

# Load the MP3 file
audio = MP3('.\output\Mo City Flexologist.mp3')

# Get the duration in seconds
duration = audio.info.length
print(f"Duration: {duration/60} seconds")
