import speech_recognition as sr
import pyttsx3 as pt3
from datetime import datetime as dt
from gtts import gTTS
from playsound import playsound
import os

from spotify import *
import pandas as pd
import spotipy as sp 
from spotipy.oauth2 import SpotifyOAuth

def take_commands():
    global cmd
    r=sr.Recognizer()
    with sr.Microphone() as mic:
        print("Dinleniyor..")
        r.pause_threshold = 0.7
        ses = r.listen(mic)
        try:
            print("Ses Algılanıyor...")
            cmd = r.recognize_google(ses,language='tr-TR')
            print(f"Komutunuz: {cmd}")
        except sr.UnknownValueError:
            print("Ses Algılanamadı!")
        except sr.RequestError:
            print("Sistem çalışmıyor!")
    return str(cmd).lower()

def speak(kelime):
    tts = gTTS(text=kelime,lang='tr',slow=False)
    file = "C:/Users/Atakan/Desktop/Python/answer.mp3"
    if not os.path.exists(file):
        tts.save(file)
        playsound(file)
        os.remove(file)
    else:
        os.remove(file)

#Spotfiy İçin olan kısım
spoti_auth = pd.read_csv('C:\\Users\\Atakan\\Desktop\\Python\\spotify_auth.txt', sep='=',index_col=0,squeeze=True,header=None)
client_id=spoti_auth['client_id']
client_secret=spoti_auth['client_secret']
device_name=spoti_auth['device_name']
redirect_uri=spoti_auth['redirect_uri']
scope=spoti_auth['scope']
username=spoti_auth['username']

#Spotify Bağlanma Kısımı
auth_manager = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope,
    username=username,
)
spotify = sp.Spotify(auth_manager=auth_manager)

#Cihaz Seçimi
devices = spotify.devices()
deviceID = None

for d in devices['devices']:
    d['name'] = d['name'].replace('´','\'')
    if d['name'] == device_name:
        deviceID=d['id']
        break




