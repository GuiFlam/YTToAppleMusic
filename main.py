from pytubefix import YouTube
from mutagen.easyid3 import EasyID3
from moviepy.video.io.VideoFileClip import VideoFileClip
import eyed3
from eyed3.id3.frames import ImageFrame
import os
import argparse
import shutil
import subprocess
from pydub import AudioSegment

# Define the destination folder for iTunes
itunes_folder = r"C:\Users\<user>\Music\iTunes\iTunes Media\Automatically Add to iTunes"

parser = argparse.ArgumentParser(description='Process a YouTube video.')
parser.add_argument('video_link', type=str, help='The YouTube video link')
parser.add_argument('title', type=str, help='The title of the video')
parser.add_argument('artist', type=str, help='The artist of the video')
parser.add_argument('genre', type=str, help='The genre of the video')
args = parser.parse_args()

# Use the arguments
video = args.video_link
title = args.title
artist = args.artist
genre = args.genre

# Define folders
image_folder = "image/"
output_folder = "output/"

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Find the first image file in the image folder
image_file = None
for file in os.listdir(image_folder):
    if file.endswith(".jpg") or file.endswith(".jpeg"):
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


audio = AudioSegment.from_mp3(mp3_filename)

fixed_file = "fixed_file.mp3"

# Export the file (re-encoding it with proper headers)
audio.export(fixed_file, format="mp3", bitrate="192k")




# Update audio metadata
audio = EasyID3(fixed_file)
audio.clear()
audio['title'] = title
audio['artist'] = artist
audio['album'] = title + " - Single"
audio['genre'] = genre
audio.save()

# Add cover image to the .mp3 file
audiofile = eyed3.load(fixed_file)
if audiofile.tag is None:
    audiofile.initTag()

with open(image_file, 'rb') as img_file:
    audiofile.tag.images.set(ImageFrame.FRONT_COVER, img_file.read(), 'image/jpeg')

audiofile.tag.save()

print("All videos have been processed successfully.")



try:
    shutil.move(os.path.join(fixed_file), os.path.join(itunes_folder, os.path.basename(fixed_file)))
    print(f"MP3 file moved to {itunes_folder}")

    # Open iTunes application
    subprocess.run(["start", "iTunes"], shell=True)
    print("iTunes has been opened.")

    # Remove all files in the image folder
    for file in os.listdir(image_folder):
        file_path = os.path.join(image_folder, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Removed file: {file_path}")
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
            print(f"Removed directory: {file_path}")
except Exception as e:
    print(f"Error moving file: {e}")

