import os
import shutil

def organizar_arquivos(diretorio):
    caminho_documentos = os.path.join(os.path.expanduser('~'), 'Documents')     # Define os caminhos para as pastas 
    caminho_imagens = os.path.join(os.path.expanduser('~'), 'Pictures')
    caminho_videos = os.path.join(os.path.expanduser('~'), 'Videos')
    caminho_musicas = os.path.join(os.path.expanduser('~'), 'Music')


    for arquivo in os.listdir(diretorio):
        if os.path.isfile(os.path.join(diretorio, arquivo)):        # Verifica se é um arquivo e não uma pasta
            extensao = os.path.splitext(arquivo)[1].lower()
            destino_encontrado = False
            
            if extensao in ['.jpg', '.jpeg', '.png', '.gif']:
                shutil.move(os.path.join(diretorio, arquivo), os.path.join(caminho_imagens, arquivo))
                destino_encontrado = True
            elif extensao in ['.mp4', '.mkv']:
                shutil.move(os.path.join(diretorio, arquivo), os.path.join(caminho_videos, arquivo))
                destino_encontrado = True
            elif extensao in ['.pdf', '.docx', '.txt']:
                shutil.move(os.path.join(diretorio, arquivo), os.path.join(caminho_documentos, arquivo))
                destino_encontrado = True
            elif extensao in ['.mp3']:
                shutil.move(os.path.join(diretorio, arquivo), os.path.join(caminho_musicas, arquivo))
                destino_encontrado = True

            if not destino_encontrado:      ## se extensao nao estiver definida mantem em downloads
                print(f"Extensão não reconhecida para o arquivo: {arquivo}")

if __name__ == "__main__":
    caminho_diretorio = os.path.join(os.path.expanduser('~'), 'Downloads')
    organizar_arquivos(caminho_diretorio)
