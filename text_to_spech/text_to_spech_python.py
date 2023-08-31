from gtts import gTTS
import os

# Pedir al usuario que ingrese la ruta del archivo de texto
input_file_name = input("Ingrese la ruta del archivo de texto para convertir a audio: --> ")

# Verificar si la ruta del archivo es válida
if not os.path.exists(input_file_name) or not os.path.isfile(input_file_name):
    print("La ruta del archivo no es válida.")
else:
    # Leer el contenido del archivo de texto
    with open(input_file_name, 'r') as file:
        content_text = file.read()

    # Carpeta para guardar
    audio_folder = os.path.abspath("output_file_folder")

    # Crear un objeto gTTS
    tts = gTTS(content_text, lang='es')

    # Asegurarse de que la carpeta exista, si no, crearla
    if not os.path.exists(audio_folder):
        os.makedirs(audio_folder)

    # Guardar el archivo de audio
    audio_output_file = os.path.join(audio_folder, "output_audio.mp3")
    tts.save(audio_output_file)

    # Reproducir el archivo de audio en sistemas Unix (Linux o macOS)
    os.system(f"afplay {audio_output_file}")  # para macOS
    # os.system(f"vlc {audio_output_file}")    # para Linux con VLC instalado
    # Puedes usar otros comandos de reproducción según tu sistema

    # Imprimir la ruta del archivo de salida
    print("Archivo de audio guardado en:", audio_output_file)
