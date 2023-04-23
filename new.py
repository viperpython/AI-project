from word2number import w2n
from num2words import num2words
# import main.generate
from io import BytesIO
from gtts import gTTS
import pygame
text=57
res=num2words(text)
print(res)
aout = BytesIO()
tts = gTTS(res,lang='ta',tld='co.in')
tts.write_to_fp(aout)
aout.seek(0)
pygame.mixer.init()
pygame.mixer.music.load(aout)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue