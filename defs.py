from spotdl import Spotdl
import os,platform
import streamlit as st
from pathlib import Path
def process_spot_track(aname, y, match,directory,track_url,dance,tgram):
    id = st.secrets["ID"]
    secret = st.secrets["SECRET"]
    sp = Spotdl(client_id=id, client_secret=secret)
    if match >= 37 or dance>=37:
        query = f"{aname} {y}"
        #print(query)
        songs = sp.search([
            query])
        vidurl = songs[0].url
        print(vidurl)
        if vidurl != None: #"No results found."
            song, fpath = sp.download(songs[0])
            try:
                os.rename(fpath, os.path.join(directory, fpath))
            except (FileExistsError,TypeError):
                print("File exists..Or some error")
                return
            #file = open(f'{directory}/songs.txt', 'a')
            try:
                #file.write(f"{y} url: {vidurl}, Energy: {match}, Stats: {track_url}\n")
                print(f"{y} Success, Energy={match}")
                tgram[2]=vidurl
                #format_and_print_artist_info(fpath,*tgram)
            except UnicodeEncodeError:
                #file.write(f"Name Error; url: {vidurl}, Energy: {match}, Stats: {track_url}\n")
                pass
            #file.close()

        else:
            print("Video not found :(")
    else:
        print(f"{y} Failed test, Energy={match}, Dancebility={dance}")


def install_ffmpeg():
    os_type = platform.system()  # Detect the OS
    try:
        if os_type == "Windows":
            print("Installing FFmpeg on Windows...")
            # Download FFmpeg zip (change URL to the latest version)
            os.system(
                "curl -O https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip")
            # Extract and set PATH (assumes you have 'tar' or a similar tool)
            os.system("tar -xf ffmpeg-master-latest-win64-gpl.zip")
            os.environ["PATH"] += os.pathsep + os.path.abspath("ffmpeg-master-latest-win64-gpl/bin")
            print("FFmpeg installed successfully.")

        elif os_type == "Linux":
            print("Installing FFmpeg on Linux...")
            os.system("sudo apt update && sudo apt install -y ffmpeg")
            print("FFmpeg installed successfully.")

        elif os_type == "Darwin":  # macOS
            print("Installing FFmpeg on macOS...")
            os.system("brew install ffmpeg")
            print("FFmpeg installed successfully.")

        else:
            print(f"Unsupported OS: {os_type}")
    except Exception as e:
        print(f"Error during FFmpeg installation: {e}")
