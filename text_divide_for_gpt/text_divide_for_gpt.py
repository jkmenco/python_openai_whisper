
def split_text_into_segments(text, segment_length):
    segments = []
    start = 0
    while start < len(text):
        segment = text[start:start + segment_length]
        segments.append(segment)
        start += segment_length
    return segments

def save_segments_to_files(segments, file_prefix):
    for i, segment in enumerate(segments):
        try:
            with open(f"{file_prefix}_{i + 1}.txt", "w") as file:
                file.write(segment) 
        except Exception as e:
            print(f"Error al guardar el segmento {i + 1}: {str(e)}")


file_path = input("Ingrese la ruta del archivo --> ")
with open(file_path, "r") as file:
    text_content = file.read()

segment_length = 2048
text_segments = split_text_into_segments(text_content, segment_length)

file_prefix = file_path.split("/")[-1].split(".")[0]
save_segments_to_files(text_segments, file_prefix)