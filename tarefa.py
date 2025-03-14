import os
import shutil
# import schedule
# import time

# Caminho para a pasta Downloads do usuário
DOWNLOADS_PATH = os.path.expanduser("~/Downloads")

# Definição das categorias e extensões
CATEGORIAS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Áudios": [".mp3", ".wav", ".aac", ".ogg", ".flac"],
    "Vídeos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
    "Compactados": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Executáveis": [".exe", ".msi", ".sh", ".bat"],
    "Outros": []
}

def organizar_downloads():
    if not os.path.exists(DOWNLOADS_PATH):
        print(f"A pasta {DOWNLOADS_PATH} não existe.")
        return

    for arquivo in os.listdir(DOWNLOADS_PATH):
        caminho_arquivo = os.path.join(DOWNLOADS_PATH, arquivo)
        
        if os.path.isfile(caminho_arquivo):
            _, extensao = os.path.splitext(arquivo)
            extensao = extensao.lower()
            
            # Identificar a categoria do arquivo
            categoria = "Outros"
            for cat, extensoes in CATEGORIAS.items():
                if extensao in extensoes:
                    categoria = cat
                    break
            
            # Criar pasta se não existir
            pasta_destino = os.path.join(DOWNLOADS_PATH, categoria)
            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)
            
            # Mover o arquivo para a pasta correspondente
            shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))
            print(f"Movido: {arquivo} -> {pasta_destino}")
            

            
#schedule.every().day.at("12:15").do(organizar_downloads)
#quero que a aplicação rode a cada a cada hora ate as 17:00
# schedule.every().hour.until("17:00").do(organizar_downloads)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

if __name__ == "__main__":
    organizar_downloads()
