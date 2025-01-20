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

def download(sp,query):
    songs = sp.search([
        query])
    song, fpath = sp.download(songs[0])
    st.write(fpath)
    st.audio(fpath)
