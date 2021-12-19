from spotipy import Spotify
import json

class InvalidSearchError(Exception):
    pass

def get_track_uri(spotify= Spotify, name=None):
    original = name
    name=name.replace(' ', "+")

    results = spotify.search(q=name,limit=1,type='track')

    if not results['tracks']['items']:
        raise InvalidSearchError(f'{original} isminde şarkı bulunamadı')
    track_uri=results['tracks']['items'][0]['uri']
    return track_uri

def get_playlist_uri(spotify= Spotify, name=None):
    original = name
    name=name.replace(' ', "+")

    results = spotify.search(q=name,limit=1,type='playlist')

    if not results['playlists']['items']:
        raise InvalidSearchError(f'{original} isminde şarkı bulunamadı')
    playlist_uri=results['playlists']['items'][0]['uri']
    return playlist_uri


def play_track(spotify= None, device_id=None,uri=None):
    spotify.start_playback(device_id=device_id,uris=[uri])

def pause_track(spotify= None, device_id=None):
    spotify.pause_playback(device_id=device_id)

def play_playlist(spotify= None, device_id=None,uri=None):
    spotify.start_playback(device_id=device_id,context_uri=uri)

def switch_song(spotify=None,device_id=None):
    spotify.next_track(device_id=device_id)

def loop(spotify=None,device_id=None):
    spotify.repeat(state='track',device_id=device_id)

def loop_quit(spotify=None,device_id=None):
    spotify.repeat(state='context',device_id=device_id)