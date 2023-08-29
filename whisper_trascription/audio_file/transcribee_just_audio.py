from moviepy.editor import *
import os
import whisper
import magic

def line_mark():
    print("...")
    print("..")
    print(".")


line_mark()
print()
input_file_name = input("Ingrese la ruta del audio para transcribir ------> ")
print()
line_mark()
input_file_name_formated_r = fr"{input_file_name}"

project_folder = os.path.abspath("output_file_folder")



def is_audio_file(file_path):
    mime_type = magic.from_file(file_path, mime=True)
    return mime_type.startswith('audio/')

def convert_audio_to_mp3(audio_file_path):
    audio = AudioFileClip(audio_file_path)

    if audio.fps != 44100 or audio.nchannels != 2:
        # Si el audio no está en el formato requerido (44.1kHz, 2 canales), convertir a mp3
        mp3_file_path = os.path.splitext(audio_file_path)[0] + ".mp3"
        print("Iniciando conversión a MP3...")
        audio.write_audiofile(mp3_file_path, codec='mp3', fps=44100, nbytes=2, verbose=True)
        print("Conversión a MP3 completa.")
        return mp3_file_path
    else:
        # El audio ya está en el formato requerido, no es necesario realizar la conversión
        return audio_file_path

def transcribe_audio_to_text(audio_file_path):
    try:
        model = whisper.load_model("medium")  # Cargar el modelo "medium" de Whisper
        result = model.transcribe(audio_file_path)  # Realizar la transcripción del audio
        transcript_text = result["text"]  # Obtener el texto transcribido
        return transcript_text
    except Exception as error:
        print(f"Error al transcribir el audio: {str(error)}")
        return None

def process_audio_file(input_file_name):
    input_file_path = os.path.join(project_folder, input_file_name)
    if os.path.exists(input_file_path):
        print(f"Iniciando procesamiento del archivo: {input_file_name}")
        print(f"Ruta completa del archivo: {input_file_path}")

        if not is_audio_file(input_file_path):
            # El archivo no es de audio, convertir a MP3
            mp3_file_path = convert_audio_to_mp3(input_file_path)
        else:
            # El archivo es de audio en formato compatible, no es necesario realizar la conversión
            mp3_file_path = input_file_path

        # Transcribir audio a texto y crear archivo de texto
        transcript_text = transcribe_audio_to_text(mp3_file_path)

        if transcript_text is not None:
            # Crear archivo de texto con la transcripción
            base_file_name = os.path.splitext(os.path.basename(mp3_file_path))[0]
            text_file_path = os.path.join(project_folder, f"{base_file_name}_transcript.txt")
            with open(text_file_path, "w") as text_file:
                text_file.write(transcript_text)

            print(f"Transcripción completa. Archivo de texto creado: {text_file_path}")
        else:
            print("No se pudo realizar la transcripción.")
    else:
        print(f"El archivo no existe en la ruta especificada: {input_file_path}")

# Ingresar el nombre del archivo con su extensión "Tu_archivo_multimedia.mp3" o "Tu_archivo_multimedia.mp4"
process_audio_file(input_file_name)

