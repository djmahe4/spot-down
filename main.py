import streamlit as st
import os,subprocess
from spotdl import Spotdl,Song#,Album
from pathlib import Path,WindowsPath
from spotdl.types.album import Album
st.title("Latest Spotify Downloader")
#st.audio("SZA - Kill Bill.mp3")
if "init" not in st.session_state:
    st.session_state.init=False
if "sp" not in st.session_state:
    st.session_state.sp=None
if "downloads" not in st.session_state:
    st.session_state.downloads=[]
def init():
    #os.run("spotdl --download-ffmpeg")
    subprocess.run(["spotdl","--download-ffmpeg"])
    sp = Spotdl(client_id='16a580bdff3b4b6f822804fb6372712c', client_secret='7b7b8f6350bb452a880cf2a2adab3187')
    st.session_state.init=True
    st.session_state.sp=sp
    #client_secret="7b7b8f6350bb452a880cf2a2adab3187"))
if st.session_state.init==False:
    init()
# import feedparser,requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone
#parsed= feedparser.parse(requests.get("https://www.youtube.com/feeds/videos.xml?playlist_id=PLFgquLnL59am6SD582GSakLhVkvLc9mDv").text)
if st.session_state.init:
    c=Album.from_url("https://open.spotify.com/album/6zAGbr91kKHWKlyMPPcaJT")
    #spotdl.download("https://open.spotify.com/album/5RQOjmGOFpakyk5VmVAI9E")
    print(c)
    d=st.session_state.sp.download_songs(c.songs)
    st.session_state.downloads=d
    #d=[(Song(name="I'm Not In Love", artists=['Emily James'], artist='Emily James', genres=[], disc_number=1, disc_count=1, album_name='I’m Not In Love / Who Would’ve Thought', album_artist='Emily James', album_type='single', duration=187, year=2023, date='2023-09-22', track_number=1, tracks_count=2, song_id='0E5qs1cpZclZrTRAlhuyMh', explicit=False, publisher='Nettwerk Music Group', url='https://open.spotify.com/track/0E5qs1cpZclZrTRAlhuyMh', isrc='CAN112301580', cover_url='https://i.scdn.co/image/ab67616d0000b2730faef05ab7d81bedc27266bb', copyright_text='2023 Emily James under exclusive license to Nettwerk Music Group Inc.', download_url='https://music.youtube.com/watch?v=w6_s-7W_DyU', lyrics=None, popularity=27, album_id='6zAGbr91kKHWKlyMPPcaJT', list_name=None, list_url=None, list_position=None, list_length=None, artist_id='7FxEy78P0oIVEVxdaL9npy'), WindowsPath("Emily James - I'm Not In Love.mp3")), (Song(name="Who Would've Thought", artists=['Emily James'], artist='Emily James', genres=[], disc_number=1, disc_count=1, album_name='I’m Not In Love / Who Would’ve Thought', album_artist='Emily James', album_type='single', duration=236, year=2023, date='2023-09-22', track_number=2, tracks_count=2, song_id='47InLMACV8Tl2JgZL2tVPA', explicit=False, publisher='Nettwerk Music Group', url='https://open.spotify.com/track/47InLMACV8Tl2JgZL2tVPA', isrc='CAN112301581', cover_url='https://i.scdn.co/image/ab67616d0000b2730faef05ab7d81bedc27266bb', copyright_text='2023 Emily James under exclusive license to Nettwerk Music Group Inc.', download_url='https://music.youtube.com/watch?v=c1movZHuwjw', lyrics=None, popularity=45, album_id='6zAGbr91kKHWKlyMPPcaJT', list_name=None, list_url=None, list_position=None, list_length=None, artist_id='7FxEy78P0oIVEVxdaL9npy'), WindowsPath("Emily James - Who Would've Thought.mp3"))]
    loc={}
    for i in st.session_state.downloads:
        st.write(i[1].name)
        loc.update({i[0].name:i[1].name})
        st.audio(i[1].name)
    print(loc)
    st.write(loc)

