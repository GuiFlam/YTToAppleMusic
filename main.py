from pytubefix import YouTube
from mutagen.easyid3 import EasyID3
from moviepy.video.io.VideoFileClip import VideoFileClip
import eyed3
from eyed3.id3.frames import ImageFrame
import os


# Add your video link, title, and artist here
video = "https://www.youtube.com/watch?v=VqT55Cwp_b0"
title = "GONE, GONE THANK YOU"
artist = "Tyler, The Creator"
genre = "Hip-Hop/Rap"

# Define folders
image_folder = "image/"
output_folder = "output/"

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Find the first image file in the image folder
image_file = None
for file in os.listdir(image_folder):
    if file.endswith(".jpg"):
        image_file = os.path.join(image_folder, file)
        print("Image file found: " + image_file)
        break

yt = YouTube(video)
video = yt.streams.filter().first()

out_file = video.download(output_path=output_folder)

# Rename the downloaded file to .mp4
base, ext = os.path.splitext(out_file)
new_file = base + '.mp4'
os.rename(out_file, new_file)
print(yt.title + " has been successfully downloaded.")  

# Extract audio and save as .mp3
clip = VideoFileClip(new_file)
mp3_filename = os.path.join(output_folder, f"{title}.mp3")
clip.audio.write_audiofile(mp3_filename)
clip.close()

# Remove the .mp4 file
os.remove(new_file)

# Update audio metadata
audio = EasyID3(mp3_filename)
audio['title'] = title
audio['artist'] = artist
audio['album'] = title + " - Single"
audio['genre'] = genre
audio.save()

# Add cover image to the .mp3 file
audiofile = eyed3.load(mp3_filename)
if audiofile.tag is None:
    audiofile.initTag()

with open(image_file, 'rb') as img_file:
    audiofile.tag.images.set(ImageFrame.FRONT_COVER, img_file.read(), 'image/jpeg')

audiofile.tag.save()

print("All videos have been processed successfully.")
