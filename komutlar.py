from Assistan import *
import webbrowser,wikipedia,time
from wikipedia.exceptions import PageError
import pywhatkit as kit
import pyautogui as pg


def commands(command):
    if "nasılsın" in command:
        speak("Teşekkürler, iyiyim efendim")
    if "youtube müzik aç" in command:
        speak("Açmak istediğiniz müzik ismini söyler misiniz ?")
        music = take_commands()
        speak(f"{music} açılıyor")
        kit.playonyt(music) 
    if "youtube aç" in command:
        webbrowser.open("http://youtube.com")
    if "twitter aç" in command:
        webbrowser.open("http://twitter.com")
    if "araştır" in command:
        speak("Ne araştırmak istersiniz?")
        info = take_commands()
        wikipedia.set_lang("tr")
        speak(f"{info} için arama yapılıyor")
        try:
            bilgi = wikipedia.summary(info,sentences=3)
            speak(bilgi)
        except wikipedia.exceptions.PageError:
            speak(f"{info} hakkında bilgi bulunamadı.")
    if "google" in command:
        speak("Ne google'lamak istersiniz ?")
        bilgi = take_commands()
        speak(f"{bilgi} google'da aratılıyor...")
        kit.search(bilgi)
    if "el yazısı" in command:
        speak("El yazısı kelimesini söyle")
        yazi = take_commands()
        kit.text_to_handwriting(yazi)
    if "not al" in command:
        if os.path.exists("Not.txt"):
            speak("Notunuzu söyleyiniz.")
            f= open("Not.txt", "a")
            note = take_commands()
            f.write(" " +note)
        else:
            speak("Notunuzu söyleyiniz.")
            f = open("Not.txt", "w")
            note = take_commands()
            f.write(note)
    if "ekran değiştir" in command:
        with pg.hold("alt"):
            pg.press("tab")
    if "ses arttır" in command:
        pg.press("volumeup")
    if "sesi azalt" in command:
        pg.press("volumedown")
    if "sesi kapat" in command:
        pg.press("volumemute")
    if "sayfayı yenile" in command:
        pg.press("browserrefresh")
    if "bilgisayarı kapat" in command:
        os.system("shutdown /s /f /t 120")
    if "saat kaç" in command:
        saat = dt.now().strftime("%H:%M")
        speak(f"Saat şu an: {saat}")
    if "şarkı aç" in command:
        speak("Hangi müziği çalmamı istersin ?")
        name = str(input("Şarkı adı: "))
        uri = get_track_uri(spotify=spotify,name=name)
        play_track(spotify=spotify,device_id=deviceID,uri=uri)
    if "şarkıyı kapat" in command:
        pause_track(spotify=spotify,device_id=deviceID)
    if "müzik listesi çal" in command:
        speak("Hangi playlisti açmamı istersin ?")
        name = str(input("playlist adı: "))
        uri=get_playlist_uri(spotify=spotify,name=name)
        play_playlist(spotify=spotify,device_id=deviceID,uri=uri)
    if "sıradaki müzik" in command:
        switch_song(spotify=spotify,device_id=deviceID)
    if "tekrar et" in command:
        loop(spotify=spotify,device_id=deviceID)
    if "tekrarı kapat" in command:
        loop_quit(spotify=spotify,device_id=deviceID)
