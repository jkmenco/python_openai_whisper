from gtts import gTTS
import os

# Create a gTTS object
tts = gTTS('este es un texto de prueba', lang='es')

# Save the speech to a file
tts.save('audio_test.mp3')

# Play the speech using afplay on macOS
os.system('afplay audio_test.mp3')