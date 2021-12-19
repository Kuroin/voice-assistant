from Assistan import *
from komutlar import commands,time

if __name__ == '__main__':
    WAKE="tako"
    print("Başlatılıyor...")
    while True:      
        komut = take_commands()
        
        if komut.count(WAKE) > 0:
            speak("Buyrun efendim")
            komut = take_commands()
            commands(komut)
            if "çıkış yap" in komut:
                speak("İyi günler efendim")
                break
            if "bekle" in komut:
                time.sleep(120)
