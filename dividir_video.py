from moviepy import VideoFileClip
import os

def dividir_video_em_partes(caminho_video, duracao_parte=180):
    # Carrega o vídeo
    video = VideoFileClip(caminho_video)
    duracao_total = int(video.duration)
    
    nome_base = os.path.splitext(os.path.basename(caminho_video))[0]
    pasta_saida = f"{nome_base}_partes_video"
    os.makedirs(pasta_saida, exist_ok=True)

    # Divide em partes
    parte = 1
    for inicio in range(0, duracao_total, duracao_parte):
        fim = min(inicio + duracao_parte, duracao_total)
        subclip = video.subclipped(inicio, fim)
        caminho_saida = os.path.join(pasta_saida, f"{nome_base}_parte{parte}.mp4")
        print(f"Exportando parte {parte}: {inicio}s até {fim}s")
        subclip.write_videofile(caminho_saida, codec="libx264", audio_codec="aac", logger=None)
        parte += 1

    print("✅ Divisão concluída!")

# Exemplo de uso:
dividir_video_em_partes("C:\\Users\\OLIMPIADA2024\\Downloads\\Whisper-OpenAI\\filme.mp4")

