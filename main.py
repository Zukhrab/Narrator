from gtts import gTTS

text = "Добро пожаловать в мир Python!"
language = "ru"
filename = "welcome.mp3"

tts = gTTS(text=text, lang=language)
tts.save(filename)