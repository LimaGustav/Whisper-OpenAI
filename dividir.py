from pydub import AudioSegment
import math
import os

# Caminho para o seu áudio
audio_path = "Audio.mp3"

# Carrega o áudio
audio = AudioSegment.from_file(audio_path)

# Duração desejada de cada parte (3 minutos = 3 * 60 * 1000 milissegundos)
chunk_length_ms = 3 * 60 * 1000

# Número total de partes
total_chunks = math.ceil(len(audio) / chunk_length_ms)

# Nome base para os arquivos cortados
base_filename = os.path.splitext(audio_path)[0]

# Cria uma pasta de saída (opcional)
output_dir = "partes"
os.makedirs(output_dir, exist_ok=True)

# Divide e salva os trechos
for i in range(total_chunks):
    start = i * chunk_length_ms
    end = min((i + 1) * chunk_length_ms, len(audio))
    chunk = audio[start:end]
    chunk.export(f"{output_dir}/{base_filename}_parte{i+1}.mp3", format="mp3")
    print(f"Salvo: parte {i+1} de {total_chunks}")

print("✅ Divisão concluída!")
