import sounddevice # bu iki kütüphaneyi yükleyelim.
from scipy.io.wavfile import write


freq = 44100  #öncelikle bir frekans belirleyelim 44100 ile 48000 arasında değer verebilirsiniz.

süre = int (input("kaç saniyelik bir ses kaydı yapmak istiyorsunuz")) # kaç saniye kayıt alınacağını yazalım, hatta bunu kullanıcıya yazdıralım.

kayit = sounddevice.rec(int(süre * freq), samplerate=freq,
                        channels=2)  # kayıt için bir isim verelerim ve kayıdı başlatalım. Parametreleri girelim ve 1 veya 2 olarak kanalı belirleyelim.
sounddevice.wait()

write("kayit.wav", freq, kayit)  #kayıt edilecek dosya adını ve dizini seçelim ve dosyanın üzerine yazdıralım.
