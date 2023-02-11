# TRANSFORMANDO TEXTO EM AUDIO -----

from gtts import gTTS
from playsound import playsound


convertendo_texto = 'audio.mp3'
language = 'pt-br'
    

sp = gTTS(
    text = ' O senhor é meu pastor, e nada me faltará',
    lang=language
)

sp.save(convertendo_texto)
playsound(convertendo_texto)
